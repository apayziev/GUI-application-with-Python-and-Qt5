from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys



class HelpWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()
        self.center()

    def initUI(self):
        self.setWindowTitle("Help")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon("images/about.png"))
        self.QLabel = QLabel(self)
        self.QLabel.setText("<h1>This is demo page</h1>")
        self.QLabel.setGeometry(QRect(0, 0, 800, 600))
        self.QLabel.setAlignment(Qt.AlignCenter)
        self.QLabel.setStyleSheet(
            "QLabel {font-size: 20px; font-weight: bold;}")
        self.QLabel.setObjectName("QLabel")
        self.setFixedSize(800, 600)
        
        self.setWindowModality(Qt.ApplicationModal)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
