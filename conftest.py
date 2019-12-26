import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose language ru, en, etc...")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        print("Browser <browser_name> still is not implented")
    yield browser
    print("\nquit browser..")
    browser.quit()

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "login_user: mark test to run only on mark 'login_user'"
        )

    config.addinivalue_line(
        "markers", "login_guest: mark test to run only on mark 'login_guest'"
        )

    config.addinivalue_line(
        "markers", "need_review: mark test to run only on mark 'need_review'"
        )