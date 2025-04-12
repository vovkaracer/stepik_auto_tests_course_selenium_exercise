from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    SHOPPING_CART = (By.CLASS_NAME, "btn-add-to-basket")
    BOOKNAME_IN_SUCCESSFUL_ADD_TO_SHOPPING_CART_MESSAGE = (By.CSS_SELECTOR, "#messages strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_IN_SUCCESSFUL_ADD_TO_SHOPPING_CART_MESSAGE = (By.CSS_SELECTOR, "#messages p strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK_IN_HEADER = (By.CSS_SELECTOR, ".basket-mini .btn-group .btn-default")
    
class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    TEXT_BASKET_EMPTY = (By.CSS_SELECTOR, ".content #content_inner p")