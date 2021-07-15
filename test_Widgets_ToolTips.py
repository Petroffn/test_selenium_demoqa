import allure
from allure_commons.types import Severity
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


@allure.title('Test')
@allure.severity(Severity.BLOCKER)

def test_Widgets_ToolTips_01():
    driver = webdriver.Chrome()
    with allure.step('Open Slider page'):
        driver.get('https://demoqa.com/tool-tips')
        driver.set_window_size(1920, 1080)

    with allure.step('Check first ToolTips'):
        action = ActionChains(driver)
        hovered_button = driver.find_element_by_xpath('//button[@id="toolTipButton"]')
        action.move_to_element(hovered_button).perform()

        time.sleep(1)

    with allure.step('Check text'):
        assert "'You hovered over the Button'"

def test_Widgets_ToolTips_02():
    driver = webdriver.Chrome()
    with allure.step('Open ToolTips page'):
        driver.get('https://demoqa.com/tool-tips')
        driver.set_window_size(1920, 1080)

    with allure.step('Check button ToolTips'):
        action = ActionChains(driver)
        hovered_input = driver.find_element_by_xpath('//input[@id="toolTipTextField"]')
        action.move_to_element(hovered_input).perform()

        time.sleep(1)

    with allure.step('Check text'):
        assert "'You hovered over the the text field'"

def test_Widgets_ToolTips_03():
    driver = webdriver.Chrome()
    with allure.step('Open ToolTips page'):
        driver.get('https://demoqa.com/tool-tips')
        driver.set_window_size(1920, 1080)

    with allure.step('Check text ToolTips'):
        action = ActionChains(driver)
        hovered_text1 = driver.find_element_by_link_text('Contrary')
        action.move_to_element(hovered_text1).perform()

        time.sleep(1)

    with allure.step('Check text'):
        assert "'You hovered over the the Contrary'"

def test_Widgets_ToolTips_04():
    driver = webdriver.Chrome()
    with allure.step('Open ToolTips page'):
        driver.get('https://demoqa.com/tool-tips')
        driver.set_window_size(1920, 1080)

    with allure.step('Check text ToolTips'):
        action = ActionChains(driver)
        hovered_text2 = driver.find_element_by_link_text('1.10.32')
        action.move_to_element(hovered_text2).perform()

        time.sleep(1)

    with allure.step('Check text'):
        assert "'You hovered over the the 1.10.32'"