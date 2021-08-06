import allure
from selenium.webdriver import ActionChains

from pages.buttons_page import TestButtonsPage


class TestButtons:
    @allure.title('Check all buttons')
    def test_open_page(self, driver):
        buttons_page = TestButtonsPage(driver)
        action = ActionChains(driver)

        buttons_page.test_open_page()
        buttons_page.double_click_button()
        action.double_click()



'''with allure.step('Double click'):
        driver.find_element_by_xpath('//button[@id="doubleClickBtn"]')
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
        assert "'You have done a dynamic click'" not in driver.page_source'''
