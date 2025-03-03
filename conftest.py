from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help='Choose language')

@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    link = f'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser = webdriver.Chrome(options=options)
    browser.get(link)
    yield browser
    print('\nquit browser')
    browser.quit()