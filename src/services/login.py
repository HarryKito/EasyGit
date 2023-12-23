# login.py
# TODO: LoginService for use git
#

from git import Repo
import easygit
import os

class LoginService(easygit.easygit):
    def __init__(self):
        print("loginService initialized")

    def user_name(self) -> str:
        reader = Repo(search_parent_directories=True).config_reader()
        field = reader.get_value("user", "name")
        return field

    def user_email(self) -> str:
        reader = Repo(search_parent_directories=True).config_reader()
        field = reader.get_value("user", "email")
        return field

    def user_password(self) -> str:
        reader = Repo(search_parent_directories=True).config_reader()
        field = reader.get_value("user", "password")
        return field

    def ready_for_git(self) -> bool:
        return ( bool(self.user_name()) and bool(self.user_email()) )

    def ready_for_remote(self) -> bool:
        return ( self.ready_for_git() and bool(self.user_password()) )

    def getbrench(self) -> str:
        reader = Repo().config_reader()
        field = reader.get_value("init", "defaultBranch")
        return field

    def getremote(self,url:str) -> Repo:
        if not self.ready_for_remote():
            print("not ready for remote")

    def setremote(self, url:str):
        if not self.ready_for_remote():
            print("not ready for remote")

if __name__ == "__main__":
    print("login service test")
    login = LoginService() # login service class
    print(login)
    _easygit = easygit.easygit()
    _easygit.initgit("test")