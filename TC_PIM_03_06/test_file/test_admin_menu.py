from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from webdriver_manager.firefox import GeckoDriverManager
import pytest
from Data import data
from Locators import locators

class Test_OrangeHRM_Menu:

    @pytest.fixture
    def booting_function(self):
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
       self.driver.implicitly_wait(6)
       yield
       self.driver.close()


    def test_admin_options(self, booting_function):
       self.driver.get(data.Web_Data().url)
       self.driver.find_element(by=By.NAME, value=locators.Web_Locators().username_locator).send_keys(
           data.Web_Data().username)
       self.driver.find_element(by=By.NAME, value=locators.Web_Locators().password_locator).send_keys(
           data.Web_Data().password)
       self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().submit_button_locator).click()
       self.driver.implicitly_wait(10)
       self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().admin_locator).click()
       assert self.driver.find_element(by=By.XPATH,
                                       value=locators.Web_Locators().pim_locator).is_displayed(), "PIM Menu not displayed"
       assert self.driver.find_element(by=By.XPATH,
                                       value=locators.Web_Locators().leave_locator).is_displayed(), "Leave Menu not displayed"
       assert self.driver.find_element(by=By.XPATH,
                                       value=locators.Web_Locators().time_locator).is_displayed(), "Time Menu not displayed"
       assert self.driver.find_element(by=By.XPATH,
                                       value=locators.Web_Locators().recruitment_locator).is_displayed(), "Recruitment Menu not displayed"
       assert self.driver.find_element(by=By.XPATH,
                                       value=locators.Web_Locators().my_info_locator).is_displayed(), "My Info option not displayed"
       assert self.driver.find_element(by=By.XPATH,
                                       value=locators.Web_Locators().performance_locator).is_displayed(), "Performance Option not displayed"
       assert self.driver.find_element(by=By.XPATH,
                                       value=locators.Web_Locators().dashboard_locator).is_displayed(), "Dashboard Menu not displayed"
       assert self.driver.find_element(by=By.XPATH,
                                       value=locators.Web_Locators().directory_locator).is_displayed(), "Directory not displayed"
       assert self.driver.find_element(by=By.XPATH,
                                       value=locators.Web_Locators().maintenance_locator).is_displayed(), "Maintenance not displayed"
       assert self.driver.find_element(by=By.XPATH,
                                       value=locators.Web_Locators().buzz_locator).is_displayed(), "Buzz option not displayed"