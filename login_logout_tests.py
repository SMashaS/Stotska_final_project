import time
from models.register_post_model import RegisterPostModel
from models.signin_post_model import SigninPostModel
import requests
from driver import Driver
from pages.login_page import LoginPage
from pages.garage_page import GaragePage
from pages.register_page import RegisterPage


class TestLoginLogout:
    def setup_class(self):
        self.driver = Driver.get_chrome_driver()
        self.login_page = LoginPage()
        self.garage_page = GaragePage()
        self.register_page = RegisterPage()
        self.session = requests.session()
        register_user_data = RegisterPostModel("Vasyl", "Fedorchuk", "fedorchuck_vasyl@gmail.com",
                                               "Vasyl1997V", "Vasyl1997V")
        self.session.post("https://qauto.forstudy.space/api/auth/signup", json=register_user_data.__dict__)

    def setup_method(self):
        self.driver.get("https://guest:welcome2qauto@qauto.forstudy.space/")

    def test_check_login_window(self):
        self.login_page.get_sign_in_button().click()
        assert self.login_page.get_email_field().is_displayed()

    def test_check_login_page_close_button(self):
        self.login_page.get_sign_in_button().click()
        time.sleep(3)
        self.login_page.get_close_button().click()
        assert self.login_page.get_sign_in_button().is_displayed()

    def test_check_login_button_is_enabled(self):
        self.login_page.get_sign_in_button().click()
        assert not self.login_page.get_login_button().is_enabled()

    def test_check_successful_login_with_unchecked_remember_me_button(self):
        self.login_page.get_sign_in_button().click()
        self.login_page.get_email_field().fill_field('fedorchuck_vasyl@gmail.com')
        self.login_page.get_password_field().fill_field('Vasyl1997V')
        assert not self.login_page.get_remember_me_checkbox().is_checked()
        self.login_page.get_login_button().click()
        assert self.garage_page.get_my_profile_button().is_displayed()
        self.garage_page.get_my_profile_button().click()
        self.garage_page.get_logout_button().click()

    def test_check_successful_login_with_checked_remember_me_checkbox(self):
        self.login_page.get_sign_in_button().click()
        self.login_page.get_email_field().fill_field('fedorchuck_vasyl@gmail.com')
        self.login_page.get_password_field().fill_field('Vasyl1997V')
        self.login_page.get_remember_me_checkbox().check()
        assert self.login_page.get_remember_me_checkbox().is_checked()
        self.login_page.get_login_button().click()
        assert self.garage_page.get_successful_login_alert().is_displayed()
        self.garage_page.get_my_profile_button().click()
        self.garage_page.get_logout_button().click()

    def test_check_login_with_not_registered_user(self):
        self.login_page.get_sign_in_button().click()
        self.login_page.get_email_field().fill_field('fadorchuck_vasyl@gmail.com')
        self.login_page.get_password_field().fill_field('Vasyl1993V')
        self.login_page.get_login_button().click()
        assert self.login_page.get_wrong_email_or_password_alert().is_displayed()

    def test_check_password_is_required(self):
        self.login_page.get_sign_in_button().click()
        self.login_page.get_password_field().click()
        self.login_page.get_email_field().click()
        assert self.login_page.get_password_required_alert().is_displayed()

    def test_check_email_is_required(self):
        self.login_page.get_sign_in_button().click()
        self.login_page.get_email_field().click()
        self.login_page.get_password_field().click()
        assert self.login_page.get_email_required_alert().is_displayed()

    def test_check_email_incorrect_data(self):
        self.login_page.get_sign_in_button().click()
        self.login_page.get_email_field().fill_field('@@hm.co')
        self.login_page.get_password_field().click()
        assert self.login_page.get_email_not_valid_data_alert().is_displayed()
        self.login_page.get_email_field().clean_field()
        self.login_page.get_email_field().fill_field(' test@test.com')
        assert self.login_page.get_email_not_valid_data_alert().is_displayed()
        self.login_page.get_email_field().clean_field()
        self.login_page.get_email_field().fill_field('test@test.com ')
        assert self.login_page.get_email_not_valid_data_alert().is_displayed()
        self.login_page.get_email_field().clean_field()
        self.login_page.get_email_field().fill_field('invalid.email@domain')
        assert self.login_page.get_email_not_valid_data_alert().is_displayed()
        self.login_page.get_email_field().clean_field()
        self.login_page.get_email_field().fill_field('invalidgmail.com')
        assert self.login_page.get_email_not_valid_data_alert().is_displayed()
        self.login_page.get_email_field().clean_field()
        self.login_page.get_email_field().fill_field('inv alid@gmail.com')
        assert self.login_page.get_email_not_valid_data_alert().is_displayed()
        self.login_page.get_email_field().clean_field()
        self.login_page.get_email_field().fill_field('@example.com')
        assert self.login_page.get_email_not_valid_data_alert().is_displayed()
        self.login_page.get_email_field().clean_field()
        self.login_page.get_email_field().fill_field('user@')
        assert self.login_page.get_email_not_valid_data_alert().is_displayed()
        self.login_page.get_email_field().clean_field()
        self.login_page.get_email_field().fill_field('user@.com')
        assert self.login_page.get_email_not_valid_data_alert().is_displayed()
        self.login_page.get_email_field().clean_field()
        self.login_page.get_email_field().fill_field('user@example..com')
        assert self.login_page.get_email_not_valid_data_alert().is_displayed()

    def test_user_logout(self):
        self.login_page.get_sign_in_button().click()
        self.login_page.get_email_field().fill_field('fedorchuck_vasyl@gmail.com')
        self.login_page.get_password_field().fill_field('Vasyl1997V')
        self.login_page.get_login_button().click()
        self.garage_page.get_my_profile_button().click()
        self.garage_page.get_logout_button().click()
        assert self.login_page.get_sign_in_button().is_displayed()

    def test_user_logout_via_side_menu(self):
        self.login_page.get_sign_in_button().click()
        self.login_page.get_email_field().fill_field('fedorchuck_vasyl@gmail.com')
        self.login_page.get_password_field().fill_field('Vasyl1997V')
        self.login_page.get_login_button().click()
        self.garage_page.get_my_profile_button().click()
        self.garage_page.get_logout_button_side_menu().click()
        assert self.login_page.get_sign_in_button().is_displayed()

    def teardown_method(self):
        pass

    def teardown_class(self):
        self.session.delete("https://qauto.forstudy.space/api/users")

# pytest -v login_logout_tests.py