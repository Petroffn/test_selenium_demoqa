import allure
from allure_commons.types import Severity
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait


@allure.title('Test')
@allure.severity(Severity.BLOCKER)

def test_AFW():
    driver = webdriver.Chrome()
    with allure.step('Open Practice Form page'):
        driver.get('https://demoqa.com/browser-windows')
        driver.set_window_size(1920, 1080)