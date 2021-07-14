import allure
from allure_commons.types import Severity
from selenium import webdriver


@allure.title('Test')
@allure.severity(Severity.BLOCKER)

def test_AFW_alerts01():
    driver = webdriver.Chrome()
    with allure.step('Click Button to see alert'):
        driver.get('https://demoqa.com/alerts')
        driver.set_window_size(1920, 1080)

    with allure.step('Click on Click me button to open alert'):
        clickme01_button = driver.find_element_by_xpath('//button[@id="alertButton"]')
        clickme01_button.click()

    p = driver.switch_to.alert.text
    print("You clicked a button")
    print(p)

    import time
    time.sleep(1)

    alert = driver.switch_to.alert
    alert.accept()


def test_AFW_alerts02():
    driver = webdriver.Chrome()
    with allure.step('Click on Click me button to open alert after 5 sec'):
        driver.get('https://demoqa.com/alerts')
        driver.set_window_size(1920, 1080)

    with allure.step('Click on Click me button'):
        clickme02_button = driver.find_element_by_xpath('//button[@id="timerAlertButton"]')
        clickme02_button.click()

    import time
    time.sleep(6)

    sec = driver.switch_to.alert.text
    print("This alert appeared after 5 seconds")
    print(sec)

    alert = driver.switch_to.alert
    alert.accept()

    import time
    time.sleep(1)
    driver.refresh()

def test_AFW_alerts03():
    driver = webdriver.Chrome()
    with allure.step('Click on Click me button then accept'):
        driver.get('https://demoqa.com/alerts')
        driver.set_window_size(1920, 1080)

    with allure.step('Click on Click me button'):
        clickme03_button = driver.find_element_by_xpath('//button[@id="confirmButton"]')
        clickme03_button.click()

    import time
    time.sleep(2)

    alert = driver.switch_to.alert
    alert.accept()

    with allure.step('Check the text for - On button click, confirm box will OK'):
        assert "'You selected Ok'"

    import time
    time.sleep(1)
    driver.refresh()

def test_AFW_alerts04():
    driver = webdriver.Chrome()
    with allure.step('Click on Click me button then dismiss'):
        driver.get('https://demoqa.com/alerts')
        driver.set_window_size(1920, 1080)

    with allure.step('Click on Click me button'):
        clickme03_button = driver.find_element_by_xpath('//button[@id="confirmButton"]')
        clickme03_button.click()

    import time
    time.sleep(2)

    alert = driver.switch_to.alert
    alert.dismiss()

    with allure.step('Check the text for - On button click, confirm box will appear Cancel'):
        assert "'You selected Cancel'"

    import time
    time.sleep(1)
    driver.refresh()

def test_AFW_alerts05():
    driver = webdriver.Chrome()
    with allure.step('Click on Click me button then accept'):
        driver.get('https://demoqa.com/alerts')
        driver.set_window_size(1920, 1080)

    with allure.step('Click on Click me button'):
        clickme04_button = driver.find_element_by_xpath('//button[@id="promtButton"]')
        clickme04_button.click()

    import time
    time.sleep(2)

    alert = driver.switch_to.alert
    alert.send_keys('qa')
    alert.accept()

    import time
    time.sleep(2)

    with allure.step('Check the text for - On button click, confirm box will appear Cancel'):
        assert "'You entered qa'"