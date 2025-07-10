import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage

@allure.title("Личный кабинет")
def test_personal_account(driver, user):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    login_page = LoginPage(driver)
    login_page.login(user["email"], user["password"])

    profile_page = ProfilePage(driver)
    profile_page.go_to_profile()

    # Ожидание загрузки страницы профиля
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//a[text()='История заказов']"))
    )

    profile_page.go_to_order_history()
    profile_page.logout()