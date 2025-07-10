import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage

@allure.title("Лента заказов")
def test_order_feed(driver, user):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    login_page = LoginPage(driver)
    login_page.login(user["email"], user["password"])

    # Переход в ленту заказов
    driver.get("https://stellarburgers.nomoreparties.site/feed")

    # Ожидание загрузки ленты
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'OrderFeed_orderFeed')]"))
    )

    order_feed_page = OrderFeedPage(driver)
    order_feed_page.click_order()

    # Ожидание модального окна
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]"))
    )