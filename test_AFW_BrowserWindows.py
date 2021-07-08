import allure
from allure_commons.types import Severity
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@allure.title('Test')
@allure.severity(Severity.BLOCKER)

def test_AFW():
    driver = webdriver.Chrome()
    with allure.step('Open Practice Form page'):
        driver.get('https://demoqa.com/alerts')
        driver.set_window_size(1920, 1080)

    with allure.step('Open Click me 1'):
        clickme1 = driver.find_element_by_xpath('//button[@id="alertButton"]')
        clickme1.click()

        WebDriverWait(driver, 10).until(EC.alert_is_present())
        driver.switch_to.alert.accept()

    with allure.step('OOpen Click me 2'):
        clickme2 = driver.find_element_by_xpath('//button[@id="timerAlertButton"]')
        clickme2.click()

        import time
        time.sleep(6)

        WebDriverWait(driver, 10).until(EC.alert_is_present())
        driver.switch_to.alert.accept()

    with allure.step('OOpen Click me 3'):
        clickme3 = driver.find_element_by_xpath('//button[@id="confirmButton"]')
        clickme3.click()
        link = driver.find_element_by_link_text('OK')
        link.click()
        assert "'You selected Cancel'" not in driver.page_source

