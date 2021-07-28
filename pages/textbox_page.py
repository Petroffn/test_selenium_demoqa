import allure
from selenium.webdriver.common.keys import Keys
from locators.textbox_locators import TextBoxLocators


class TextBoxPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Open https://demoqa.com/text-box Page')
    def test_open_page(self):
        self.driver.get('https://demoqa.com/text-box')

    @allure.step('Select full name field')
    def select_first_name_field(self):
        self.driver.find_element(*TextBoxLocators.select_field_full_name).click()

    @allure.step('Enter First Name')
    def input_first_name(self, fullname):
        self.driver.find_element(*TextBoxLocators.enter_full_name).send_keys(fullname)

    @allure.step('Select full name field')
    def select_first_email_field(self):
        self.driver.find_element(*TextBoxLocators.select_field_email_name).click()

    @allure.step('Enter First Name')
    def input_email(self, email):
        self.driver.find_element(*TextBoxLocators.enter_email).send_keys(email)

    @allure.step('Enter Current Address')
    def input_current_address(self, currentaddress):
        self.driver.find_element(*TextBoxLocators.enter_current_address).send_keys(currentaddress)

    @allure.step('Enter Permanent Address')
    def input_permanent_address(self, permanentaddress):
        self.driver.find_element(*TextBoxLocators.enter_permanent_address).send_keys(permanentaddress)

    @allure.step('scroll')
    def scroll(self):
        self.driver.find_element_by_tag_name('html').send_keys(Keys.END)

    @allure.step('click on the submit button')
    def click_submit_button(self):
        self.driver.find_element(*TextBoxLocators.button_submit).click()

    @allure.step('Check entered text')
    def check_text_name(self):
        assert "'Name:Mykola Petrov'"

    @allure.step('Check Full Name text')
    def check_text_name(self):
        assert "'Name:Mykola Petrov'"

    @allure.step('Check Full Name text')
    def check_text_email(self):
        assert "'Email:example@example.com'"

    @allure.step('Check Current Address text')
    def check_text_currentaddress(self):
        assert "'Current Address :40 Central Park S, New York, NY 10019'"

    @allure.step('Check Permananet Address text')
    def check_text_permananetaddress(self):
        assert "'1 Central Park West New York NY 10023'"
