import unittest
import os
from src.commands.pwd import PwdCommand as Pwd


class TestPwd(unittest.TestCase):
    def setUp(self):
        self.previous_dir = os.getcwd()

    def tearDown(self):
        os.chdir(self.previous_dir)

    def test_pwd(self):
        expected = os.getcwd()
        response = Pwd().execute({})
        self.assertEqual(response, expected)
