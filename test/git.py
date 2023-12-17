import os
from git import Repo

def make_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
