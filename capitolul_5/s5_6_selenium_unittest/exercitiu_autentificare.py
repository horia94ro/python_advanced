import unittest
import time
from selenium import webdriver


class Exercitiu(unittest.TestCase):

    def setUp(self) -> None:
        self.chrome = None
        self.chrome = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        self.chrome.maximize_window()
        # Definim credențialele la în setUP, în caz că vom mai avea nevoie de ele
        self.email = ""
        self.password = ""

    def test_autentificare(self):
        EXPECTED_TITLE = "Panoul Principal | Telecom Academy"
        self.chrome.get("https://cursuri.telacad.ro/login")
        time.sleep(3)
        # Realizăm identificarea celor două câmpuri pe bază de ID
        email_field = self.chrome.find_element_by_id("login-email")
        password_field = self.chrome.find_element_by_id("login-password")

        # Identificarea butonului de Sign In am extras-o direct din Chrome cu Copy->Copy XPath
        sign_in_button = self.chrome.find_element_by_xpath('//*[@id="login"]/button')

        email_field.send_keys(self.email)
        password_field.send_keys(self.password)
        sign_in_button.click()
        time.sleep(3)
        ACTUAL_TITLE = self.chrome.title
        self.assertIn(ACTUAL_TITLE, EXPECTED_TITLE, "Titlul paginii dupa autentificare este gresit.")

    def tearDown(self) -> None:
        if self.chrome: self.chrome.quit()
