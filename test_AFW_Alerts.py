import allure
from allure_commons.types import Severity
from selenium import webdriver


@allure.title('Test')
@allure.severity(Severity.BLOCKER)

def test_AFW():
    driver = webdriver.Chrome()
    with allure.step('Open Practice Form page'):
        driver.get('https://demoqa.com/browser-windows')
        driver.set_window_size(1920, 1080)

