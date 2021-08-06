import allure
from pages.checkbox_page import TestCheckPage


class TestCheckBox:
    @allure.title('Check checkboxes')
    def test_open_page(self, driver):
        checkbox_page = TestCheckPage(driver)

        checkbox_page.test_open_page()
        checkbox_page.select_tree_node_home()
        checkbox_page.check_text_tree_node_home()
        checkbox_page.select_tree_node_home()
        checkbox_page.select_tree_node_desktop()

