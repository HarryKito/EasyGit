# GitPython
import git
from git import Repo

import sys
import os
import time

import graphics
if __name__ =="__main__":
    Repo.clone_from("https://github.com/HarryKito/ky-algorithm-class-b.git", "TEST" , recursive=True )
    app = graphics.MainPage(sys.argv)
    ex = graphics.run_mainPage()
    sys.exit(app.exec_())