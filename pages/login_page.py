from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    LOGIN_PANEL = (By.XPATH, "//h5[text()='Login']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_login_page_displayed(self):
        return self.is_visible(self.LOGIN_PANEL)

    def login(self, username, password):
        self.do_send_keys(self.USERNAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
