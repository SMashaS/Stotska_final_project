import time
import pytest
from models.register_post_model import RegisterPostModel
from models.signin_post_model import SigninPostModel
import requests
from driver import Driver
from pages.login_page import LoginPage
from pages.garage_page import GaragePage
from pages.register_page import RegisterPage
from pages.settings_page import SettingsPage


class TestRegistration:
    def setup_class(self):
        self.driver = Driver.get_chrome_driver()
        self.login_page = LoginPage()
        self.garage_page = GaragePage()
        self.register_page = RegisterPage()
        self.settings_page = SettingsPage()
        self.session = requests.session()

    def setup_method(self):
        self.driver.get("https://guest:welcome2qauto@qauto.forstudy.space/")

    def test_check_registration_window(self):
        self.login_page.get_sign_in_button().click()
        self.register_page.get_registration_button().click()
        assert self.register_page.get_name_field().is_displayed()

    def test_check_register_button_is_enabled(self):
        self.login_page.get_sign_in_button().click()
        self.register_page.get_registration_button().click()
        self.register_page.get_name_field().fill_field('M')
        self.register_page.get_last_name_field().fill_field('Fedorchuk')
        self.register_page.get_email_field().fill_field('fedorchuck_maryna@gmail.com')
        self.register_page.get_password_field().fill_field('Maryna1997M')
        self.register_page.get_repeat_password_field().fill_field('Maryna1997M')
        assert not self.register_page.get_register_button().is_enabled()

    def test_check_name_is_required(self):
        self.login_page.get_sign_in_button().click()
        self.register_page.get_registration_button().click()
        self.register_page.get_name_field().click()
        self.register_page.get_last_name_field().click()
        assert self.register_page.get_name_required_alert().is_displayed()

    def test_check_last_name_is_required(self):
        self.login_page.get_sign_in_button().click()
        self.register_page.get_registration_button().click()
        self.register_page.get_last_name_field().click()
        self.register_page.get_name_field().click()
        assert self.register_page.get_last_name_required_alert().is_displayed()

    def test_check_email_is_required(self):
        self.login_page.get_sign_in_button().click()
        self.register_page.get_registration_button().click()
        self.register_page.get_email_field().click()
        self.register_page.get_name_field().click()
        assert self.register_page.get_email_required_alert().is_displayed()

    @pytest.mark.parametrize("email_address", [
        '@@hm.co',
        ' test@test.com',
        'test@test.com ',
        'invalid.email@domain',
        'invalidgmail.com',
        'inv alid@gmail.com',
        '@example.com',
        'user@',
        'user@.com',
        'user@example..com'
    ])
    def test_check_email_incorrect(self, email_address):
        self.login_page.get_sign_in_button().click()
        self.register_page.get_registration_button().click()
        self.register_page.get_email_field().fill_field(email_address)
        self.register_page.get_name_field().click()
        assert self.register_page.get_email_not_valid_data_alert().is_displayed()

    def test_check_password_is_required(self):
        self.login_page.get_sign_in_button().click()
        self.register_page.get_registration_button().click()
        self.register_page.get_password_field().click()
        self.register_page.get_name_field().click()
        assert self.register_page.get_password_required_alert().is_displayed()

    def test_check_repeat_password_is_required(self):
        self.login_page.get_sign_in_button().click()
        self.register_page.get_registration_button().click()
        self.register_page.get_repeat_password_field().click()
        self.register_page.get_name_field().click()
        assert self.register_page.get_repeat_password_required_alert().is_displayed()

    @pytest.mark.parametrize("name", [
        'A',
        'abcabcabcabcabcabcabc'
    ])
    def test_check_name_field_length(self, name):
        self.login_page.get_sign_in_button().click()
        self.register_page.get_registration_button().click()
        self.register_page.get_name_field().fill_field(name)
        self.register_page.get_last_name_field().click()
        assert self.register_page.get_name_not_valid_length_alert().is_displayed()

    @pytest.mark.parametrize("last_name", [
        'A',
        'abcabcabcabcabcabcabc'
    ])
    def test_check_last_name_field_length(self, last_name):
        self.login_page.get_sign_in_button().click()
        self.register_page.get_registration_button().click()
        self.register_page.get_last_name_field().fill_field(last_name)
        self.register_page.get_name_field().click()
        assert self.register_page.get_last_name_not_valid_length_alert().is_displayed()

    @pytest.mark.parametrize("name", [
        '@@',
        '##',
        '!!',
        '$$',
        '**',
        '::',
        '()',
        '  ',
        '..',
        ',,',
        '??',
        '--',
        '45'
    ])
    def test_check_name_not_valid_data(self, name):
        self.login_page.get_sign_in_button().click()
        self.register_page.get_registration_button().click()
        self.register_page.get_name_field().fill_field(name)
        self.register_page.get_last_name_field().click()
        assert self.register_page.get_name_not_valid_data_alert().is_displayed()

    @pytest.mark.parametrize("last_name", [
        '@@',
        '##',
        '!!',
        '$$',
        '**',
        '::',
        '()',
        '  ',
        '..',
        ',,',
        '??',
        '--',
        '45'
    ])
    def test_check_last_name_not_valid_data(self, last_name):
        self.login_page.get_sign_in_button().click()
        self.register_page.get_registration_button().click()
        self.register_page.get_last_name_field().fill_field(last_name)
        self.register_page.get_name_field().click()
        assert self.register_page.get_last_name_not_valid_data_alert().is_displayed()

    def test_check_name_field_length_and_not_valid_data(self):
        self.login_page.get_sign_in_button().click()
        self.register_page.get_registration_button().click()
        self.register_page.get_name_field().fill_field('@')
        self.register_page.get_last_name_field().click()
        assert self.register_page.get_name_not_valid_length_alert().is_displayed() \
               and self.register_page.get_name_not_valid_data_alert().is_displayed()

    def test_check_last_name_field_length_and_not_valid_data(self):
        self.login_page.get_sign_in_button().click()
        self.register_page.get_registration_button().click()
        self.register_page.get_last_name_field().fill_field('@')
        self.register_page.get_name_field().click()
        assert self.register_page.get_last_name_not_valid_length_alert().is_displayed() \
               and self.register_page.get_last_name_not_valid_data_alert().is_displayed()

    @pytest.mark.parametrize("password", [
        'password',
        'PASSWORD',
        '12345678',
        'PASSWOR8',
        'passwor8',
        'PASSWORd',
        'PASSWORD123456ppp',
        '@#$%^&*()*'
    ])
    def test_check_incorrect_password_field(self, password):
        self.login_page.get_sign_in_button().click()
        self.register_page.get_registration_button().click()
        self.register_page.get_password_field().fill_field(password)
        self.register_page.get_name_field().click()
        assert self.register_page.get_password_repeat_password_not_valid_data_alert().is_displayed()

    @pytest.mark.parametrize("repeat_password", [
        'password',
        'PASSWORD',
        '12345678',
        'PASSWOR8',
        'passwor8',
        'PASSWORd',
        'PASSWORD123456ppp',
        '@#$%^&*()*'
    ])
    def test_check_incorrect_repeat_password_field(self, repeat_password):
        self.login_page.get_sign_in_button().click()
        self.register_page.get_registration_button().click()
        self.register_page.get_repeat_password_field().fill_field(repeat_password)
        self.register_page.get_name_field().click()
        assert self.register_page.get_password_repeat_password_not_valid_data_alert().is_displayed()

    def test_check_passwords_do_not_match(self):
        self.login_page.get_sign_in_button().click()
        self.register_page.get_registration_button().click()
        self.register_page.get_password_field().fill_field('passwo2P')
        self.register_page.get_repeat_password_field().fill_field('passwo2PA')
        self.register_page.get_name_field().click()
        assert self.register_page.get_passwords_do_not_match_alert().is_displayed()

    def test_check_register_page_close_button(self):
        self.login_page.get_sign_in_button().click()
        self.register_page.get_registration_button().click()
        time.sleep(5)
        self.register_page.get_close_button().click()
        assert self.login_page.get_sign_in_button().is_displayed()

    def test_check_user_exists(self):
        register_user_data = RegisterPostModel("Maryna", "Fedorchuk", "fedorchuck_maryna@gmail.com",
                                               "Maryna1997M", "Maryna1997M")
        self.session.post("https://qauto.forstudy.space/api/auth/signup", json=register_user_data.__dict__)
        self.session.get("https://qauto.forstudy.space/api/auth/logout")
        self.login_page.get_sign_in_button().click()
        self.register_page.get_registration_button().click()
        self.register_page.get_name_field().fill_field('Maryna')
        self.register_page.get_last_name_field().fill_field('Fedorchuk')
        self.register_page.get_email_field().fill_field('fedorchuck_maryna@gmail.com')
        self.register_page.get_password_field().fill_field('Maryna1997M')
        self.register_page.get_repeat_password_field().fill_field('Maryna1997M')
        self.register_page.get_register_button().click()
        assert self.register_page.get_user_exists_alert().is_displayed()
        sign_in_data = SigninPostModel("fedorchuck_maryna@gmail.com", "Maryna1997M", "False")
        self.session.post("https://qauto.forstudy.space/api/auth/signin", json=sign_in_data.__dict__)
        self.session.delete("https://qauto.forstudy.space/api/users")

    def test_check_successful_registration(self):
        self.login_page.get_sign_in_button().click()
        self.register_page.get_registration_button().click()
        self.register_page.get_name_field().fill_field('Maryna')
        self.register_page.get_last_name_field().fill_field('Fedorchuk')
        self.register_page.get_email_field().fill_field('fedorchuck_maryna@gmail.com')
        self.register_page.get_password_field().fill_field('Maryna1997M')
        self.register_page.get_repeat_password_field().fill_field('Maryna1997M')
        self.register_page.get_register_button().click()
        assert self.garage_page.get_my_profile_button().is_displayed()
        time.sleep(5)
        self.settings_page.get_settings_side_menu_button().click()
        self.settings_page.get_remove_my_account_button().click()
        self.settings_page.get_remove_my_account_window_remove_button().click()

    def teardown_method(self):
        pass

    def teardown_class(self):
        pass

# pytest -v registration_tests.py
