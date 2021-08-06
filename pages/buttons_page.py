import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from config import BASE_URL
from conftest import driver
from locators.buttons_locators import ButtonsLocators


class TestButtonsPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Open https://demoqa.com/buttons Page')
    def test_open_page(self):
        self.driver.get(BASE_URL + '/buttons')

    @allure.step('double click')
    def double_click_button(self, action):
        self.driver.find_element(*ButtonsLocators.double_click_button).action()



