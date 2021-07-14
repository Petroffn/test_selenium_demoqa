from selenium.webdriver.common.action_chains import ActionChains
import allure
from allure_commons.types import Severity
from selenium import webdriver


@allure.title('Test')
@allure.severity(Severity.BLOCKER)

def test_Widgets_Tabs_01():
    driver = webdriver.Chrome()
    with allure.step('Open Tabs page'):
        driver.get('https://demoqa.com/tabs')
        driver.set_window_size(1920, 1080)

    with allure.step('Check content from Origin'):
        origin_button = driver.find_element_by_xpath('//a[@id="demo-tab-origin"]')
        origin_button.click()

    with allure.step('Check Text'):
        assert "'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.'"

def test_Widgets_Tabs_02():
    driver = webdriver.Chrome()
    with allure.step('Open Tabs page'):
        driver.get('https://demoqa.com/tabs')
        driver.set_window_size(1920, 1080)

    with allure.step('Check content from Use'):
        origin_button = driver.find_element_by_xpath('//a[@id="demo-tab-use"]')
        origin_button.click()

    with allure.step('Check Text'):
        assert "'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).'"

