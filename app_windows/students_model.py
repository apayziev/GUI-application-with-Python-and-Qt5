from abc import ABC, abstractmethod
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
    def delete_student(self):
        pass

    @classmethod
    @abstractmethod
    def objects():
        pass

    @abstractmethod
    def get_by_id(id):
        pass


class AllStudents(BaseModel):
    """This class represents all students"""

    table = "Students"

    def __init__(self, surname, name, address, dob, marital_status, passport, courseID, id=None, ) -> None:
        super().__init__(id)
        self.surname = surname
        self.name = name
        self.address = address
        self.dob = dob
        self.marital_status = marital_status
        self.passport = passport
        self.courseID = courseID

    # Setters and getters for all attributes

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if isinstance(surname, str):
            self.__surname = surname
        else:
            self.isValid = False
            raise TypeError("Surname must be a string")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            self.isValid = False
            raise TypeError("Name must be a string")

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        if isinstance(address, str):
            self.__address = address
        else:
            self.isValid = False
            raise TypeError("Address must be a string")

    @property
    def dob(self):
        return self.__dob

    @dob.setter
    def dob(self, dob):
        if isinstance(dob, str):
            self.__dob = dob
        else:
            self.isValid = False
            raise TypeError("DOB must be a string")

    @property
    def marital_status(self):
        return self.__marital_status

    @marital_status.setter
    def marital_status(self, marital_status):
        if isinstance(marital_status, str):
            self.__marital_status = marital_status
        else:
            self.isValid = False
            raise TypeError("Marital status must be a string")

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, passport):
        if isinstance(passport, str):
            self.__passport = passport
        else:
            self.isValid = False
            raise TypeError("Passport must be a string")

    @property
    def courseID(self):
        return self.__courseID

    @courseID.setter
    def courseID(self, courseID):
        if isinstance(courseID, int):
            self.__courseID = courseID
        else:
            self.isValid = False
            raise TypeError("Course must be a integer")

    def __str__(self):
        return (f"{self.id} {self.surname} {self.name} {self.address} {self.dob} {self.marital_status} {self.passport} {self.courseID}")

    def save_to_db(self):
        """This method saves the student to the database"""
        if self.isValid:
            try:
                with sqlite3.connect(db_path) as conn:
                    cursor = conn.cursor()
            except sqlite3.Error as e:
                print(f"Error connecting to database: {e}")
            else:
                try:
                    if self.id is None:
                        # Insert new student into database
                        cursor.execute(f"INSERT INTO {self.table} (surname, name, address, dob, MaritalStatus, passport, courseID) VALUES (:surname, :name, :address, :dob, :MaritalStatus, :passport, :courseID)",
                                       {'surname': self.surname,
                                        'name': self.name,
                                        'address': self.address,
                                        'dob': self.dob,
                                        'MaritalStatus': self.marital_status, 'passport': self.passport,
                                        'courseID': self.courseID})
                        self.id = cursor.lastrowid
                    else:
                        # update existing student in database
                        cursor.execute(f"UPDATE {self.table} SET surname=:surname, name=:name, address=:address, dob=:dob, MaritalStatus=:MaritalStatus, passport=:passport, courseID=:courseID WHERE {self.table}.id=:id",
                                       {'surname': self.surname,
                                        'name': self.name,
                                        'address': self.address,
                                        'dob': self.dob,
                                        'MaritalStatus': self.marital_status, 'passport': self.passport,
                                        'courseID': self.courseID, 'id': self.id})
                except sqlite3.Error as e:
                    print(f"Error saving student to database: {e}")
                    conn.rollback()
                finally:
                    conn.commit()
                return True
        else:
            return False

    def objects():
        """This method returns all students from the database"""
        try:
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
        else:
            try:
                for row in cursor.execute(f"SELECT * FROM {AllStudents.table}"):
                    yield AllStudents(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[0])
            except sqlite3.Error as e:
                print(f"Error getting students from database: {e}")

    def delete_student(self):
        """This method deletes a student from the database"""
        try:
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
        else:
            try:
                cursor.execute(
                    f"DELETE FROM {self.table} WHERE id=:id", {'id': self.id})
            except sqlite3.Error as e:
                print(f"Error deleting student from database: {e}")
                conn.rollback()
            else:
                conn.commit()
                return True

    def get_by_id(self):
        """This method returns a student from the database"""
        try:
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
        else:
            try:
                cursor.execute(
                    f"SELECT * FROM {self.table} WHERE id=:id", {'id': self.id})
                row = cursor.fetchone()
                return AllStudents(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[0])
            except sqlite3.Error as e:
                print(f"Error getting student from database: {e}")
                conn.rollback()


