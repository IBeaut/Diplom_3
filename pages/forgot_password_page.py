from pages.base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators

class ForgotPasswordPage(BasePage):
    def restore_password(self, email):
        self.send_keys(ForgotPasswordLocators.EMAIL_INPUT, email)
        self.click(ForgotPasswordLocators.RESTORE_BUTTON)

    def click_show_password(self):
        self.click(ForgotPasswordLocators.SHOW_PASSWORD_BUTTON)

    def is_password_field_active(self):
        return self.is_visible(ForgotPasswordLocators.ACTIVE_PASSWORD_FIELD)