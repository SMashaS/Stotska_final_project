from selenium.webdriver.common.by import By
from .base_page_with_driver import BasePageWithDriver
from controls.button import Button
from controls.textbox import TextBox
from controls.label import Label


class LoginPage(BasePageWithDriver):
    def __init__(self):
        super().__init__()
        self._sign_in_button = None

    def get_sign_in_button(self):
        self._sign_in_button = Button(self._driver.find_element(By.XPATH, "//button[text()='Sign In']"))
        return self._sign_in_button