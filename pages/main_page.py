from pages.base_page import BasePage
from locators.main_locators import MainLocators

class MainPage(BasePage):
    def click_constructor(self):
        self.click(MainLocators.CONSTRUCTOR_TAB)

    def click_feed(self):
        self.click(MainLocators.FEED_TAB)

    def click_ingredient(self):
        assert self.is_visible(MainLocators.INGREDIENT_ITEM), "Ингредиент не найден"
        self.click(MainLocators.INGREDIENT_ITEM)

    def close_modal(self):
        self.click(MainLocators.MODAL_CLOSE_BUTTON)

    def get_counter_value(self):
        return self.find_element(MainLocators.COUNTER).text

    def click_order_button(self):
        self.click(MainLocators.ORDER_BUTTON)