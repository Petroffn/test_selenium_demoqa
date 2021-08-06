import allure
from pages.radio_button_page import PageRadioBatton


class TestRadioBatton:
    @allure.title('Check all radio button')
    def test_open_page(self, driver):
        radiobutton_page = PageRadioBatton(driver)

        radiobutton_page.test_open_page()
        radiobutton_page.click_on_yes_button()
        radiobutton_page.check_yes_button()
        radiobutton_page.click_on_impressive_button()
        radiobutton_page.check_impressive_button()



