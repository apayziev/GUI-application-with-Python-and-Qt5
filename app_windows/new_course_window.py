from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from courses_model import Courses


class NewCourseWindow(QWidget):

    def __init__(self, new_course_added):
        super().__init__()
        self.initUI()
        
        self.new_course_added = new_course_added

    def initUI(self):
        self.setWindowTitle("New Course")
        self.setGeometry(30, 120, 400, 200)
        self.setWindowIcon(QIcon("images/icon.png"))
        self.setFixedSize(self.size())

        # courseLabel
        self.courseLabel = QLabel("Course name: ", self)
        self.courseLabel.setGeometry(30, 30, 150, 30)
        self.courseLabel.setFont(QFont("Arial", 12))
        self.courseLabel.setStyleSheet("color: Black; font-weight: bold;")

        # courseLine
        self.courseLine = QLineEdit(self)
        self.courseLine.setGeometry(180, 30, 200, 30)
        self.courseLine.setFont(QFont("Arial", 12))
        self.courseLine.textChanged.connect(self.on_text_changed)
        self.courseLine.returnPressed.connect(self.on_return_pressed)
        self.courseLine.setPlaceholderText("Type course name")
        self.courseLine.setMaxLength(20)
        self.courseLine.setEchoMode(QLineEdit.Normal)
        self.courseLine.setClearButtonEnabled(True)

        # addButton
        self.addButton = QPushButton("Add", self)
        self.addButton.setDefault(True)
        self.addButton.setGeometry(190, 100, 90, 40)
        self.addButton.setFont(QFont("Arial", 12))
        self.addButton.clicked.connect(self.on_add_button_clicked)

        # cancelButton
        self.cancelButton = QPushButton("Cancel", self)
        self.cancelButton.setGeometry(290, 100, 90, 40)
        self.cancelButton.setFont(QFont("Arial", 12))
        self.cancelButton.clicked.connect(self.on_cancel_button_clicked)

        self.setWindowModality(Qt.ApplicationModal)

    def on_add_button_clicked(self):
        course = Courses(self.courseLine.text().upper())
        if self.courseLine.text() == "":
            self.courseLine.setStyleSheet("background-color: #2A95F9;")
            self.courseLine.setFocus()

            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setText("Course name cannot be empty")
            self.msg.setWindowTitle("Warning")
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg.exec_()

        else:
            self.courseLine.setStyleSheet("background-color: white;")
            course.save_to_db()
            self.new_course_added(course)
            QMessageBox.information(
                self, "Success", "Course Added")
            self.close()
            

    def on_cancel_button_clicked(self):
        self.close()

    def on_text_changed(self):
        if self.courseLine.text() == "":
            self.courseLine.setStyleSheet("background-color: white;")
        else:
            self.courseLine.setStyleSheet("background-color: white;")

    def on_return_pressed(self):
        if self.courseLine.text() == "":
            self.courseLine.setStyleSheet("background-color: white;")
        else:
            self.courseLine.setStyleSheet("background-color: white;")
            self.close()
