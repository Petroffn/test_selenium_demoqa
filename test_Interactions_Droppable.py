import allure
from allure_commons.types import Severity
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_Widgets_ToolTips_01():
    driver = webdriver.Chrome()
    with allure.step('Open droppable page'):
        driver.get('https://demoqa.com/droppable')
        driver.set_window_size(1920, 1080)

