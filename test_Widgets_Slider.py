from selenium.webdriver.common.action_chains import ActionChains
import allure
from allure_commons.types import Severity
from selenium import webdriver


@allure.title('Test')
@allure.severity(Severity.BLOCKER)

def test_Widgets_Slider_01():
    driver = webdriver.Chrome()
    with allure.step('Open Slider page'):
        driver.get('https://demoqa.com/slider')
        driver.set_window_size(1920, 1080)

    import time
    time.sleep(3)

    with allure.step('Open move Slider'):
        slider = driver.find_element_by_xpath('//input[@class="range-slider range-slider--primary"]')

        move = ActionChains(driver)
        move.click_and_hold(slider).move_by_offset(10, 0).release().perform()

        import time
        time.sleep(5)

    with allure.step('Result 51'):
        assert "'51'"