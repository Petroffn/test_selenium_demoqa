import allure
from allure_commons.types import Severity
from selenium import webdriver



@allure.title('Test')
@allure.severity(Severity.BLOCKER)

def test_AFW_BW_01():
    driver = webdriver.Chrome()
    with allure.step('Open Practice Form page'):
        driver.get('https://demoqa.com/accordian')
        driver.set_window_size(1920, 1080)

    with allure.step('Check first text'):
        assert "'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'"

def test_AFW_BW_02():
    driver = webdriver.Chrome()
    with allure.step('Open Practice Form page'):
        driver.get('https://demoqa.com/accordian')
        driver.set_window_size(1920, 1080)

    with allure.step('Open new tab'):
        newtab = driver.find_element_by_xpath('//div[@id="section2Heading"]')
        newtab.click()

    with allure.step('Check first text'):
        assert "'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source.'"

def test_AFW_BW_03():
    driver = webdriver.Chrome()
    with allure.step('Open Practice Form page'):
        driver.get('https://demoqa.com/accordian')
        driver.set_window_size(1920, 1080)

    with allure.step('Open new tab'):
        newtab = driver.find_element_by_xpath('//div[@id="section3Heading"]')
        newtab.click()

    with allure.step('Check first text'):
        assert "'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).'"
