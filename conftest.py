import allure
import pytest
from selenium import webdriver


@pytest.fixture()
def driver(request):
    with allure.step('Open Browser'):
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.implicitly_wait(5)
        request.addfinalizer(driver.quit)
        return driver

