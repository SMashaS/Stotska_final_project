from models.register_post_model import RegisterPostModel
from models.signin_post_model import SigninPostModel
import pytest
import requests


class TestApiChecks:
    sign_in_data = SigninPostModel("fedorchuck_alexa@gmail.com", "Alexa1997A", "False")

    def setup_class(self):
        self.session = requests.session()
        register_user_data = RegisterPostModel("Alex", "Fedorchuk", "fedorchuck_alexa@gmail.com",
                                               "Alexa1997A", "Alexa1997A")
        self.session.post("https://qauto.forstudy.space/api/auth/signup", json=register_user_data.__dict__)

    def setup_method(self):
        self.session.post("https://qauto.forstudy.space/api/auth/signin", json=TestApiChecks.sign_in_data.__dict__)

    def test_check_successful_registration_api(self):
        self.session.delete("https://qauto.forstudy.space/api/users")
        data_for_register_user = RegisterPostModel("Alexa", "Fedorchuk", "fedorchuck_alexa@gmail.com",
                                               "Alexa1997A", "Alexa1997A")
        registered_user = self.session.post("https://qauto.forstudy.space/api/auth/signup",
                                            json=data_for_register_user.__dict__)
        assert registered_user.json()["status"] == "ok"
        self.session.post("https://qauto.forstudy.space/api/auth/signin", json=TestApiChecks.sign_in_data.__dict__)

    def test_check_registration_with_registered_user(self):
        self.session.get("https://qauto2.forstudy.space/api/auth/logout")
        data_for_register_user = RegisterPostModel("Alexa", "Fedorchuk", "fedorchuck_alexa@gmail.com",
                                               "Alexa1997A", "Alexa1997A")
        registered_user = self.session.post("https://qauto.forstudy.space/api/auth/signup",
                                            json=data_for_register_user.__dict__)
        assert registered_user.json()["status"] == "error"
        assert registered_user.json()["message"] == "User already exists"
        self.session.post("https://qauto.forstudy.space/api/auth/signin", json=TestApiChecks.sign_in_data.__dict__)


    def test_check_registration_with_no_full_data(self):
        self.session.get("https://qauto2.forstudy.space/api/auth/logout")
        try:
            data_for_register_user = RegisterPostModel(name="Alexa", email="lex_fedorchuck@gmail.com",
                                                       password="Alexa1997A", repeat_password="Alexa1997A")
            self.session.post("https://qauto.forstudy.space/api/auth/signup", json=data_for_register_user.__dict__)
            assert False
        except TypeError:
            assert True
        self.session.post("https://qauto.forstudy.space/api/auth/signin", json=TestApiChecks.sign_in_data.__dict__)

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
        self.session.get("https://qauto2.forstudy.space/api/auth/logout")
        data_for_register_user = RegisterPostModel(name, last_name, email, password, repeat_password)
        registered_user = self.session.post("https://qauto.forstudy.space/api/auth/signup",
                                            json=data_for_register_user.__dict__)
        assert registered_user.json()['status'] == 'error'
        assert registered_user.json()["message"] == expected_message
        self.session.post("https://qauto.forstudy.space/api/auth/signin", json=TestApiChecks.sign_in_data.__dict__)

    def teardown_method(self):
        self.session.get("https://qauto2.forstudy.space/api/auth/logout")

    def teardown_class(self):
        self.session.post("https://qauto.forstudy.space/api/auth/signin", json=TestApiChecks.sign_in_data.__dict__)
        self.session.delete("https://qauto.forstudy.space/api/users")

# pytest -v api_tests.py