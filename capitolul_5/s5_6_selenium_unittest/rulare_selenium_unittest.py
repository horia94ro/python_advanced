import unittest
import time
from selenium import webdriver


class CursuriTelacad(unittest.TestCase):

    def setUp(self) -> None:
        self.chrome = None
        self.chrome = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        self.chrome.maximize_window()

    def test_login_page(self):
        EXPECTED_TITLE = "Sign in or Register | Telecom Academy"
        self.chrome.get("https://cursuri.telacad.ro/login")
        time.sleep(3)
        ACTUAL_TITLE = self.chrome.title
        self.assertIn(ACTUAL_TITLE, EXPECTED_TITLE, "Titlul paginii de login este gresit.")

    def test_courses_page(self):
        EXPECTED_TITLE = "Courses | Telecom Academy"
        self.chrome.get("https://cursuri.telacad.ro/courses")
        time.sleep(3)
        ACTUAL_TITLE = self.chrome.title
        self.assertIn(ACTUAL_TITLE, EXPECTED_TITLE, "Titlul paginii de cursuri este gresit.")

    def test_after_login_title(self):
        pass



    def tearDown(self) -> None:
        if self.chrome: self.chrome.quit()