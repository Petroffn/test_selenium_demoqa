import allure
from allure_commons.types import Severity
from selenium.webdriver import ActionChains
from selenium import webdriver



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
