from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://demo.mars-iris.com/")
driver.find_element_by_id("login_UserId").send_keys("irisadmin")
driver.find_element_by_id("login_Password").send_keys("Demo%789")
driver.find_element_by_id("login_Submit").click()
_wait = WebDriverWait(driver,10,poll_frequency=0.1, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                                        ElementNotSelectableException] )
asset_elemet: WebElement = _wait.until(EC.element_to_be_clickable((By.XPATH,'//span[text()="Assets"]')))
#driver.find_element_by_xpath('//span[text()="Assets"]')
print(asset_elemet)
print(asset_elemet.text)
print(asset_elemet.get_attribute("class"))
print(asset_elemet.get_attribute("name"))