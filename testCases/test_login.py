import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.logGen()

    def test_homePageTitle(self,setup):
        self.logger.info("**********Test_001_Login**********")
        self.logger.info("**********verifying test_homePageTitle**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "MARS Iris":
            assert True
            self.driver.close()
            self.logger.info("**********verifying test_homePageTitle passed**********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("******************verifying test_homePageTitle failed**********")
            assert False


    def test_login(self, setup):
        self.logger.info("**********verifying test_login**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        if actual_title == "MARS Iris":
            assert True
            self.driver.close()
            self.logger.info("**********verifying test_login passed**********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("**********verifying test_login failed**********")
            assert False

