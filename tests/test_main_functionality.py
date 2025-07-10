import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.main_page import MainPage

@allure.title("Основной функционал")
def test_main_functionality(driver, user):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    login_page = LoginPage(driver)
    login_page.login(user["email"], user["password"])

    main_page = MainPage(driver)

    # Ожидание загрузки главной страницы
    WebDriverWait(driver, 10).until(
        EC.url_contains("/")
    )

    # Переход в конструктор (если не на главной)
    main_page.click_constructor()

    # Клик по ингредиенту
    main_page.click_ingredient()

    # Ожидание модального окна
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]"))
    )

    main_page.close_modal()

    # Ожидание закрытия модального окна
    WebDriverWait(driver, 10).until_not(
        EC.visibility_of_element_located((By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]"))
    )

    # Переход в ленту заказов
    main_page.click_feed()

    # Ожидание загрузки ленты
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'OrderFeed_orderFeed')]"))
    )