import allure
from allure_commons.types import Severity
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait


@allure.title('Test')
@allure.severity(Severity.BLOCKER)

def test_forms01():
    driver = webdriver.Chrome()
    with allure.step('Open Practice Form page'):
        driver.get('https://demoqa.com/automation-practice-form')
        driver.set_window_size(1920, 1080)

    with allure.step('Enter Full Name'):
        name_input = driver.find_element_by_xpath('//input[@placeholder="First Name"]')
        name_input.send_keys('Mykola')

    with allure.step('Enter Full Name'):
        name_input = driver.find_element_by_xpath('//input[@placeholder="Last Name"]')
        name_input.send_keys('Petrov')

    with allure.step('Enter Full Name'):
        name_input = driver.find_element_by_xpath('//input[@placeholder="name@example.com"]')
        name_input.send_keys('petroffn@gmail.com')

    with allure.step('Click on Radio button Yes'):
        driver.find_element_by_xpath('//label[@for="gender-radio-1"]').click()

    with allure.step('Enter Phone number'):
        name_input = driver.find_element_by_xpath('//input[@id="userNumber"]')
        name_input.send_keys('0661324657')

    with allure.step('Select data'):
        datefield = driver.find_element_by_id("dateOfBirthInput")
        datefield.click()
        months = driver.find_elements_by_css_selector("select[class*='month-select'] option")
        for month in months:
            if month.text == "June":
                month.click()
                time.sleep(5)
                break

        days = driver.find_elements_by_css_selector("div[class*='datepicker__day']")
        for day in days:
            if day.text == "15":
                day.click()
                break

    with allure.step('Select Sports checkbox'):
        driver.find_element_by_xpath('//label[@for="hobbies-checkbox-1"]').click()

    picture = driver.find_element_by_xpath('//input[@id="uploadPicture"]')
    picture.send_keys("D:\\Allure Report - Google Chrome 2021-07-05 11.16.35.png")

    with allure.step('Enter Current Address'):
        currentaddress_input = driver.find_element_by_xpath('//textarea[@placeholder="Current Address"]')
        currentaddress_input.send_keys('вулиця Пушкінська, 2а, Харків, Харківська область, Украина, 61000')

    # Need creare tests for State and Sity

    with allure.step('Click on Submit button'):
        submit_button = driver.find_element_by_xpath('//button[@id="submit"]')
        submit_button.click()


