import allure
from allure_commons.types import Severity
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



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
        name_input.send_keys('example@gmail.com')

    with allure.step('Click on Radio button Yes'):
        driver.find_element_by_xpath('//label[@for="gender-radio-1"]').click()

    with allure.step('Enter Phone number'):
        name_input = driver.find_element_by_xpath('//input[@id="userNumber"]')
        name_input.send_keys('0661324657')

    import time
    time.sleep(3)

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

    import time
    time.sleep(3)

    with allure.step('Select Subjects'):
        elem = driver.find_element_by_id("subjectsInput")
        elem.send_keys("English")
        elem.send_keys(Keys.ARROW_DOWN)
        elem.send_keys(Keys.RETURN)

    with allure.step('Select Sports checkbox'):
        driver.find_element_by_xpath('//label[@for="hobbies-checkbox-1"]').click()

    picture = driver.find_element_by_xpath('//input[@id="uploadPicture"]')
    picture.send_keys("D:\\Allure Report - Google Chrome 2021-07-05 11.16.35.png")

    with allure.step('Enter Current Address'):
        currentaddress_input = driver.find_element_by_xpath('//textarea[@placeholder="Current Address"]')
        currentaddress_input.send_keys('56 Breakspears Rd, London SE4 1UL, UK')

    # Need creare tests for State and Sity
    import time
    time.sleep(2)

    with allure.step('Enter State'):
        state_button = driver.find_element_by_xpath('//input[@id="react-select-3-input"]')
        state_button.send_keys("NCR", Keys.ENTER)

    import time
    time.sleep(3)

    with allure.step('Enter City'):
        city_button = driver.find_element_by_xpath('//input[@id="react-select-4-input"]')
        city_button.send_keys("Delhi", Keys.ENTER + Keys.TAB + Keys.ENTER)



