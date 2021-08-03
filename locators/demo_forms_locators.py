from selenium.webdriver.common.by import By


class DemoFormsLocators:
    enter_first_name = (By.ID, 'firstName')
    enter_last_name = (By.ID, 'lastName')
    enter_email = (By.ID, 'userEmail')
    click_male_radio_button = (By.XPATH, '//label[@for="gender-radio-1"]')
    enter_mobile = (By.ID, 'userNumber')
    select_dob = (By.ID, 'dateOfBirthInput')
    select_month_list = (By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[1]/form/div[5]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select')
    select_month = (By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[1]/form/div[5]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select/option[4]')
    select_day = (By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[1]/form/div[5]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div[5]')
    enter_subject = (By.ID, 'subjectsInput')
    click_sports_checkbox = (By.XPATH, '//*[@id="hobbies-checkbox-1"]')
    add_image = (By.XPATH, '//*[@id="uploadPicture"]')
    select_currentaddress_field = (By.ID, 'currentAddress')
    enter_current_address = (By.ID, 'currentAddress')
    enter_state = (By.ID, 'react-select-3-input')
    enter_city = (By.ID, 'react-select-4-input')
