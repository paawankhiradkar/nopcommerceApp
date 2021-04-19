from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="chromedriver.exe")
        driver.implicitly_wait(5)
    elif browser == "firefox":
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
    else:
        driver = webdriver.Chrome(executable_path="chromedriver.exe")
        driver.implicitly_wait(5)

    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")