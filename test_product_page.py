from .pages.product_page import ProductPage

def test_guest_can_add_product_to_shopping_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_shopping_cart()
    page.solve_quiz_and_get_code()

def test_guest_should_see_successful_add_to_shopping_cart_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_shopping_cart()
    page.solve_quiz_and_get_code()
    page.should_be_successful_add_to_shopping_cart_message()

def test_guest_should_see_correct_product_name_in_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_shopping_cart()
    page.solve_quiz_and_get_code()
    page.should_be_correct_product_name_in_message()

def test_guest_should_see_correct_price_in_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_shopping_cart()
    page.solve_quiz_and_get_code()
    page.should_be_correct_price_in_message()
