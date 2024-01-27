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


class Test_OrangeHRM:

   @pytest.fixture
   def booting_function(self):
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
       self.driver.implicitly_wait(6)
       yield
       self.driver.close()


   def test_get_title(self, booting_function):
       self.driver.get(data.Web_Data().url)
       assert self.driver.title == data.Web_Data().homepage_title
       print("SUCCESS : Web Title Verified")


   def test_login(self, booting_function):
       self.driver.get(data.Web_Data().url)
       self.driver.find_element(by=By.NAME, value=locators.Web_Locators().username_locator).send_keys(data.Web_Data().username)
       self.driver.find_element(by=By.NAME, value=locators.Web_Locators().password_locator).send_keys(data.Web_Data().password)
       self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().submit_button_locator).click()
       assert self.driver.current_url == data.Web_Data().dashboard_url
       print("SUCCESS : Logged in with Username {a} & Password {b}".format(a=data.Web_Data().username, b=data.Web_Data.password))


   def test_admin_options(self, booting_function):
       self.driver.get(data.Web_Data().url)
       self.driver.find_element(by=By.NAME, value=locators.Web_Locators().username_locator).send_keys(
           data.Web_Data().username)
       self.driver.find_element(by=By.NAME, value=locators.Web_Locators().password_locator).send_keys(
           data.Web_Data().password)
       self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().submit_button_locator).click()
       self.driver.implicitly_wait(10)
       self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().Admin_locator).click()
       self.driver.implicitly_wait(6)
       assert self.driver.find_element(by=By.XPATH,
                                       value=locators.Web_Locators().User_Management_locator).is_displayed(), "User Management not displayed"
       assert self.driver.find_element(by=By.XPATH,
                                       value=locators.Web_Locators().Qualifications_locator).is_displayed(), "Qualifications not displayed"
       assert self.driver.find_element(by=By.XPATH,
                                       value=locators.Web_Locators().Job_locator).is_displayed(), "Job not displayed"
       assert self.driver.find_element(by=By.XPATH,
                                       value=locators.Web_Locators().Organization_locator).is_displayed(), "Organization not displayed"
       assert self.driver.find_element(by=By.XPATH,
                                       value=locators.Web_Locators().Nationalities_locator).is_displayed(), "Nationalities not displayed"
       assert self.driver.find_element(by=By.XPATH,
                                       value=locators.Web_Locators().Corporate_branding_locator).is_displayed(), "Corporate branding not displayed"
       assert self.driver.find_element(by=By.XPATH,
                                       value=locators.Web_Locators().Configuration_locator).is_displayed(), "Configuration not displayed"