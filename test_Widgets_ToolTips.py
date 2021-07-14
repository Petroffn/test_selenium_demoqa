import allure
from allure_commons.types import Severity
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


@allure.title('Test')
@allure.severity(Severity.BLOCKER)

def test_Widgets_ToolTips_01():
    driver = webdriver.Chrome()
    with allure.step('Open Slider page'):
        driver.get('https://demoqa.com/tool-tips')
        driver.set_window_size(1920, 1080)

    with allure.step('Check first ToolTips'):
        

