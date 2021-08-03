import allure

from config import BASE_URL


class TestCheckPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Open https://demoqa.com/checkbox Page')
    def test_open_page(self):
        self.driver.get(BASE_URL + '/checkbox')