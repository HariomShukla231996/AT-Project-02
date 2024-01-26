from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import pytest
from Data import data
from Locators import locators


class Test_OrangeHRM:

   @pytest.fixture
   def booting_function(self):
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
       self.driver.implicitly_wait(10)
       yield
       self.driver.close()


   def test_password_link(self, booting_function):
       self.driver.get(data.Web_Data().url)
       self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().forgot_password_locator).click()
       self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().username_locator).send_keys(data.Web_Data().username)
       self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().reset_password_locator).click()
       assert self.driver.current_url == data.Web_Data().dashboard_url
       print("Reset password link sent successfully")




