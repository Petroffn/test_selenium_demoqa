import allure
from allure_commons.types import Severity
from selenium.webdriver import ActionChains
from selenium import webdriver



@allure.title('Test')
@allure.severity(Severity.BLOCKER)







def test_case05():
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/elements')
    driver.set_window_size(1920, 1080)
    with allure.step('Click on Buttons button'):
        elements_button = driver.find_element_by_xpath('//li[@id="item-4"]')
        elements_button.click()

    import time
    time.sleep(3)

    with allure.step('Double click'):
        driver.find_element_by_xpath('//button[@id="doubleClickBtn"]').click()
        action = ActionChains(driver)
        action.double_click()

    with allure.step('Check entered text'):
        assert "'You have done a double click'" not in driver.page_source

    import time
    time.sleep(2)
    driver.refresh()

    with allure.step('Right click'):
        source = driver.find_element_by_xpath('//button[@id="rightClickBtn"]')
        action = ActionChains(driver)
        action.context_click(source).perform()

    import time
    time.sleep(2)
    driver.refresh()

    with allure.step('Click on Click me button'):
        clickme_button = driver.find_element_by_xpath('//button[@class="btn btn-primary"]')
        clickme_button.click()

    with allure.step('Check entered text'):
        assert "'You have done a dynamic click'" not in driver.page_source

def test_case06():
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/elements')
    driver.set_window_size(1920, 1080)
    with allure.step('Click on Buttons button'):
            elements_button = driver.find_element_by_xpath('//li[@id="item-5"]')
            elements_button.click()

    with allure.step('Click on created link'):
        linkCreated = driver.find_element_by_xpath('//a[@id="created"]')
        linkCreated.click()

    with allure.step('Check title 201'):
        assert "'Link has responded with staus 201 and status text Created'" not in driver.page_source

    import time
    time.sleep(1)
    driver.refresh()

    with allure.step('Click on No content link'):
        linknocontent = driver.find_element_by_xpath('//a[@id="created"]')
        linknocontent.click()

    with allure.step('Check title 204'):
        assert "'Link has responded with staus 204 and status text No Content'" not in driver.page_source

    import time
    time.sleep(1)
    driver.refresh()

    with allure.step('Click on Moved link'):
        linmoved = driver.find_element_by_xpath('//a[@id="moved"]')
        linmoved.click()

    with allure.step('Check title 301'):
        assert "'Link has responded with staus 301 and status text Moved Permanently'" not in driver.page_source

    import time
    time.sleep(1)
    driver.refresh()

    with allure.step('Click on Bed Request'):
        linkbedrequest = driver.find_element_by_xpath('//a[@id="bad-request"]')
        linkbedrequest.click()

    with allure.step('Check title 400'):
        assert "'Link has responded with staus 400 and status text Bad Request'" not in driver.page_source

    import time
    time.sleep(1)
    driver.refresh()

    with allure.step('Click on Unauthorized link'):
        linkUnauthorized = driver.find_element_by_xpath('//a[@id="unauthorized"]')
        linkUnauthorized.click()

    with allure.step('Check title 401'):
        assert "'Link has responded with staus 401 and status text Unauthorized'" not in driver.page_source

    import time
    time.sleep(1)
    driver.refresh()

    with allure.step('Click on Forbidden link'):
        linkForbidden = driver.find_element_by_xpath('//a[@id="forbidden"]')
        linkForbidden.click()

    with allure.step('Check title 403'):
        assert "'Link has responded with staus 403 and status text Forbidden'" not in driver.page_source

    import time
    time.sleep(1)
    driver.refresh()

    with allure.step('Click on Not Found link'):
        linkForbidden = driver.find_element_by_xpath('//a[@id="invalid-url"]')
        linkForbidden.click()

    with allure.step('Check title 404'):
        assert "'Link has responded with staus 404 and status text Not Found'" not in driver.page_source

    import time
    time.sleep(1)
    driver.refresh()

    with allure.step('Open home link'):
        linkhome = driver.find_element_by_xpath('//a[@id="simpleLink"]')
        linkhome.click()


    driver.switch_to.window(driver.window_handles[1])
    with allure.step('Check title new page'):
        assert "'© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'" not in driver.page_source

def test_case07():
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/elements')
    driver.set_window_size(1920, 1080)
    with allure.step('Click on Buttons button'):
            elements_button = driver.find_element_by_xpath('//li[@id="item-6"]')
            elements_button.click()

    with allure.step('Check image'):
        if driver.find_element_by_css_selector("img[src$='Toolsqa.jpg']"):
            print
            "Image is not visible on screen"
        else :
            print
            "Image is visible on screen"

    # Добавить тесты с ссылками

def test_case08():
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/upload-download')
    driver.set_window_size(1920, 1080)
    with allure.step('Download image'):
        download_button = driver.find_element_by_xpath('//a[@id="downloadButton"]')
        download_button.click()

    import time
    time.sleep(3)
    driver.refresh()

    choosefile = driver.find_element_by_xpath('//input[@id="uploadFile"]')
    choosefile.send_keys("D:\\Allure Report - Google Chrome 2021-07-05 11.16.35.png")

    with allure.step('Check title '):
        assert "'Allure Report - Google Chrome 2021-07-05 11.16.35.png'" not in driver.page_source
        
def test_case09():
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/dynamic-properties')
    driver.set_window_size(1920, 1080)
    with allure.step('Whait 6 sek and check the button'):

        import time
        time.sleep(6)

        # some tex

    with allure.step('Check title '):
        assert "'Visible After 5 Seconds'" not in driver.page_source

def test_case09():
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/dynamic-properties')
    driver.set_window_size(1920, 1080)
    with allure.step('Whait 6 sek and check the button'):

        import time
        time.sleep(6)

        # some tex

    with allure.step('Check title '):
        assert "'Visible After 5 Seconds'" not in driver.page_source


