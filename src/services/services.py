import unittest
from login import *
from easygit import *
class LoginTestCase(unittest.TestCase):
    _login = LoginService()
    def test_init_git(self):
        self._login.initgit()
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
