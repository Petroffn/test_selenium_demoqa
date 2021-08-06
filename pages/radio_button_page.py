import allure
from config import BASE_URL
from locators.radio_button_locators import TestRadioLocators


class PageRadioBatton:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Open https://demoqa.com/radio-button page')
    def test_open_page(self):
        self.driver.get(BASE_URL + '/radio-button')

    @allure.step('Select Yes radio button')
    def click_on_yes_button(self):
        self.driver.find_element(*TestRadioLocators.click_on_yes_button).click()

    @allure.step('Check Yes radio button')
    def check_yes_button(self):
        self.driver.find_element(*TestRadioLocators.check_yes_button)

    @allure.step('Select impressive radio button')
    def click_on_impressive_button(self):
        self.driver.find_element(*TestRadioLocators.click_on_impressive_butto).click()

    @allure.step('Check impressive radio button')
    def check_impressive_button(self):
        self.driver.find_element(*TestRadioLocators.check_impressive_button)
