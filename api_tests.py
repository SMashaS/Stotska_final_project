from models.register_post_model import RegisterPostModel
from models.signin_post_model import SigninPostModel
import pytest
import requests
from driver import Driver


class TestApiChecks:
    def setup_class(self):
        self.driver = Driver.get_chrome_driver()
        self.session = requests.session()
        register_user_data = RegisterPostModel("Vasyl", "Fedorchuk", "fedorchuck_vasyl@gmail.com",
                                               "Vasyl1997V", "Vasyl1997V")
        self.session.post("https://qauto.forstudy.space/api/auth/signup", json=register_user_data.__dict__)

    def setup_method(self):
        self.driver.get("https://guest:welcome2qauto@qauto.forstudy.space/")

    def test_check_successful_registration_api(self):
        self.session.delete("https://qauto.forstudy.space/api/users")

        data_for_register_user = RegisterPostModel("Vasyl", "Fedorchuk", "fedorchuck_vasyl@gmail.com",
                                               "Vasyl1997V", "Vasyl1997V")
        registered_user = self.session.post("https://qauto.forstudy.space/api/auth/signup",
                                            json=data_for_register_user.__dict__)
        assert registered_user.json()["status"] == "ok"

    def test_check_registration_with_registered_user(self):
        data_for_register_user = RegisterPostModel("Vasyl", "Fedorchuk", "fedorchuck_vasyl@gmail.com",
                                                   "Vasyl1997V", "Vasyl1997V")
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
        ("V", "Fedorchuk", "fedorchuck_vasyl@gmail.com", "Vasyl1997V", "Vasyl1997V",
         "Name has to be from 2 to 20 characters long"),
        ("Vasyl", "F@", "fedorchuck_vasyl@gmail.com", "Vasyl1997V", "Vasyl1997V", "Last Name is invalid"),
        ("Vasyl", "Fedorchuck", "@gmail.com", "Vasyl1997V", "Vasyl1997V", "Email is incorrect"),
        ("Vasyl", "Fedorchuck", "fedorchuck_vasyl@gmail.com", "VasylVasyl", "VasylVasyl",
         "Password has to be from 8 to 15 characters long and contain at least one integer, one capital, and one small letter"),
        ("Vasyl", "Fedorchuck", "fedorchuck_vasyl@gmail.com", "Vasyl1997V", "Vas1997VV", "Passwords do not match")
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