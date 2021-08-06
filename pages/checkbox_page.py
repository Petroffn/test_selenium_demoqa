import allure

from config import BASE_URL
from locators.checkbox_locators import CheckBoxLocators


class TestCheckPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Open https://demoqa.com/checkbox Page')
    def test_open_page(self):
        self.driver.get(BASE_URL + '/checkbox')

    @allure.step('Select tree node home')
    def select_tree_node_home(self):
        self.driver.find_element(*CheckBoxLocators.expand_all).click()
        self.driver.find_element(*CheckBoxLocators.select_tree_node_home).click()

    @allure.step('Check the text')
    def check_text_tree_node_home(self):
        self.driver.find_element(*CheckBoxLocators.check_text_tree_node_home)
        self.driver.find_element(*CheckBoxLocators.select_tree_node_home).click()

    @allure.step('Select tree node home')
    def select_tree_node_desktop(self):
        self.driver.find_element(*CheckBoxLocators.select_tree_node_desktop).click()

    @allure.step('Check the text')
    def check_text_tree_node_desktop(self):
        self.driver.find_element(*CheckBoxLocators.check_text_tree_node_desktop)
        self.driver.find_element(*CheckBoxLocators.select_tree_node_desktop).click()

