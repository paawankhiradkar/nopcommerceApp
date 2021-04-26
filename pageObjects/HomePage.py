from selenium import  webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from pageObjects import LoginPage

class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 10, poll_frequency=0.1, ignored_exceptions=[NoSuchElementException,
                                                                                            ElementNotVisibleException,
                                                                                            ElementNotSelectableException])
    @property
    def isLoginSuccesful(self):
        try:
            element: WebElement = self._wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Assets"]')))
            if element.text == "Asset":
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def clickDashboard(self):
        try:
            element: WebElement = self._wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Dashboard']/parent::span")))
            element.click()
        except Exception as e:
            print(e)
