from selenium.webdriver.common.by import By
from .base_page_with_driver import BasePageWithDriver
from controls.button import Button


class GaragePage(BasePageWithDriver):
    def __init__(self):
        super().__init__()
        self._my_profile_button = None

    def get_my_profile_button(self):
        self._my_profile_button = Button(self._driver.find_element(By.ID, "userNavDropdown"))
        return self._my_profile_button
