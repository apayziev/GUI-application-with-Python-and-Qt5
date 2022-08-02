from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from new_student_window import NewStudentWindow
from students_model import AllStudents
from courses_model import Courses
import sys


class AllStudentsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.row_count = 0
        self.selectedStudent = None

    def initUI(self):
        self.setWindowTitle("All students")
        self.setWindowIcon(QIcon("images/icon.png"))
        self.setGeometry(50, 110, 1250, 800)
        self.setFixedSize(self.size())

        # filterComboBox
        self.filterComboBox = QComboBox(self)
        self.filterComboBox.setGeometry(30, 10, 200, 30)
        self.filterComboBox.setFont(QFont("Arial", 12))
        self.filterComboBox.addItems(
            ["Choose one", "Surname", "Name", "Course"])
        self.filterComboBox.setCurrentIndex(0)

        # filter button
        self.filterButton = QPushButton("Filter", self)
        self.filterButton.setGeometry(250, 10, 100, 30)
        self.filterButton.setFont(QFont("Arial", 12))
        self.filterButton.setStyleSheet(
            "background-color: ; color: white;")
        self.filterButton.clicked.connect(self.on_filter_button_clicked)

        # searchComboBox
        self.searchComboBox = QComboBox(self)
        self.searchComboBox.setGeometry(30, 480, 200, 30)
        self.searchComboBox.setFont(QFont("Arial", 12))
        self.searchComboBox.addItems(
            ["Choose one", "Surname", "Name", "PassportNo"])
        self.searchComboBox.setCurrentIndex(0)

        # searchLine
        self.searchLine = QLineEdit(self)
        self.searchLine.setGeometry(250, 480, 200, 30)
        self.searchLine.setFont(QFont("Arial", 12))
        self.searchLine.setPlaceholderText("Type here")

        # searchButton
        self.searchButton = QPushButton("Search", self)
        self.searchButton.setGeometry(470, 480, 100, 30)
        self.searchButton.setFont(QFont("Arial", 12))
        self.searchButton.clicked.connect(self.on_search_button_clicked)

        # addButton
        self.addButton = QPushButton("Add", self)
        self.addButton.setGeometry(1070, 60, 100, 40)
        self.addButton.setFont(QFont("Arial", 12))
        self.addButton.clicked.connect(self.on_add_button_clicked)

        # updateButton
        self.updateButton = QPushButton("Update", self)
        self.updateButton.setGeometry(1070, 110, 100, 40)
        self.updateButton.setFont(QFont("Arial", 12))
        self.updateButton.clicked.connect(self.on_update_button_clicked)

        # deleteButton
        self.deleteButton = QPushButton("Delete", self)
        self.deleteButton.setGeometry(1070, 160, 100, 40)
        self.deleteButton.setFont(QFont("Arial", 12))
        self.deleteButton.clicked.connect(self.on_delete_button_clicked)

        # refreshButton
        self.refreshButton = QPushButton("Refresh", self)
        self.refreshButton.setGeometry(1070, 210, 100, 40)
        self.refreshButton.setFont(QFont("Arial", 12))
        self.refreshButton.clicked.connect(self.on_refresh_button_clicked)

        # tableWidget
        self.table = QTableWidget(self)
        # setrowcolor black
        self.table.setAlternatingRowColors(True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        # setHorizontalItems font-weight: bold
        self.table.horizontalHeader().setFont(
            QFont("Arial", 10, QFont.Bold))
        # set setHorizontalHeaderLabels background-color: lightgray
        self.table.horizontalHeader().setStyleSheet(
            "QHeaderView::section {background-color: lightgray}")
        self.table.verticalHeader().setStyleSheet(
            "QHeaderView::section {background-color: lightgray}")

        # make table scrollable
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table.setShowGrid(True)

        self.table.setCornerButtonEnabled(True)
        self.table.setStyleSheet("QTableView::item { border: 1px solid black }"
                                 "QTableView::item:color{color: black}"
                                 "QTableView::item:hover { border: 1px solid red }"
                                 "QTableView::item:selected { border: 1px solid red }"
                                 "QTableView::item:selected:active { border: 1px solid blue }"
                                 "QTableView::item:selected:!active:focus { border: 1px solid red }"
                                 "QTableView::item:selected:focus { border: 1px solid red }"
                                 "QTableView::item:selected:hover { border: 1px solid red }"
                                 )

        self.table.setGeometry(QRect(30, 60, 1000, 400))

        self.table.setColumnCount(8)
        self.table.setRowCount(0)
        self.table.setHorizontalHeaderLabels(
            ["ID", "Surname", "Name", "Address", "Dob", "Marital Status", "PassportNo", "Course"])
        self.table.setColumnWidth(0, 10)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 150)
        self.table.setColumnWidth(4, 150)
        self.table.setColumnWidth(5, 100)
        self.table.setColumnWidth(6, 150)
        self.table.setColumnWidth(7, 100)

        # hide ID column
        self.table.setColumnHidden(0, True)

        for student in AllStudents.objects():
            row_count = self.table.rowCount()
            self.table.setRowCount(row_count + 1)
            self.table.setItem(row_count, 0, QTableWidgetItem(str(student.id)))
            self.table.setItem(row_count, 1, QTableWidgetItem(student.surname))
            self.table.setItem(row_count, 2, QTableWidgetItem(student.name))
            self.table.setItem(row_count, 3, QTableWidgetItem(student.address))
            self.table.setItem(row_count, 4, QTableWidgetItem(student.dob))
            self.table.setItem(
                row_count, 5, QTableWidgetItem(student.marital_status))
            self.table.setItem(
                row_count, 6, QTableWidgetItem(student.passport))

            course = Courses.get_by_id(id=student.courseID)
            self.table.setItem(row_count, 7, QTableWidgetItem(course.name))

        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.resizeColumnsToContents()

        self.table.clicked.connect(self.onClickStudent)

        self.setWindowModality(Qt.ApplicationModal)

    def new_student_added(self, student):
        row_count = self.table.rowCount()
        self.table.setRowCount(row_count + 1)
        self.table.setItem(row_count, 0, QTableWidgetItem(str(student.id)))
        self.table.setItem(row_count, 1, QTableWidgetItem(student.surname))
        self.table.setItem(row_count, 2, QTableWidgetItem(student.name))
        self.table.setItem(row_count, 3, QTableWidgetItem(student.address))
        self.table.setItem(row_count, 4, QTableWidgetItem(student.dob))
        self.table.setItem(
            row_count, 5, QTableWidgetItem(student.marital_status))
        self.table.setItem(
            row_count, 6, QTableWidgetItem(student.passport))

        course = Courses.get_by_id(id=student.courseID)
        self.table.setItem(row_count, 7, QTableWidgetItem(course.name))

    def on_add_button_clicked(self):
        self.newStudentWindow = NewStudentWindow(self.new_student_added)
        self.newStudentWindow.show()
        self.setGeometry(550, 100, 1250, 800)

    def on_update_button_clicked(self):
        pass

    def on_delete_button_clicked(self):
        if self.selectedStudent is not None:
            self.selectedStudent.delete_student()
            self.table.removeRow(self.selectedRow)
            self.table.setRowCount(self.row_count - 1)
            self.row_count -= 1

    def on_refresh_button_clicked(self):
        self.table.setRowCount(0)
        self.row_count = 0
        for student in AllStudents.objects():
            row_count = self.table.rowCount()
            self.table.setRowCount(row_count + 1)
            self.table.setItem(row_count, 0, QTableWidgetItem(str(student.id)))
            self.table.setItem(row_count, 1, QTableWidgetItem(student.surname))
            self.table.setItem(row_count, 2, QTableWidgetItem(student.name))
            self.table.setItem(row_count, 3, QTableWidgetItem(student.address))
            self.table.setItem(row_count, 4, QTableWidgetItem(student.dob))
            self.table.setItem(
                row_count, 5, QTableWidgetItem(student.marital_status))
            self.table.setItem(
                row_count, 6, QTableWidgetItem(student.passport))

            course = Courses.get_by_id(id=student.courseID)
            self.table.setItem(row_count, 7, QTableWidgetItem(course.name))

    def on_filter_button_clicked(self):
        selected = self.filterComboBox.currentText()
        # sort by selected
        if selected == "Surname":
            self.table.sortItems(1)
        elif selected == "Name":
            self.table.sortItems(2)
        elif selected == "Choose one":
            pass

    def on_search_button_clicked(self):
        # Epty the table
        self.table.setRowCount(0)
        self.row_count = 0
        # Get the search text
        selected = self.searchComboBox.currentText()
        search_text = str(self.searchLine.text())
        for student in AllStudents.objects():
            if selected == "Surname":
                if student.surname == search_text.title():
                    row_count = self.table.rowCount()
                    self.table.setRowCount(row_count + 1)
                    self.table.setItem(
                        row_count, 0, QTableWidgetItem(str(student.id)))
                    self.table.setItem(
                        row_count, 1, QTableWidgetItem(student.surname))
                    self.table.setItem(
                        row_count, 2, QTableWidgetItem(student.name))
                    self.table.setItem(
                        row_count, 3, QTableWidgetItem(student.address))
                    self.table.setItem(
                        row_count, 4, QTableWidgetItem(student.dob))
                    self.table.setItem(
                        row_count, 5, QTableWidgetItem(student.marital_status))
                    self.table.setItem(
                        row_count, 6, QTableWidgetItem(student.passport))

                    course = Courses.get_by_id(id=student.courseID)
                    self.table.setItem(
                        row_count, 7, QTableWidgetItem(course.name))

            elif selected == "Name":
                if student.name == search_text.title():
                    row_count = self.table.rowCount()
                    self.table.setRowCount(row_count + 1)
                    self.table.setItem(
                        row_count, 0, QTableWidgetItem(str(student.id)))
                    self.table.setItem(
                        row_count, 1, QTableWidgetItem(student.surname))
                    self.table.setItem(
                        row_count, 2, QTableWidgetItem(student.name))
                    self.table.setItem(
                        row_count, 3, QTableWidgetItem(student.address))
                    self.table.setItem(
                        row_count, 4, QTableWidgetItem(student.dob))
                    self.table.setItem(
                        row_count, 5, QTableWidgetItem(student.marital_status))
                    self.table.setItem(
                        row_count, 6, QTableWidgetItem(student.passport))

                    course = Courses.get_by_id(id=student.courseID)
                    self.table.setItem(
                        row_count, 7, QTableWidgetItem(course.name))

            elif selected == "PassportNo":
                if student.passport == search_text.upper():
                    row_count = self.table.rowCount()
                    self.table.setRowCount(row_count + 1)
                    self.table.setItem(
                        row_count, 0, QTableWidgetItem(str(student.id)))
                    self.table.setItem(
                        row_count, 1, QTableWidgetItem(student.surname))
                    self.table.setItem(
                        row_count, 2, QTableWidgetItem(student.name))
                    self.table.setItem(
                        row_count, 3, QTableWidgetItem(student.address))
                    self.table.setItem(
                        row_count, 4, QTableWidgetItem(student.dob))
                    self.table.setItem(
                        row_count, 5, QTableWidgetItem(student.marital_status))
                    self.table.setItem(
                        row_count, 6, QTableWidgetItem(student.passport))

                    course = Courses.get_by_id(id=student.courseID)
                    self.table.setItem(
                        row_count, 7, QTableWidgetItem(course.name))
            
    def onClickStudent(self):
        self.selectedRow = self.table.currentRow()
        self.selectedStudent = AllStudents(id=self.table.item(self.selectedRow, 0).text(),
                                           surname=self.table.item(
                                               self.selectedRow, 1).text(),
                                           name=self.table.item(
                                               self.selectedRow, 2).text(),
                                           address=self.table.item(
                                               self.selectedRow, 3).text(),
                                           dob=self.table.item(
                                               self.selectedRow, 4).text(),
                                           marital_status=self.table.item(
                                               self.selectedRow, 5).text(),
                                           passport=self.table.item(
                                               self.selectedRow, 6).text(),
                                           courseID=int(Courses.get_course_id(self.table.item(self.selectedRow, 7).text())))
