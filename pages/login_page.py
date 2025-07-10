from pages.base_page import BasePage
from locators.login_locators import LoginLocators

class LoginPage(BasePage):
    def login(self, email, password):
        self.send_keys(LoginLocators.EMAIL_INPUT, email)
        self.send_keys(LoginLocators.PASSWORD_INPUT, password)
        self.click(LoginLocators.LOGIN_BUTTON)