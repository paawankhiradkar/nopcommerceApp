import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.HomePage import HomePage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_002_homePage:
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.logGen()

    def test_succesfulLogin(self,setup):
        self.logger.info("*****Verfying Test_002_homePage*********")
        self.logger.info("*****Verfying if login successful*********")
        self.driver = setup
        self.driver.get(self.baseURL)
        loginPage = LoginPage(self.driver)
        loginPage.setUserName(self.username)
        loginPage.setPassword(self.password)
        loginPage.clickLogin()
        homepage = HomePage(self.driver)
        if homepage.isLoginSuccesful:
            assert True
            self.logger.info("**********Login Succesful**********")
            self.driver.close()
        else:
            self.logger.info("Login Failed")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_successful_login.png")
            self.driver.close()
            assert False

    @pytest.mark.dashboard
    def test_dashboard_clickable(self,setup):
        self.logger.info("Verifying dashboard.")
        self.driver = setup
        self.driver.get(self.baseURL)
        loginPage = LoginPage(self.driver)
        loginPage.setUserName(self.username)
        loginPage.setPassword(self.password)
        loginPage.clickLogin()
        homePage = HomePage(self.driver)
        homePage.clickDashboard()
        if self.driver.find_element(By.XPATH,"//span[text()='Dashboard']/parent::div").is_displayed():
            assert True
            self.logger.info("Dashboard visible.")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_dashboard_clickable.png")
            self.logger.info("Dashboard NOT visbile.")
            self.driver.close()
            assert False
