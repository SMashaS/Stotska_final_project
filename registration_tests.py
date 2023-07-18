from models.register_post_model import RegisterPostModel
from models.signin_post_model import SigninPostModel
import requests
from driver import Driver
from pages.login_page import LoginPage
from pages.garage_page import GaragePage
from pages.register_page import RegisterPage


class TestAuthentication:
    def setup_class(self):
        self.driver = Driver.get_chrome_driver()
        self.login_page = LoginPage()
        self.garage_page = GaragePage()
        self.register_page = RegisterPage()
        self.session = requests.session()

    def setup_method(self):
        self.driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")

    def test_check_registration_window(self):
        self.login_page.get_sign_in_button().click()
        self.register_page.get_registration_button().click()
        assert self.register_page.get_name_field().is_displayed()

    def test_check_register_button_is_enabled(self):
        self.login_page.get_sign_in_button().click()
        self.register_page.get_registration_button().click()
        self.register_page.get_name_field().fill_field('V')
        self.register_page.get_last_name_field().fill_field('Fedorchuk')
        self.register_page.get_email_field().fill_field('fedorchuck_victor@gmail.com')
        self.register_page.get_password_field().fill_field('Victor1997V')
        self.register_page.get_repeat_password_field().fill_field('Victor1997V')
        assert not self.register_page.get_register_button().is_enabled()

    def test_check_name_is_required(self):
        self.login_page.get_sign_in_button().click()
        self.register_page.get_registration_button().click()
        self.register_page.get_name_field().click()
        self.register_page.get_last_name_field().click()
        assert self.register_page.get_name_required_alert().is_displayed()

    def test_check_name_short_length(self):
        self.login_page.get_sign_in_button().click()
        self.register_page.get_registration_button().click()
        self.register_page.get_name_field().fill_field('A')
        self.register_page.get_last_name_field().click()
        assert self.register_page.get_name_not_valid_length_alert().is_displayed()

    def test_check_name_long_length(self):
        self.login_page.get_sign_in_button().click()
        self.register_page.get_registration_button().click()
        self.register_page.get_name_field().fill_field('abcabcabcabcabcabcabc')
        self.register_page.get_last_name_field().click()
        assert self.register_page.get_name_not_valid_length_alert().is_displayed()

    def test_check_name_not_valid_data(self):
        self.login_page.get_sign_in_button().click()
        self.register_page.get_registration_button().click()
        self.register_page.get_name_field().fill_field('Mariia@')
        self.register_page.get_last_name_field().click()
        assert self.register_page.get_name_not_valid_data_alert().is_displayed()

    def test_check_successful_registration_api(self):
        data_for_register_user = RegisterPostModel("Victor", "Fedorchuk", "fedorchuck_victor@gmail.com", "Victor1997V", "Victor1997V")
        registered_user = self.session.post("https://qauto2.forstudy.space/api/auth/signup", json=data_for_register_user.__dict__)
        assert registered_user.json()["status"] == "ok"

    def test_check_register_page_close_button(self):
        self.login_page.get_sign_in_button().click()
        self.register_page.get_registration_button().click()
        self.register_page.get_close_button().click()
        assert self.login_page.get_sign_in_button().is_displayed()

    def test_check_user_exists(self):
        register_user_data = RegisterPostModel("Victor", "Fedorchuk", "fedorchuck_victor@gmail.com",
                                               "Victor1997V", "Victor1997V")
        self.session.post("https://qauto2.forstudy.space/api/auth/signup", json=register_user_data.__dict__)
        self.session.get("https://qauto2.forstudy.space/api/auth/logout")
        self.login_page.get_sign_in_button().click()
        self.register_page.get_registration_button().click()
        self.register_page.get_name_field().fill_field('Victor')
        self.register_page.get_last_name_field().fill_field('Fedorchuk')
        self.register_page.get_email_field().fill_field('fedorchuck_victor@gmail.com')
        self.register_page.get_password_field().fill_field('Victor1997V')
        self.register_page.get_repeat_password_field().fill_field('Victor1997V')
        self.register_page.get_register_button().click()
        assert self.register_page.get_user_exists_alert().is_displayed()
        sign_in_data = SigninPostModel("fedorchuck_victor@gmail.com", "Victor1997V", "False")
        self.session.post("https://qauto2.forstudy.space/api/auth/signin", json=sign_in_data.__dict__)
        self.session.delete("https://qauto2.forstudy.space/api/users")

    def test_check_successful_registration(self):
        self.login_page.get_sign_in_button().click()
        self.register_page.get_registration_button().click()
        self.register_page.get_name_field().fill_field('Victor')
        self.register_page.get_last_name_field().fill_field('Fedorchuk')
        self.register_page.get_email_field().fill_field('fedorchuck_victor@gmail.com')
        self.register_page.get_password_field().fill_field('Victor1997V')
        self.register_page.get_repeat_password_field().fill_field('Victor1997V')
        self.register_page.get_register_button().click()
        assert self.garage_page.get_my_profile_button().is_displayed()
        self.session.delete("https://qauto2.forstudy.space/api/users")
        self.session.get("https://qauto2.forstudy.space/api/auth/logout")


# pytest -v registration_tests.py
