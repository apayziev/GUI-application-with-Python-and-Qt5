from abc import ABC, abstractmethod
from unittest import removeResult
from settings import db_path
import sqlite3


class BaseModel(ABC):

    def __init__(self, id=None) -> None:
        self.id = id
        self.__isValid = True

    @property
    def isValid(self):
        return self.__isValid

    @isValid.setter
    def isValid(self, isValid):
        self.__isValid = isValid

    @abstractmethod
    def save_to_db(self):
        pass

    @abstractmethod
    def delete_data(self):
        pass

    @classmethod
    @abstractmethod
    def objects():
        pass

    @abstractmethod
    def get_by_id(id):
        pass

    @classmethod
    @abstractmethod
    def getCourses():
        pass

    @abstractmethod
    def get_course_id(course_name):
        pass


class Courses(BaseModel):
    """This class represents all courses"""

    table = "Courses"

    def __init__(self, name, id=None) -> None:
        super().__init__(id)
        self.name = name

    # Setters and getters for all attributes

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            self.__name = ''
            self.isValid = False

    def __str__(self):
        return (f"{self.id} {self.name}")

    def objects():
        try:
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
        else:
            for row in cursor.execute(f"SELECT * FROM {Courses.table}"):
                yield Courses(row[1], row[0])

    # Save to list the courses name
    def getCourses():
        courses = []
        try:
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
        else:
            try:
                for row in cursor.execute(f"SELECT * FROM {Courses.table}"):
                    courses.append(row[1])
            except sqlite3.Error as e:
                print(f"Error getting courses from database: {e}")
        finally:
            return courses

    def save_to_db(self):
        """This method saves a course to the database"""
        if self.isValid:
            try:
                with sqlite3.connect(db_path) as conn:
                    cursor = conn.cursor()
            except sqlite3.Error as e:
                print(f"Error connecting to database: {e}")
            else:
                try:
                    if self.id is None:
                        cursor.execute(
                            f"INSERT INTO {Courses.table} (name) VALUES (:name)", {'name': self.name})
                        self.id = cursor.lastrowid
                    else:
                        cursor.execute(
                            f"UPDATE {Courses.table} SET name=:name WHERE id=:id", {'name': self.name, 'id': self.id})
                except sqlite3.Error as e:
                    print(f"Error saving course to database: {e}")
                    conn.rollback()
                else:
                    conn.commit()
        else:
            return False

    def delete_data(self):
        """This method deletes a course from the database"""
        if self.isValid:
            try:
                with sqlite3.connect(db_path) as conn:
                    cursor = conn.cursor()
            except sqlite3.Error as e:
                print(f"Error connecting to database: {e}")
            else:
                try:
                    cursor.execute(
                        f"DELETE FROM {Courses.table} WHERE id=:id", {'id': self.id})
                except sqlite3.Error as e:
                    print(f"Error deleting course from database: {e}")
                    conn.rollback()
                else:
                    conn.commit()
        else:
            return False

    def get_by_id(id):
        """This method returns a course by id"""
        try:
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
        else:
            try:
                takeItem = cursor.execute(
                    f"SELECT * FROM {Courses.table} WHERE id=:id", {'id': id}).fetchone()
                if takeItem is not None:
                    return Courses(takeItem[1], takeItem[0])
                else:
                    raise ValueError("No such course")
            except sqlite3.Error as e:
                print(f"Error getting course from database: {e}")

    # get the course name and return it's id
    def get_course_id(course_name):
        try:
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
        else:
            try:
                takeItem = cursor.execute(
                    f"SELECT * FROM {Courses.table} WHERE name=:name", {'name': course_name}).fetchone()
                if takeItem is not None:
                    return takeItem[0]
                else:
                    raise ValueError("No such course")
            except sqlite3.Error as e:
                print(f"Error getting course from database: {e}")
