import allure
from allure_commons.types import Severity
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@allure.title('Test')
@allure.severity(Severity.BLOCKER)

def test_AFW_BW_01():
    driver = webdriver.Chrome()
    with allure.step('Open Practice Form page'):
        driver.get('https://demoqa.com/browser-windows')
        driver.set_window_size(1920, 1080)

    with allure.step('Open new tab'):
        newtab = driver.find_element_by_xpath('//button[@id="tabButton"]')
        newtab.click()

    driver.switch_to.window(driver.window_handles[1])
    with allure.step('Check title'):
        assert "'This is a sample page'"

def test_AFW_BW_02():
    driver = webdriver.Chrome()
    with allure.step('Open Practice Form page'):
        driver.get('https://demoqa.com/browser-windows')
        driver.set_window_size(1920, 1080)

    with allure.step('Open new window'):
        newwindow = driver.find_element_by_xpath('//button[@id="windowButton"]')
        newwindow.click()

    driver.switch_to.window(driver.window_handles[1])
    with allure.step('Check title'):
        assert "'This is a sample page'"

def test_AFW_BW_03():
    driver = webdriver.Chrome()
    with allure.step('Open Practice Form page'):
        driver.get('https://demoqa.com/browser-windows')
        driver.set_window_size(1920, 1080)

    with allure.step('Open new window'):
        newmessage = driver.find_element_by_xpath('//button[@id="messageWindowButton"]')
        newmessage.click()

        driver.switch_to.window(driver.window_handles[1])
        with allure.step('Check title'):
            assert "'Knowledge increases by sharing but not by saving. Please share this website with your friends and in your organization.'"

