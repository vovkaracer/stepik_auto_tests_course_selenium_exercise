from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
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