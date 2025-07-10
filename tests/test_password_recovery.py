import allure
from pages.forgot_password_page import ForgotPasswordPage

@allure.title("Восстановление пароля")
def test_password_recovery(driver):
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    page = ForgotPasswordPage(driver)
    page.restore_password("test@example.com")
    page.click_show_password()
    assert page.is_password_field_active()