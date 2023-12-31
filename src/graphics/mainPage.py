from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5 import uic

ui = uic.loadUiType("bin/mainPage.ui")[0]
class MainPage(QMainWindow, ui):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def initUI(self):
        self.setWindowTitle('EasyGit')
        self.setWindowIcon(QIcon('img/github.png'))
        self.setGeometry(300, 300, 300, 200)
        self.show()