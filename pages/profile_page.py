from pages.base_page import BasePage
from locators.profile_locators import ProfileLocators

class ProfilePage(BasePage):
    def go_to_profile(self):
        self.click(ProfileLocators.PROFILE_LINK)

    def go_to_order_history(self):
        assert self.is_visible(ProfileLocators.ORDER_HISTORY_LINK), "История заказов не найдена"
        self.click(ProfileLocators.ORDER_HISTORY_LINK)

    def logout(self):
        self.click(ProfileLocators.LOGOUT_BUTTON)