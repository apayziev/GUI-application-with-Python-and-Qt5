import traceback
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from new_course_window import NewCourseWindow
try:
    from courses_model import Courses
except ImportError:
    traceback.print_exc()


class AllCoursesWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.row_count = 0
        self.initUI()

        self.selectedCourse = None

    def initUI(self):
        self.setWindowTitle("All Courses")
        self.setGeometry(30, 120, 500, 450)
        self.setWindowIcon(QIcon("images/icon.png"))
        self.setFixedSize(self.size())

        # tableWidget
        self.table = QTableWidget(self)
        self.table.setGeometry(QRect(30, 30, 300, 400))
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)

        self.table.setColumnCount(2)
        self.table.setRowCount(0)
        self.table.setHorizontalHeaderLabels(
            ["ID", "Course name"])
        self.table.setColumnWidth(0, 10)
        self.table.setColumnWidth(1, 150)

        # allCourseSaveButton
        self.allCourseSaveButton = QPushButton("Add", self)
        self.allCourseSaveButton.setGeometry(QRect(350, 30, 90, 40))
        self.allCourseSaveButton.setFont(QFont("Arial", 12))
        self.allCourseSaveButton.clicked.connect(
            self.on_allCourseSaveButton_clicked)

        # allCourseUpdateButton
        self.allCourseUpdateButton = QPushButton("Update", self)
        self.allCourseUpdateButton.setGeometry(QRect(350, 80, 90, 40))
        self.allCourseUpdateButton.setFont(QFont("Arial", 12))
        self.allCourseUpdateButton.clicked.connect(
            self.on_allCourseUpdateButton_clicked)

        # allCourseDeleteButton
        self.allCourseDeleteButton = QPushButton("Delete", self)
        self.allCourseDeleteButton.setGeometry(QRect(350, 130, 90, 40))
        self.allCourseDeleteButton.setFont(QFont("Arial", 12))
        self.allCourseDeleteButton.clicked.connect(
            self.on_allCourseDeleteButton_clicked)

        # allCourseRefreshButton
        self.allCourseRefreshButton = QPushButton("Refresh", self)
        self.allCourseRefreshButton.setGeometry(QRect(350, 180, 90, 40))
        self.allCourseRefreshButton.setFont(QFont("Arial", 12))
        self.allCourseRefreshButton.clicked.connect(
            self.on_allCourseRefreshButton_clicked)

        self.table.hideColumn(0)
        self.setWindowModality(Qt.ApplicationModal)

        for course in Courses.objects():
            self.table.setRowCount(self.row_count + 1)
            self.table.setItem(self.row_count, 0,
                               QTableWidgetItem(str(course.id)))
            self.table.setItem(self.row_count, 1,
                               QTableWidgetItem(str(course.name)))
            self.row_count += 1

        self.table.resizeColumnsToContents()
        self.table.clicked.connect(self.onClickCourse)

    def on_allCourseSaveButton_clicked(self):
        self.new_course_window = NewCourseWindow(self.new_course_added)
        self.new_course_window.setGeometry(QRect(550, 120, 400, 200))
        self.new_course_window.show()

    def new_course_added(self, course):
        self.table.setRowCount(self.row_count + 1)
        self.table.setItem(self.row_count, 0,
                           QTableWidgetItem(str(course.id)))
        self.table.setItem(self.row_count, 1,
                           QTableWidgetItem(str(course.name)))
        self.row_count += 1

    def on_allCourseUpdateButton_clicked(self):
        self.new_course_window = NewCourseWindow(self.new_course_added)
        self.new_course_window.setGeometry(QRect(550, 120, 400, 200))
        self.new_course_window.show()

        if self.selectedCourse is not None:
            self.selectedCourse.name = self.courseLine.text()
            print(self.selectedCourse.name)
            self.table.setItem(self.selectedRow, 1, QTableWidgetItem(
                str(self.courseLine.text())))
            self.selectedCourse.save_to_db()

    def on_allCourseDeleteButton_clicked(self):
        if self.selectedCourse is not None:
            self.selectedCourse.delete_data()
            self.table.removeRow(self.selectedRow)
            self.table.setRowCount(self.row_count - 1)
            self.row_count -= 1

    def on_allCourseRefreshButton_clicked(self):
        self.table.setRowCount(0)
        self.row_count = 0

        for course in Courses.objects():
            self.table.setRowCount(self.row_count + 1)
            self.table.setItem(self.row_count, 0,
                               QTableWidgetItem(str(course.id)))
            self.table.setItem(self.row_count, 1,
                               QTableWidgetItem(str(course.name)))
            self.row_count += 1

    def onClickCourse(self):
        self.selectedRow = self.table.currentRow()        
        self.selectedCourse = Courses(self.table.item(self.selectedRow, 1).text(),
                                      self.table.item(self.selectedRow, 0).text())
