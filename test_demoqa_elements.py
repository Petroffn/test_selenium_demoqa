import allure
from allure_commons.types import Severity
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait


@allure.title('Test')
@allure.severity(Severity.BLOCKER)

def test_case01():
    driver = webdriver.Chrome()
    with allure.step('Open DemoQA elements page'):
        driver.get('https://demoqa.com/elements')
        driver.set_window_size(1920, 1080)

    with allure.step('Click on Text Box button'):
        elements_button = driver.find_element_by_xpath('//li[@id="item-0"]')
        elements_button.click()

    with allure.step('Enter Full Name'):
        fullname_input = driver.find_element_by_xpath('//input[@placeholder="Full Name"]')
        fullname_input.send_keys('Mykola Petrov')

    with allure.step('Enter email'):
        email_input = driver.find_element_by_xpath('//input[@placeholder = "name@example.com"]')
        email_input.send_keys('petroffn@gmail.com')

    with allure.step('Enter Current Address'):
        currentaddress_input = driver.find_element_by_xpath('//textarea[@placeholder = "Current Address"]')
        currentaddress_input.send_keys('вулиця Пушкінська, 2а, Харків, Харківська область, Украина, 61000')

    with allure.step('Enter Permanent Address'):
        currentaddress_input = driver.find_element_by_xpath('//textarea[@id="permanentAddress"]')
        currentaddress_input.send_keys('вулиця Героїв Праці, 7, Харків, Харківська область, Украина, 61000')

    with allure.step('Click on Submit button'):
        submit_button = driver.find_element_by_xpath('//button[@id="submit"]')
        submit_button.click()


    with allure.step('Check entered text'):
        assert "'Name:Mykola Petrov Email:petroffn@gmail.com Current Address :вулиця Пушкінська, 2а, Харків, Харківська область, Украина, 61000 Permananet Address :вулиця Героїв Праці, 7, Харків, Харківська область, Украина, 61000" not in driver.page_source

def test_case02():
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/elements')
    driver.set_window_size(1920, 1080)
    with allure.step('Click on Check Box button'):
        elements_button = driver.find_element_by_xpath('//li[@id="item-1"]')
        elements_button.click()


    with allure.step('Open home tree'):
        expand_button = driver.find_element_by_xpath('//button[@title="Expand all"]')
        expand_button.click()

    with allure.step('Hide home tree'):
        collapse_button = driver.find_element_by_xpath('//button[@title="Collapse all"]')
        collapse_button.click()

    with allure.step('Open home tree'):
        expand_button = driver.find_element_by_xpath('//button[@title="Expand all"]')
        expand_button.click()

    with allure.step('Select Home checkbox'):
        driver.find_element_by_xpath('//label[@for="tree-node-home"]').click()


    with allure.step('Check entered text'):
        assert "'You have selected : home desktop notes commands documents workspace react angular veu office public private classified general downloads wordFile excelFile'" not in driver.page_source


    with allure.step('Unselect Home checkbox'):
        driver.find_element_by_xpath('//label[@for="tree-node-home"]').click()

    with allure.step('Select Descktop checkbox'):
        driver.find_element_by_xpath('//label[@for="tree-node-desktop"]').click()

    with allure.step('Check entered text'):
        assert "'You have selected : desktop notes commands'" not in driver.page_source

    with allure.step('Unelect Descktop checkbox'):
        driver.find_element_by_xpath('//label[@for="tree-node-desktop"]').click()

    with allure.step('Select Notes checkbox'):
        driver.find_element_by_xpath('//label[@for="tree-node-notes"]').click()

    with allure.step('Check entered text'):
        assert "'You have selected : notes'" not in driver.page_source

    with allure.step('Unelect Descktop checkbox'):
        driver.find_element_by_xpath('//label[@for="tree-node-notes"]').click()


def test_case03():
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/elements')
    driver.set_window_size(1920, 1080)
    with allure.step('Click on Radio button'):
        elements_button = driver.find_element_by_xpath('//li[@id="item-2"]')
        elements_button.click()

    with allure.step('Click on Radio button Yes'):
        driver.find_element_by_xpath('//label[@for="yesRadio"]').click()

    with allure.step('Check entered text'):
        assert "'You have selected Yes'" not in driver.page_source

    with allure.step('Click on Radio button "Impressive"'):
        driver.find_element_by_xpath('//label[@for="impressiveRadio"]').click()

    with allure.step('Check entered text'):
        assert "'You have selected Impressive'" not in driver.page_source


