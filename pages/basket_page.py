from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "basket is not empty"

    def should_be_text_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_BASKET_EMPTY), "text basket empty does not present"