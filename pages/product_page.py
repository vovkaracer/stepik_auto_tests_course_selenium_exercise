from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_shopping_cart(self):
        shopping_cart = self.browser.find_element(*ProductPageLocators.SHOPPING_CART)
        shopping_cart.click()

    def should_be_successful_add_to_shopping_cart_message(self):
        assert self.is_element_present(*ProductPageLocators.BOOKNAME_IN_SUCCESSFUL_ADD_TO_SHOPPING_CART_MESSAGE), "successful add to shopping cart message is not present"

    def should_be_correct_product_name_in_message(self):
        assert self.is_text_in_elements_equal(*ProductPageLocators.BOOKNAME_IN_SUCCESSFUL_ADD_TO_SHOPPING_CART_MESSAGE, *ProductPageLocators.BOOK_NAME), \
            "book name on page is not the same book name in message"

    def should_be_correct_price_in_message(self):
        assert self.is_text_in_elements_equal(*ProductPageLocators.PRICE_IN_SUCCESSFUL_ADD_TO_SHOPPING_CART_MESSAGE, *ProductPageLocators.BOOK_PRICE), \
            "price on page is not the same price in message"