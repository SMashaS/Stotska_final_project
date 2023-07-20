import time

import pytest
from models.register_post_model import RegisterPostModel
from models.signin_post_model import SigninPostModel
import requests
from driver import Driver
from pages.login_page import LoginPage
from pages.garage_page import GaragePage
from pages.settings_page import SettingsPage
from pages.register_page import RegisterPage


class TestsUserSettings:
    def setup_class(self):
        self.driver = Driver.get_chrome_driver()
        self.login_page = LoginPage()
        self.register_page = RegisterPage()
        self.garage_page = GaragePage()
        self.settings_page = SettingsPage()
        self.session = requests.session()
        register_user_data = RegisterPostModel("Artsem", "Fedorchuk", "fedorchuck_artsem@gmail.com",
                                               "Artsem1997N", "Artsem1997N")
        self.session.post("https://qauto.forstudy.space/api/auth/signup", json=register_user_data.__dict__)

    def setup_method(self):
        self.driver.get("https://guest:welcome2qauto@qauto.forstudy.space/")
        self.login_page.get_sign_in_button().click()
        self.login_page.get_email_field().fill_field("fedorchuck_artsem@gmail.com")
        self.login_page.get_password_field().fill_field("Artsem1997N")
        self.login_page.get_login_button().click()

    def test_settings_page_displayed(self):
        self.garage_page.get_my_profile_button().click()
        self.settings_page.get_settings_dropdown_menu_button().click()
        assert self.settings_page.get_usd_button().is_displayed()

    def test_settings_title_in_dropdown_is_not_enabled(self):
        self.garage_page.get_my_profile_button().click()
        self.settings_page.get_settings_dropdown_menu_button().click()
        self.garage_page.get_my_profile_button().click()
        assert not self.settings_page.get_settings_dropdown_menu_button().is_enabled()

    def test_settings_title_in_side_menu_is_active(self):
        button_settings_side_menu = self.settings_page.get_settings_side_menu_button()
        button_settings_side_menu.click()
        assert button_settings_side_menu.is_active()

    def test_default_currency_is_usd(self):
        self.settings_page.get_settings_side_menu_button().click()
        assert self.settings_page.get_usd_button().is_active()

    def test_default_units_of_distance_is_km(self):
        self.settings_page.get_settings_side_menu_button().click()
        assert self.settings_page.get_km_button().is_active()

    def test_change_currency_to_uah(self):
        self.garage_page.get_my_profile_button().click()
        self.settings_page.get_settings_dropdown_menu_button().click()
        uah_button = self.settings_page.get_uah_button()
        uah_button.click()
        assert self.settings_page.get_currency_changed_alert().is_displayed()
        time.sleep(2)
        assert uah_button.is_active()
        assert not uah_button.is_enabled()
        self.settings_page.get_usd_button().click()

    def test_change_currency_to_eur(self):
        self.garage_page.get_my_profile_button().click()
        self.settings_page.get_settings_dropdown_menu_button().click()
        eur_button = self.settings_page.get_eur_button()
        eur_button.click()
        assert self.settings_page.get_currency_changed_alert().is_displayed()
        time.sleep(2)
        assert eur_button.is_active()
        assert not eur_button.is_enabled()
        self.settings_page.get_usd_button().click()

    def test_change_currency_to_pln(self):
        self.garage_page.get_my_profile_button().click()
        self.settings_page.get_settings_dropdown_menu_button().click()
        pln_button = self.settings_page.get_pln_button()
        pln_button.click()
        assert self.settings_page.get_currency_changed_alert().is_displayed()
        time.sleep(2)
        assert pln_button.is_active()
        assert not pln_button.is_enabled()
        self.settings_page.get_usd_button().click()

    def test_change_currency_to_gbp(self):
        self.garage_page.get_my_profile_button().click()
        self.settings_page.get_settings_dropdown_menu_button().click()
        gbp_button = self.settings_page.get_gbp_button()
        gbp_button.click()
        assert self.settings_page.get_currency_changed_alert().is_displayed()
        time.sleep(2)
        assert gbp_button.is_active()
        assert not gbp_button.is_enabled()
        self.settings_page.get_usd_button().click()

    def test_change_currency_to_usd(self):
        self.settings_page.get_settings_side_menu_button().click()
        time.sleep(2)
        self.settings_page.get_uah_button().click()
        time.sleep(2)
        usd_button = self.settings_page.get_usd_button()
        usd_button.click()
        assert self.settings_page.get_currency_changed_alert().is_displayed()
        time.sleep(2)
        assert usd_button.is_active()
        assert not usd_button.is_enabled()

    def test_changed_currency_is_saved_after_logout(self):
        self.settings_page.get_settings_side_menu_button().click()
        time.sleep(2)
        changed_button = self.settings_page.get_eur_button()
        changed_button.click()
        assert self.settings_page.get_currency_changed_alert().is_displayed()
        self.garage_page.get_logout_button_side_menu().click()
        self.login_page.get_sign_in_button().click()
        self.login_page.get_email_field().fill_field("fedorchuck_artsem@gmail.com")
        self.login_page.get_password_field().fill_field("Artsem1997N")
        self.login_page.get_login_button().click()
        self.settings_page.get_settings_side_menu_button().click()
        changed_button = self.settings_page.get_eur_button()
        assert not changed_button.is_enabled()
        self.settings_page.get_usd_button().click()

    def test_change_units_of_distance_to_ml(self):
        self.garage_page.get_my_profile_button().click()
        self.settings_page.get_settings_dropdown_menu_button().click()
        ml_button = self.settings_page.get_ml_button()
        ml_button.click()
        assert self.settings_page.get_units_of_distance_changed_alert().is_displayed()
        time.sleep(2)
        assert ml_button.is_active()
        assert not ml_button.is_enabled()
        self.settings_page.get_km_button().click()

    def test_change_units_of_distance_to_km(self):
        self.garage_page.get_my_profile_button().click()
        self.settings_page.get_settings_dropdown_menu_button().click()
        self.settings_page.get_ml_button().click()
        km_button = self.settings_page.get_km_button()
        km_button.click()
        assert self.settings_page.get_units_of_distance_changed_alert().is_displayed()
        time.sleep(2)
        assert km_button.is_active()
        assert not km_button.is_enabled()

    def test_changed_units_of_distance_is_saved_after_logout(self):
        self.settings_page.get_settings_side_menu_button().click()
        time.sleep(2)
        changed_button = self.settings_page.get_ml_button()
        changed_button.click()
        assert self.settings_page.get_units_of_distance_changed_alert().is_displayed()
        self.garage_page.get_logout_button_side_menu().click()
        self.login_page.get_sign_in_button().click()
        self.login_page.get_email_field().fill_field("fedorchuck_artsem@gmail.com")
        self.login_page.get_password_field().fill_field("Artsem1997N")
        self.login_page.get_login_button().click()
        self.settings_page.get_settings_side_menu_button().click()
        changed_button = self.settings_page.get_ml_button()
        assert not changed_button.is_enabled()
        self.settings_page.get_km_button().click()

    def test_check_email_and_password_are_required_in_change_email(self):
        self.settings_page.get_settings_side_menu_button().click()
        self.settings_page.get_change_email_button().click()
        assert self.settings_page.get_email_required_alert().is_displayed()
        assert self.settings_page.get_password_required_alert().is_displayed()

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
    def test_check_email_is_incorrect(self, email_address):
        self.settings_page.get_settings_side_menu_button().click()
        self.settings_page.get_new_email_address_field().fill_field(email_address)
        self.settings_page.get_change_email_button().click()
        assert self.settings_page.get_email_is_incorrect_alert().is_displayed()

    def test_check_wrong_password(self):
        self.settings_page.get_settings_side_menu_button().click()
        self.settings_page.get_new_email_address_field().fill_field("fedorchuck_artem@gmail.com")
        self.settings_page.get_change_email_password_field().fill_field("Artsem1997")
        self.settings_page.get_change_email_button().click()
        assert self.settings_page.get_wrong_password_alert().is_displayed()

    def test_check_email_already_exists_in_change_email(self):
        self.garage_page.get_my_profile_button().click()
        self.garage_page.get_logout_button().click()
        self.login_page.get_sign_in_button().click()
        self.register_page.get_registration_button().click()
        self.register_page.get_name_field().fill_field('Kristina')
        self.register_page.get_last_name_field().fill_field('Fedorchuk')
        self.register_page.get_email_field().fill_field('fedorchuck_kristina@gmail.com')
        self.register_page.get_password_field().fill_field('Kristina1997K')
        self.register_page.get_repeat_password_field().fill_field('Kristina1997K')
        self.register_page.get_register_button().click()
        self.settings_page.get_settings_side_menu_button().click()
        self.settings_page.get_new_email_address_field().fill_field("fedorchuck_artsem@gmail.com")
        self.settings_page.get_change_email_password_field().fill_field("Kristina1997K")
        self.settings_page.get_change_email_button().click()
        time.sleep(2)
        assert self.settings_page.get_email_already_exists_alert().is_displayed()
        self.settings_page.get_remove_my_account_button().click()
        self.settings_page.get_remove_my_account_window_remove_button().click()
        self.login_page.get_sign_in_button().click()
        self.login_page.get_email_field().fill_field("fedorchuck_artsem@gmail.com")
        self.login_page.get_password_field().fill_field("Artsem1997N")
        self.login_page.get_login_button().click()

    def test_check_successful_change_email(self):
        self.settings_page.get_settings_side_menu_button().click()
        self.settings_page.get_new_email_address_field().fill_field("test_new_email@gmail.com")
        self.settings_page.get_change_email_password_field().fill_field("Artsem1997N")
        self.settings_page.get_change_email_button().click()
        time.sleep(1)
        assert self.settings_page.get_email_has_been_changed_alert().is_displayed()
        self.garage_page.get_my_profile_button().click()
        self.garage_page.get_logout_button().click()
        self.login_page.get_sign_in_button().click()
        self.login_page.get_email_field().fill_field("test_new_email@gmail.com")
        self.login_page.get_password_field().fill_field("Artsem1997N")
        self.login_page.get_login_button().click()
        assert self.garage_page.get_my_profile_button().is_displayed()
        self.settings_page.get_settings_side_menu_button().click()
        self.settings_page.get_new_email_address_field().fill_field("fedorchuck_artsem@gmail.com")
        self.settings_page.get_change_email_password_field().fill_field("Artsem1997N")
        self.settings_page.get_change_email_button().click()

    def test_check_login_with_old_email_after_changing_to_new_one(self):
        self.settings_page.get_settings_side_menu_button().click()
        self.settings_page.get_new_email_address_field().fill_field("test_new_email@gmail.com")
        self.settings_page.get_change_email_password_field().fill_field("Artsem1997N")
        self.settings_page.get_change_email_button().click()
        time.sleep(1)
        self.garage_page.get_my_profile_button().click()
        self.garage_page.get_logout_button().click()
        self.login_page.get_sign_in_button().click()
        self.login_page.get_email_field().fill_field("fedorchuck_artsem@gmail.com")
        self.login_page.get_password_field().fill_field("Artsem1997N")
        self.login_page.get_login_button().click()
        time.sleep(1)
        assert self.login_page.get_wrong_email_or_password_alert().is_displayed()
        self.login_page.get_email_field().clean_field()
        self.login_page.get_email_field().fill_field("test_new_email@gmail.com")
        self.login_page.get_password_field().clean_field()
        self.login_page.get_password_field().fill_field("Artsem1997N")
        self.login_page.get_login_button().click()
        self.garage_page.get_my_profile_button().click()
        self.settings_page.get_settings_dropdown_menu_button().click()
        self.settings_page.get_new_email_address_field().fill_field("fedorchuck_artsem@gmail.com")
        self.settings_page.get_change_email_password_field().fill_field("Artsem1997N")
        self.settings_page.get_change_email_button().click()

    def teardown_method(self):
        time.sleep(5)
        self.garage_page.get_logout_button_side_menu().click()

    def teardown_class(self):
        time.sleep(5)
        self.login_page.get_sign_in_button().click()
        self.login_page.get_email_field().fill_field("fedorchuck_artsem@gmail.com")
        self.login_page.get_password_field().fill_field("Artsem1997N")
        self.login_page.get_login_button().click()
        time.sleep(5)
        self.settings_page.get_settings_side_menu_button().click()
        self.settings_page.get_remove_my_account_button().click()
        self.settings_page.get_remove_my_account_window_remove_button().click()

# pytest -v user_settings_tests.py