import allure
from selenium.webdriver.common.keys import Keys

from config import BASE_URL
from locators.demo_forms_locators import DemoFormsLocators


class DemoFormPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Open https://demoqa.com/automation-practice-form Page')
    def test_open_page(self):
        self.driver.get(BASE_URL + '/automation-practice-form')

    @allure.step('Enter first name')
    def enter_first_name(self, firstname):
        self.driver.find_element(*DemoFormsLocators.enter_first_name).send_keys(firstname)

    @allure.step('Enter Last name')
    def enter_last_name(self, lastname):
        self.driver.find_element(*DemoFormsLocators.enter_last_name).send_keys(lastname)

    @allure.step('Enter an Email address')
    def enter_email(self, email):
        self.driver.find_element(*DemoFormsLocators.enter_email).send_keys(email)

    @allure.step('Click on Radio button Male')
    def click_male_radio_button(self):
        self.driver.find_element(*DemoFormsLocators.click_male_radio_button).click()

    @allure.step('Enter Phone number')
    def enter_mobile(self, mobile):
        self.driver.find_element(*DemoFormsLocators.enter_mobile).send_keys(mobile)

    @allure.step('Select DOB')
    def select_dob(self):
        self.driver.find_element(*DemoFormsLocators.select_dob).click()

    @allure.step('Open months list')
    def select_month_list(self):
        self.driver.find_element(*DemoFormsLocators.select_month_list).click()

    @allure.step('Select month')
    def select_month(self):
        self.driver.find_element(*DemoFormsLocators.select_month).click()

    @allure.step('Selct day')
    def select_day(self):
        self.driver.find_element(*DemoFormsLocators.select_day).click()

    @allure.step('Enter Subject')
    def enter_subject(self, subject):
        self.driver.find_element(*DemoFormsLocators.enter_subject).send_keys(subject)
        self.driver.find_element(*DemoFormsLocators.enter_subject).send_keys(Keys.ARROW_DOWN)
        self.driver.find_element(*DemoFormsLocators.enter_subject).send_keys(Keys.RETURN)

    @allure.step('Click on Sports checkbox')
    def click_sports_checkbox(self):
        self.driver.find_element(*DemoFormsLocators.click_sports_checkbox).click()

    @allure.step('Add picture')
    def add_image(self, image):
        self.driver.find_element(*DemoFormsLocators.add_image).send_keys(image)

    @allure.step('Enter Current Address')
    def select_currentaddress_field(self):
        self.driver.find_element(*DemoFormsLocators.select_currentaddress_field).click()

    @allure.step('Enter Current Address')
    def input_current_address(self, currentaddress):
        self.driver.find_element(*DemoFormsLocators.enter_current_address).send_keys(currentaddress)

    @allure.step('Enter State')
    def enter_state(self, state):
        self.driver.find_element(*DemoFormsLocators.enter_state).send_keys(state)
        self.driver.find_element(*DemoFormsLocators.enter_state).send_keys(Keys.ENTER)

    @allure.step('Enter City')
    def enter_city(self, city):
        self.driver.find_element(*DemoFormsLocators.enter_city).send_keys(city)
        self.driver.find_element(*DemoFormsLocators.enter_city).send_keys(Keys.ENTER)

    @allure.step('scroll')
    def scroll(self):
        self.driver.find_element_by_tag_name('html').send_keys(Keys.END)

    @allure.step('click on the submit button')
    def click_submit_button(self):
        self.driver.find_element(*DemoFormsLocators.button_submit).click()

    @allure.step('Check text Student Name')
    def check_text_name(self):
        assert "'Mykola Petrov'"

    @allure.step('Check text Student Email')
    def check_email(self):
        assert "'example@gmail.com'"

    @allure.step('Check Gender male')
    def check_gender(self):
        assert "'Male'"

    @allure.step('Check Date of Birth')
    def check_dob(self):
        assert "'15 June,2021'"

    @allure.step('Subjects')
    def check_subject(self):
        assert "'English'"

    @allure.step('Check Hobbies')
    def check_hobbies(self):
        assert "'Sports'"

    @allure.step('Picture')
    def check_image(self):
        assert "'Allure Report - Google Chrome 2021-07-05 11.16.35.png'"

    @allure.step('Check Address')
    def check_address(self):
        assert "'56 Breakspears Rd, London SE4 1UL, UK'"

    @allure.step('State ans City')
    def check_state_city(self):
        assert "'5NCR Delhi'"
