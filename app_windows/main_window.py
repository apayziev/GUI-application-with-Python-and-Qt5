from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from new_student_window import NewStudentWindow
from help_window import HelpWindow
from all_students_window import AllStudentsWindow
from new_course_window import NewCourseWindow
from all_courses_window import AllCoursesWindow
import sys


class Window(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.initActions()
        self.initMenu()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon("images/icon.png"))
        self.showMaximized()

    def initActions(self):
        self.saveAction = QAction(QIcon("images/save.png"), "&Save", self)
        self.exitAction = QAction("&Exit", self)
        self.exitAction.setStatusTip("Exit application")
        self.exitAction.setShortcut("Alt+F4")
        self.exitAction.triggered.connect(qApp.quit)

        self.newStudentAction = QAction(
            QIcon("images/add-user.png"), "&New student", self)
        self.newStudentAction.triggered.connect(self.show_new_student_window)

        self.allStudentAction = QAction(
            QIcon("images/all-users.png"), "&All students", self)
        self.allStudentAction.triggered.connect(self.show_all_students_window)

        self.newCourseAction = QAction(
            QIcon("images/add-course.png"), "&New course", self)
        self.newCourseAction.triggered.connect(self.show_new_course_window)

        self.allCoursesAction = QAction(
            QIcon("images/all-courses.png"), "&All courses", self)
        self.allCoursesAction.triggered.connect(self.show_all_courses_window)

        self.aboutAction = QAction(QIcon("images/about.png"), "&About", self)
        self.aboutAction.triggered.connect(self.help_window)

    def show_new_student_window(self):
        self.newStudentWindow = NewStudentWindow()
        self.newStudentWindow.show()

    def show_all_students_window(self):
        self.allStudentsWindow = AllStudentsWindow()
        self.allStudentsWindow.show()

    def show_new_course_window(self):
        self.newCourseWindow = NewCourseWindow()
        self.newCourseWindow.show()

    def show_all_courses_window(self):
        self.allCoursesWindow = AllCoursesWindow()
        self.allCoursesWindow.show()

    def help_window(self):
        self.helpWindow = HelpWindow()
        self.helpWindow.show()

    def initMenu(self):
        menuBar = self.menuBar()
        self.setMenuBar(menuBar)

        fileMenu = menuBar.addMenu("&File")
        menuBar.setStyleSheet("font-size: 20px;")
        fileMenu.addAction(self.saveAction)
        fileMenu.addAction(self.exitAction)

        servicesMenu = menuBar.addMenu("&Students")
        servicesMenu.addAction(self.newStudentAction)
        servicesMenu.addAction(self.allStudentAction)

        coursesMenu = menuBar.addMenu("&Courses")
        coursesMenu.addAction(self.newCourseAction)
        coursesMenu.addAction(self.allCoursesAction)

        helpMenu = menuBar.addMenu("&Help")
        helpMenu.addAction(self.aboutAction)

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, "Message", "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.showMaximized()
    sys.exit(app.exec_())
