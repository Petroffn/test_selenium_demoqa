import allure


class TextBoxPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Open https://demoqa.com/text-box Page')
    def test_open_page(self):
        self.driver.get('https://demoqa.com/text-box')

    @allure.step('Select full name field')
    def select_first_name_field(self):
        self.driver.find_element_by_xpath('//li[@id="item-0"]').click()

    @allure.step('Enter First Name')
    def input_first_name(self, fullname):
        self.driver.find_element_by_xpath('//input[@placeholder="Full Name"]').send_keys(fullname)

    @allure.step('Select full name field')
    def select_first_email_field(self):
        self.driver.find_element_by_xpath('//input[@id="userEmail"]').click()

    @allure.step('Enter First Name')
    def input_email(self, email):
        self.driver.find_element_by_xpath('//input[@id="userEmail"]').send_keys(email)

    @allure.step('Enter Current Address')
    def input_current_address(self, currentaddress):
        self.driver.find_element_by_xpath('//textarea[@placeholder = "Current Address"]').send_keys(currentaddress)

    @allure.step('Enter Current Address')
    def input_permanent_address(self, permanentaddress):
        self.driver.find_element_by_xpath('//textarea[@id="permanentAddress"]').send_keys(permanentaddress)

    @allure.step('click on the submit button')
    def click_submit_button(self):
        self.driver.find_element_by_xpath('//button[@id="submit"]').click()

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
