from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import pytest

def test_guest_can_add_product_to_shopping_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_shopping_cart()
    page.solve_quiz_and_get_code()

def test_guest_should_see_successful_add_to_shopping_cart_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_shopping_cart()
    page.solve_quiz_and_get_code()
    page.should_be_successful_add_to_shopping_cart_message()

def test_guest_should_see_correct_product_name_in_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_shopping_cart()
    page.solve_quiz_and_get_code()
    page.should_be_correct_product_name_in_message()

def test_guest_should_see_correct_price_in_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_shopping_cart()
    page.solve_quiz_and_get_code()
    page.should_be_correct_price_in_message()

@pytest.mark.xfail(reason="It is negative test. Guest should see success message after adding product to basket")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_shopping_cart()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="It is negative test. Guest should not see success message before add product to basket")
def test_guest_can_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_successful_add_to_shopping_cart_message()

@pytest.mark.xfail(reason="It is negative test. Message shouldn`t disappear after adding product to basket")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_shopping_cart()
    page.solve_quiz_and_get_code()
    page.should_disappear_of_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_link_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()