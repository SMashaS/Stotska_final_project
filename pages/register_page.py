from selenium.webdriver.common.by import By
from .base_page_with_driver import BasePageWithDriver
from controls.button import Button
from controls.label import Label
from controls.textbox import TextBox


class RegisterPage(BasePageWithDriver):
    def __init__(self):
        super().__init__()
        self._registration_button = None
        self._name_field = None
        self._last_name_field = None
        self._email_field = None
        self._password_field = None
        self._repeat_password_field = None
        self._register_button = None
        self._close_button = None
        self._name_required_alert = None
        self._last_name_required_alert = None
        self._email_required_alert = None
        self._password_required_alert = None
        self._repeat_password_required_alert = None
        self._name_not_valid_data_alert = None
        self._last_name_not_valid_data_alert = None
        self._email_not_valid_data_alert = None
        self._password_repeat_password_not_valid_data_alert = None
        self._user_exists_alert = None

    def get_registration_button(self):
        self._registration_button = Button(self._driver.find_element(By.XPATH, "//button[text()='Registration']"))
        return self._registration_button

    def get_name_field(self):
        self._name_field = TextBox(self._driver.find_element(By.ID, "signupName"))
        return self._name_field

    def get_last_name_field(self):
        self._last_name_field = TextBox(self._driver.find_element(By.ID, "signupLastName"))
        return self._last_name_field

    def get_email_field(self):
        self._email_field = TextBox(self._driver.find_element(By.ID, "signupEmail"))
        return self._email_field

    def get_password_field(self):
        self._password_field = TextBox(self._driver.find_element(By.ID, "signupPassword"))
        return self._password_field

    def get_repeat_password_field(self):
        self._repeat_password_field = TextBox(self._driver.find_element(By.ID, "signupRepeatPassword"))
        return self._repeat_password_field

    def get_register_button(self):
        self._register_button = Button(self._driver.find_element(By.XPATH, "//button[text()='Register']"))
        return self._register_button

    def get_close_button(self):
        self._close_button = Button(self._driver.find_element(By.XPATH, "//button[@aria-label='Close']"))
        return self._close_button

    def get_name_required_alert(self):
        self._name_required_alert = Label(self._driver.find_element(By.XPATH, "//p[text()='Name required']"))
        return self._name_required_alert

    def get_last_name_required_alert(self):
        self._last_name_required_alert = Label(self._driver.find_element(By.XPATH, "//p[text()='Last name required']"))
        return self._last_name_required_alert

    def get_email_required_alert(self):
        self._email_required_alert = Label(self._driver.find_element(By.XPATH, "//p[text()='Email required']"))
        return self._email_required_alert

    def get_password_required_alert(self):
        self._password_required_alert = Label(self._driver.find_element(By.XPATH, "//p[text()='Password required']"))
        return self._password_required_alert

    def get_repeat_password_required_alert(self):
        self._repeat_password_required_alert = Label(self._driver.find_element(By.XPATH, "Re-enter password required"))
        return self._repeat_password_required_alert

    def get_name_not_valid_data_alert(self):
        self._name_not_valid_data_alert = Label(self._driver.find_element(
            By.XPATH, "//p[text()='Name has to be from 2 to 20 characters long']"))
        return self._name_not_valid_data_alert

    def get_last_name_not_valid_data_alert(self):
        self._last_name_not_valid_data_alert = Label(self._driver.find_element(
            By.XPATH, "//p[text()='Last name has to be from 2 to 20 characters long']"))
        return self._last_name_not_valid_data_alert

    def get_email_not_valid_data_alert(self):
        self._email_not_valid_data_alert = Label(self._driver.find_element(By.XPATH, "//p[text()='Email is \n"
                                                                                     "incorrect']"))
        return self._email_not_valid_data_alert

    def get_password_repeat_password_not_valid_data_alert(self):
        self._password_repeat_password_not_valid_data_alert = Label(self._driver.find_element(
            By.XPATH, "//p[text()='Password has to be from 8 to 15 characters long and contain at least one integer, \n"
                      "one capital, and one small letter']"))
        return self._password_repeat_password_not_valid_data_alert

    def get_user_exists_alert(self):
        self._user_exists_alert = Label(self._driver.find_element(By.XPATH, "//p[text()='User already exists']"))
        return self._user_exists_alert
