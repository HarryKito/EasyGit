from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon

class login(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('EasyGit login')
        self.setWindowIcon(QIcon('img/github.png'))
        self.setGeometry(300, 300, 300, 200)
        self.show()