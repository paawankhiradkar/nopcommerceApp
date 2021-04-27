from selenium import  webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from pageObjects import LoginPage

class HomePage():

    dashboard_xpath = "//span[text()='Dashboard']/parent::span"
    assets_xpath = "//span[text()='Assets']"
    health_xpath = "//span[text()='Health']"
    resources_xpath = "//span[text()='Resources']"
    home_xpath = "//a[@href='/appui/app/server/home/reportView?routeId=reports_view']"
    status_xpath = "//a[@href='app/server/status']"
    license_xpath = "//a[@href='app/server/license']"
    manage_xpath = "//a[@href='/appui/app/server/manage']"
    profile_xpath = "//a[@id='profile']"
    logout_xpath = "//span[text()='Logout']"

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

    def click(self, label, logger):
        self.label = label.lower()
        self.logger = logger
        if self.label == 'dashboard':
            try:
                element: WebElement = self._wait.until(EC.element_to_be_clickable((By.XPATH,self.dashboard_xpath)))
                element.click()
            except Exception as e:
                self.logger.info(e)
                self.logger.info("Could not find element {}".format(self.label))
        elif self.label == 'assets':
            try:
                element: WebElement = self._wait.until(EC.element_to_be_clickable((By.XPATH,self.assets_xpath)))
                element.click()
            except Exception as e:
                self.logger.info(e)
                self.logger.info("Could not find element {}".format(self.label))
        elif self.label == 'health':
            try:
                element: WebElement = self._wait.until(EC.element_to_be_clickable((By.XPATH,self.health_xpath)))
                element.click()
            except Exception as e:
                self.logger.info(e)
                self.logger.info("Could not find element {}".format(self.label))
        elif self.label == 'resources':
            try:
                element: WebElement = self._wait.until(EC.element_to_be_clickable((By.XPATH,self.resources_xpath)))
                element.click()
            except Exception as e:
                self.logger.info(e)
                self.logger.info("Could not find element {}".format(self.label))
        elif self.label == 'home':
            try:
                element: WebElement = self._wait.until(EC.element_to_be_clickable((By.XPATH,)))
                element.click()
            except Exception as e:
                self.logger.info(e)
                self.logger.info("Could not find element {}".format(self.label))
        elif self.label == 'status':
            try:
                element: WebElement = self._wait.until(EC.element_to_be_clickable((By.XPATH,self.status_xpath)))
                element.click()
            except Exception as e:
                self.logger.info(e)
                self.logger.info("Could not find element {}".format(self.label))
        elif self.label == 'license':
            try:
                element: WebElement = self._wait.until(EC.element_to_be_clickable((By.XPATH,self.license_xpath)))
                element.click()
            except Exception as e:
                self.logger.info(e)
                self.logger.info("Could not find element {}".format(self.label))
        elif self.label == 'manage':
            try:
                element: WebElement = self._wait.until(EC.element_to_be_clickable((By.XPATH,self.manage_xpath)))
                element.click()
            except Exception as e:
                self.logger.info(e)
                self.logger.info("Could not find element {}".format(self.label))
        elif self.label == 'profile':
            try:
                element: WebElement = self._wait.until(EC.element_to_be_clickable((By.XPATH,self.profile_xpath)))
                element.click()
            except Exception as e:
                self.logger.info(e)
                self.logger.info("Could not find element {}".format(self.label))

    def logout(self, logger):
        self.logger = logger
        self.click('profile', self.logger)
        element: WebElement = self._wait.until(EC.element_to_be_clickable((By.XPATH,self.logout_xpath)))
        element.click()


