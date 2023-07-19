from models.register_post_model import RegisterPostModel
from models.signin_post_model import SigninPostModel
import pytest
import requests
from driver import Driver


class TestApiChecks:
    def setup_class(self):
        self.driver = Driver.get_chrome_driver()
        self.session = requests.session()
        register_user_data = RegisterPostModel("Egor", "Fedorchuk", "fedorchuck_egor@gmail.com",
                                               "Egor1997E", "Egor1997E")
        self.session.post("https://qauto.forstudy.space/api/auth/signup", json=register_user_data.__dict__)

    def setup_method(self):
        self.driver.get("https://guest:welcome2qauto@qauto.forstudy.space/")

    def test_check_successful_registration_api(self):
        self.session.delete("https://qauto.forstudy.space/api/users")
        data_for_register_user = RegisterPostModel("Egor", "Fedorchuk", "fedorchuck_egor@gmail.com",
                                               "Egor1997E", "Egor1997E")
        registered_user = self.session.post("https://qauto.forstudy.space/api/auth/signup",
                                            json=data_for_register_user.__dict__)
        assert registered_user.json()["status"] == "ok"

    def test_check_registration_with_registered_user(self):
        data_for_register_user = RegisterPostModel("Egor", "Fedorchuk", "fedorchuck_egor@gmail.com",
                                                   "Egor1997E", "Egor1997E")
        registered_user = self.session.post("https://qauto.forstudy.space/api/auth/signup",
                                            json=data_for_register_user.__dict__)
        assert registered_user.json()["status"] == "error"
        assert registered_user.json()["message"] == "User already exists"

    def test_check_registration_with_no_full_data(self):
        try:
            data_for_register_user = RegisterPostModel(name="Ivan", email="ivan_fedorchuck@gmail.com",
                                                       password="Ivan1997I", repeat_password="Ivan1997I")
            self.session.post("https://qauto.forstudy.space/api/auth/signup", json=data_for_register_user.__dict__)
            assert False
        except TypeError:
            assert True

    @pytest.mark.parametrize("name, last_name, email, password, repeat_password, expected_message", [
        ("E", "Fedorchuk", "fedorchuck_egor@gmail.com", "Egor1997E", "Egor1997E",
         "Name has to be from 2 to 20 characters long"),
        ("Egor", "F@", "fedorchuck_egor@gmail.com", "Egor1997E", "Egor1997E", "Last Name is invalid"),
        ("Egor", "Fedorchuck", "@gmail.com", "Egor1997E", "Egor1997E", "Email is incorrect"),
        ("Egor", "Fedorchuck", "fedorchuck_egor@gmail.com", "EgorEgor", "EgorEgor",
         "Password has to be from 8 to 15 characters long and contain at least one integer, one capital, and one small letter"),
        ("Egor", "Fedorchuck", "fedorchuck_egor@gmail.com", "Egor1997E", "Egor1997EE", "Passwords do not match")
    ])
    def test_registration_with_incorrect_data(self, name, last_name, email, password, repeat_password,
                                              expected_message):
        data_for_register_user = RegisterPostModel(name, last_name, email, password, repeat_password)
        registered_user = self.session.post("https://qauto.forstudy.space/api/auth/signup",
                                            json=data_for_register_user.__dict__)
        assert registered_user.json()['status'] == 'error'
        assert registered_user.json()["message"] == expected_message

    def teardown_method(self):
        pass

    def teardown_class(self):
        self.session.delete("https://qauto.forstudy.space/api/users")

# pytest -v api_tests.py