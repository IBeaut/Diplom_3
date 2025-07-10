from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators

class OrderFeedPage(BasePage):
    def click_order(self):
        assert self.is_visible(OrderFeedLocators.ORDER_ITEM), "Заказ не найден"
        self.click(OrderFeedLocators.ORDER_ITEM)

    def is_modal_open(self):
        return self.is_visible(OrderFeedLocators.MODAL_ORDER)

    def get_total_orders(self):
        return self.find_element(OrderFeedLocators.TOTAL_ORDERS).text

    def get_today_orders(self):
        return self.find_element(OrderFeedLocators.TODAY_ORDERS).text

    def get_order_in_work(self):
        return self.find_element(OrderFeedLocators.ORDER_IN_WORK).text