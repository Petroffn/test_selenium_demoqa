import allure
from allure_commons.types import Severity
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



@allure.title('Test')
@allure.severity(Severity.BLOCKER)

def test_Widgets_AC_01():
    driver = webdriver.Chrome()
    with allure.step('Open Practice Form page'):
        driver.get('https://demoqa.com/auto-complete')
        driver.set_window_size(1920, 1080)

    import time
    time.sleep(3)

    with allure.step('Select Red and Blue'):
        elem1 = driver.find_element_by_xpath('//input[@id="autoCompleteMultipleInput"]')
        elem1.click()

        import time
        time.sleep(2)

        elem1.send_keys('Red')
        elem1.send_keys(Keys.ARROW_DOWN)
        elem1.send_keys(Keys.RETURN)

        import time
        time.sleep(2)

        elem1.send_keys('Blue')
        elem1.send_keys(Keys.ARROW_DOWN)
        elem1.send_keys(Keys.RETURN)

def test_Widgets_AC_02():
    driver = webdriver.Chrome()
    with allure.step('Open Practice Form page'):
        driver.get('https://demoqa.com/auto-complete')
        driver.set_window_size(1920, 1080)

    with allure.step('Select Blue'):
        elem2 = driver.find_element_by_xpath('//input[@id="autoCompleteSingleInput"]')
        elem2.click()

        import time
        time.sleep(2)

        elem2.send_keys('Blue')
        elem2.send_keys(Keys.ARROW_DOWN)
        elem2.send_keys(Keys.RETURN)


