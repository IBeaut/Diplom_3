from selenium.webdriver.common.by import By

class MainLocators:
    CONSTRUCTOR_TAB = (By.XPATH, "//p[text()='Конструктор']")
    FEED_TAB = (By.XPATH, "//p[text()='Лента Заказов']")
    INGREDIENT_ITEM = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button")
    COUNTER = (By.XPATH, "//p[contains(@class, 'counter')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")