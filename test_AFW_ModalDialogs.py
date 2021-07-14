import allure
from allure_commons.types import Severity
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



@allure.title('Test')
@allure.severity(Severity.BLOCKER)

def test_modaldialod01():
    driver = webdriver.Chrome()
    with allure.step('Open Modal Dialogs page'):
        driver.get('https://demoqa.com/modal-dialogs')
        driver.set_window_size(1920, 1080)

    with allure.step('Click on Small modal button'):
        smallmodal_button = driver.find_element_by_xpath('//button[@id="showSmallModal"]')
        smallmodal_button.click()

    with allure.step('Check text Small modal'):
        assert "'This is a small modal. It has very less content'"

    with allure.step('Close the modal window'):
        close_button = driver.find_element_by_xpath('//button[@id="closeSmallModal"]')
        close_button.click()

    import time
    time.sleep(5)

def test_modaldialod02():
    driver = webdriver.Chrome()
    with allure.step('Open Modal Dialogs page'):
        driver.get('https://demoqa.com/modal-dialogs')
        driver.set_window_size(1920, 1080)

    with allure.step('Click on Large modal button'):
        largemodal_button = driver.find_element_by_xpath('//button[@id="showLargeModal"]')
        largemodal_button.click()

    with allure.step('Check text Large modal'):
        assert "'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'"

    with allure.step('Close the modal window'):
        close_button = driver.find_element_by_xpath('//button[@id="closeLargeModal"]')
        close_button.click()

