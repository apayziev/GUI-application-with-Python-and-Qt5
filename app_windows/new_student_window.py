from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from students_model import AllStudents
from courses_model import Courses
import sys


class NewStudentWindow(QWidget):
    def __init__(self, new_student_added):
        super().__init__()
        self.initUI()

        self.new_student_added = new_student_added

    def initUI(self):
        self.setWindowTitle("New Student")
        self.setGeometry(100, 100, 400, 500)
        self.setWindowIcon(QIcon("images/icon.png"))
        self.setFixedSize(self.size())

        # surnameLabel
        self.surnameLabel = QLabel("Surname: ", self)
        self.surnameLabel.setGeometry(40, 20, 100, 30)
        self.surnameLabel.setFont(QFont("Arial", 12))
        self.surnameLabel.setStyleSheet("color: Black; font-weight: bold;")

        # surnameLine
        self.surnameLine = QLineEdit(self)
        self.surnameLine.setGeometry(140, 20, 200, 30)
        self.surnameLine.setFont(QFont("Arial", 12))
        self.surnameLine.setStyleSheet("background-color: white;")
        self.surnameLine.setFocus()
        self.surnameLine.setPlaceholderText("Surname")
        self.surnameLine.setMaxLength(100)
        self.surnameLine.setEchoMode(QLineEdit.Normal)
        self.surnameLine.setClearButtonEnabled(True)
      

        # nameLabel
        self.nameLabel = QLabel("Name: ", self)
        self.nameLabel.setGeometry(40, 60, 100, 30)
        self.nameLabel.setFont(QFont("Arial", 12))
        self.nameLabel.setStyleSheet("color: Black; font-weight: bold;")

        # nameLine
        self.nameLine = QLineEdit(self)
        self.nameLine.setGeometry(140, 60, 200, 30)
        self.nameLine.setFont(QFont("Arial", 12))
        self.nameLine.setStyleSheet("background-color: white;")
        self.nameLine.setPlaceholderText("Name")
        self.nameLine.setMaxLength(50)
        self.nameLine.setEchoMode(QLineEdit.Normal)
        self.nameLine.setClearButtonEnabled(True)
   

        # addressLabel
        self.addressLabel = QLabel("Address: ", self)
        self.addressLabel.setGeometry(40, 100, 100, 30)
        self.addressLabel.setFont(QFont("Arial", 12))
        self.addressLabel.setStyleSheet("color: Black; font-weight: bold;")

        # addressLine
        self.addressLine = QLineEdit(self)
        self.addressLine.setGeometry(140, 100, 200, 30)
        self.addressLine.setFont(QFont("Arial", 12))
        self.addressLine.setStyleSheet("background-color: white;")
        self.addressLine.setPlaceholderText("Address")
        self.addressLine.setMaxLength(50)
        self.addressLine.setEchoMode(QLineEdit.Normal)
        self.addressLine.setClearButtonEnabled(True)
   

        # dobLabel
        self.dobLabel = QLabel("Dob: ", self)
        self.dobLabel.setStatusTip("Date of birth")
        self.dobLabel.setToolTip("Date of birth")
        self.dobLabel.setGeometry(40, 140, 100, 30)
        self.dobLabel.setFont(QFont("Arial", 12))
        self.dobLabel.setStyleSheet("color: Black; font-weight: bold;")

        # dobLine
        self.dobLine = QDateEdit(self)
        self.dobLine.setGeometry(140, 140, 200, 30)
        self.dobLine.setFont(QFont("Arial", 12))
        self.dobLine.setStyleSheet("background-color: white; color: black;")
        self.dobLine.setDisplayFormat("dd.MM.yyyy")
        self.dobLine.setCalendarPopup(True)
        self.dobLine.setDate(QDate.currentDate())

        # maritalStatusLabel
        self.maritalStatusLabel = QLabel("Marital\nStatus: ", self)
        self.maritalStatusLabel.setGeometry(40, 180, 100, 50)
        self.maritalStatusLabel.setFont(QFont("Arial", 12))
        self.maritalStatusLabel.setStyleSheet(
            "color: Black; font-weight: bold;")

        # maritalStatusComboBox
        self.maritalStatusComboBox = QComboBox(self)
        self.maritalStatusComboBox.setGeometry(140, 180, 200, 30)
        self.maritalStatusComboBox.setFont(QFont("Arial", 12))
        self.maritalStatusComboBox.setStyleSheet("background-color: white;")
        self.maritalStatusComboBox.addItems(["Single", "Married", "Divorced"])
        self.maritalStatusComboBox.addItem("Married")
        self.maritalStatusComboBox.setCurrentIndex(0)

        # passportNumberLabel
        self.passportNumberLabel = QLabel("Passport: ", self)
        self.passportNumberLabel.setGeometry(40, 230, 100, 30)
        self.passportNumberLabel.setFont(QFont("Arial", 12))
        self.passportNumberLabel.setStyleSheet(
            "color: Black; font-weight: bold;")

        # passportNumberLine
        self.passportNumberLine = QLineEdit(self)
        self.passportNumberLine.setGeometry(140, 225, 200, 30)
        self.passportNumberLine.setFont(QFont("Arial", 12))
        self.passportNumberLine.setStyleSheet("background-color: white;")
        self.passportNumberLine.setPlaceholderText("Passport Number")
        self.passportNumberLine.setMaxLength(10)
        self.passportNumberLine.setEchoMode(QLineEdit.Normal)
        self.passportNumberLine.setClearButtonEnabled(True)
        self.passportNumberLine.setValidator(
            QRegExpValidator(QRegExp("[A-Za-z0-9]{1,20}")))

        # courseLabel
        self.courseLabel = QLabel("Course: ", self)
        self.courseLabel.setGeometry(40, 270, 100, 30)
        self.courseLabel.setFont(QFont("Arial", 12))
        self.courseLabel.setStyleSheet("color: Black; font-weight: bold;")

        # courseLine
        self.courseLineComboBox = QComboBox(self)
        self.courseLineComboBox.setGeometry(140, 270, 200, 30)
        self.courseLineComboBox.setFont(QFont("Arial", 12))
        self.courseLineComboBox.setStyleSheet("background-color: white;")
        self.courseLineComboBox.addItems(Courses.getCourses())
        self.courseLineComboBox.setCurrentIndex(0)

        # saveButton
        self.saveButton = QPushButton("Save", self)
        self.saveButton.setDefault(True)
        self.saveButton.setGeometry(30, 350, 100, 40)
        self.saveButton.setFont(QFont("Arial", 12))
        self.saveButton.clicked.connect(self.on_save_button_clicked)

        # cancelButton
        self.cancelButton = QPushButton("Cancel", self)
        self.cancelButton.setGeometry(140, 350, 100, 40)
        self.cancelButton.setFont(QFont("Arial", 12))
        self.cancelButton.clicked.connect(self.on_cancel_button_clicked)

        # clearButton
        self.clearButton = QPushButton("Clear", self)
        self.clearButton.setGeometry(250, 350, 100, 40)
        self.clearButton.setFont(QFont("Arial", 12))
        self.clearButton.clicked.connect(self.on_clear_button_clicked)

        self.setWindowModality(Qt.ApplicationModal)

    def on_cancel_button_clicked(self):
        self.close()

    def on_clear_button_clicked(self):
        self.clearButton.clicked.connect(self.surnameLine.clear)
        self.clearButton.clicked.connect(self.nameLine.clear)
        self.clearButton.clicked.connect(self.addressLine.clear)
        self.clearButton.clicked.connect(self.passportNumberLine.clear)
        self.dobLine.setDate(QDate.currentDate())
        self.maritalStatusComboBox.setCurrentIndex(0)
        self.courseLineComboBox.setCurrentIndex(0)

    def surnameLineChecker(self):
        if self.surnameLine.text() == "":
            self.surnameLine.setStyleSheet("background-color: #2A95F9;")
            self.surnameLine.setFocus()
            QMessageBox.warning(
                self, "Error", "Surname can't be empty", QMessageBox.Ok)
        else:
            self.surnameLine.setStyleSheet("background-color: white;")
            return self.surnameLine.text()
            
    def nameLineChecker(self):
        if self.nameLine.text() == "":
            self.nameLine.setStyleSheet("background-color: #2A95F9;")
            self.nameLine.setFocus()
            QMessageBox.warning(
                self, "Error", "Name can't be empty", QMessageBox.Ok)
        else:
            self.nameLine.setStyleSheet("background-color: white;")
            return self.nameLine.text()

    def addressLineChecker(self):
        if self.addressLine.text() == "":
            self.addressLine.setStyleSheet("background-color: #2A95F9;")
            self.addressLine.setFocus()
            QMessageBox.warning(
                self, "Error", "Address can't be empty", QMessageBox.Ok)
        else:
            self.addressLine.setStyleSheet("background-color: white;")
            return self.addressLine.text()

    def passportNumberLineChecker(self):
        if self.passportNumberLine.text() == "":
            self.passportNumberLine.setStyleSheet("background-color: #2A95F9;")
            self.passportNumberLine.setFocus()
            QMessageBox.warning(
                self, "Error", "Passport Number can't be empty", QMessageBox.Ok)
        else:
            self.passportNumberLine.setStyleSheet("background-color: white;")
            return self.passportNumberLine.text()

    def on_save_button_clicked(self):
        try:
            student = AllStudents(str(self.surnameLineChecker()).title(), str(self.nameLineChecker()).title(), str(self.addressLineChecker()).title(), str(self.dobLine.text()), str(self.maritalStatusComboBox.currentText()), str(self.passportNumberLineChecker()).upper(),
                                      int(Courses.get_course_id(str(self.courseLineComboBox.currentText()))))
        except:
            QMessageBox.warning(
                self, "Error", "Please fill all the fields", QMessageBox.Ok)
        else:
            if self.surnameLine.text() != "" and self.nameLine.text() != "" and self.addressLine.text() != "" and self.passportNumberLine.text() != "":
                student.save_to_db()
                self.new_student_added(student)
                QMessageBox.information(
                    self, "Success", "Student added successfully", QMessageBox.Ok)
                self.close()
