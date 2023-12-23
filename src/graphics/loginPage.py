from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5 import uic

ui = uic.loadUiType("bin/loginPage.ui")[0]

class loginPage(QMainWindow, ui):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def initUI(self):
        self.setWindowIcon(QIcon('img/github.png'))
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)