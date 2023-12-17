from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MainPage(QWidget):
    
    def __init__(self,argv):
        super().__init__()
        self.initUI()
        return QApplication(argv)

    def initUI(self):
        self.setWindowTitle('EasyGit')
        self.setWindowIcon(QIcon('img/github.png'))
        self.setGeometry(300, 300, 300, 200)
        self.show()

def run_mainPage():
    return MainPage()