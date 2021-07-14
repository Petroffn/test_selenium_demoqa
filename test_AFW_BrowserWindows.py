import allure
from allure_commons.types import Severity
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@allure.title('Test')
@allure.severity(Severity.BLOCKER)

def test_AFW_01():
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

    with allure.step('Open Click me 3'):
        clickme3 = driver.find_element_by_xpath('//button[@id="confirmButton"]')
        clickme3.click()
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        driver.switch_to.alert.accept()
        assert "'You selected Cancel'" not in driver.page_source

    with allure.step('Open Click me 4'):
        clickme3 = driver.find_element_by_xpath('//button[@id="promtButton"]')
        clickme3.click()

        obj = driver.switch_to.alert
        obj.send_keys('Mykola')

        import time
        time.sleep(2)

        obj.accept()

        message = obj.text
        print("Alert shows following message: " + message)

        time.sleep(2)

        obj.accept()

        # get the text returned when OK Button is clicked.
        txt = driver.find_element_by_id('msg')
        print(txt.text)

        #WebDriverWait(driver, 10).until(EC.alert_is_present())
        #driver.switch_to.alert.accept()
        assert "'You entered Mykola'" not in driver.page_source

