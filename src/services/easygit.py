# easygit.py
# TODO: easygit is a main git controls
#
from git import Repo
import os

class easygit:
    def __init__(self):
        print("easygit initialized")

    def initgit(self, dir: str = None ):
        if dir is None:
            dir = os.getcwd()
        else:
            dir = os.path.join(os.getcwd(), dir)
        reader = Repo.init(dir)
        print(reader)

    def addgit(self, path: str):
        repo = Repo()