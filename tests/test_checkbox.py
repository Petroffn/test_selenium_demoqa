import allure
from pages.checkbox_page import

class TestCheckBox:
    @allure.title('Check checkboxes')
    def test_open_page(self, driver):
        checkbox_page = TestCheckPage(driver)

        checkbox_page.test_open_page()

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