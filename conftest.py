import pytest
from selenium import webdriver

from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser():
    user_language = "en"
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

