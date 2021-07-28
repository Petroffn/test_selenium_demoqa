import csv

import allure
from selenium.common.exceptions import NoSuchElementException
from pages.textbox_page import TextBoxPage


class TestTextBox:
    @allure.title('Check all fields')
    def test_open_page(self, driver):
        textbox_page = TextBoxPage(driver)

        accounts = []
        with open('testdata/testdata.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            for line in reader:
                accounts.append(line)
                print(accounts)

        fullname = (line[0])
        email = (line[3])
        currentaddress = (line[4])
        permanentaddress = (line[5])

        textbox_page.test_open_page()
        textbox_page.select_first_name_field()
        textbox_page.input_first_name(fullname)
        textbox_page.select_first_email_field()
        textbox_page.input_email(email)
        textbox_page.input_current_address(currentaddress)
        textbox_page.input_permanent_address(permanentaddress)
        textbox_page.click_submit_button()
        textbox_page.check_text_name()
        textbox_page.check_text_email()
        textbox_page.check_text_name()
        textbox_page.check_text_currentaddress()


