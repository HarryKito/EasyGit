# GitPython
import git
from git import Repo

import os
import time
import sys

from graphics import mainPage
from PyQt5.QtWidgets import QApplication

if __name__ =="__main__":
    # Repo.clone_from("https://github.com/HarryKito/ky-algorithm-class-b.git", "TEST" , recursive=True )
    app = QApplication(sys.argv)
    ex = mainPage.MainPage()
    sys.exit(app.exec_())