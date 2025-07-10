from selenium.webdriver.common.by import By

class OrderFeedLocators:
    ORDER_ITEM = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]")
    MODAL_ORDER = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")
    TOTAL_ORDERS = (By.XPATH, "//p[text()='Выполнено за всё время:']/following-sibling::p")
    TODAY_ORDERS = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    ORDER_IN_WORK = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li")