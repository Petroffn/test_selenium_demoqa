import csv
import time

import allure
from pages.demo_forms_page import DemoFormPage


class TestDemoForm:
    @allure.title('Check demo form ')
    def test_demo_forms(self, driver):
        deomoform_page = DemoFormPage(driver)

        accounts = []
        with open('../testdata/demoform_test_data.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            for line in reader:
                accounts.append(line)
                print(accounts)

        firstname = (line[0])
        lastname = (line[1])
        email = (line[2])
        mobile = (line[3])
        subject = (line[4])
        currentaddress = (line[5])
        state = (line[6])
        city = (line[7])
        image = "../testdata/sample.jpeg"

        deomoform_page.test_open_page()
        deomoform_page.enter_first_name(firstname)
        deomoform_page.enter_last_name(lastname)
        deomoform_page.enter_email(email)
        deomoform_page.click_male_radio_button()
        deomoform_page.enter_mobile(mobile)
        deomoform_page.select_dob()
        deomoform_page.select_month_list()
        deomoform_page.select_month()
        deomoform_page.select_day()
        deomoform_page.enter_subject(subject)
        deomoform_page.click_sports_checkbox()
        #deomoform_page.add_image(image)
        deomoform_page.select_currentaddress_field()
        deomoform_page.input_current_address(currentaddress)
        deomoform_page.enter_state(state)
        deomoform_page.enter_city(city)
