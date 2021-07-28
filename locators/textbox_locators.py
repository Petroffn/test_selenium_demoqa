from selenium.webdriver.common.by import By


class TextBoxLocators:
    select_field_full_name = (By.ID, 'item-0')
    enter_full_name = (By.XPATH, '//input[@placeholder="Full Name"]')
    select_field_email_name = (By.ID, 'userEmail')
    enter_email = (By.ID, 'userEmail')
    enter_current_address = (By.ID, 'currentAddress')
    enter_permanent_address = (By.ID, 'permanentAddress')
    button_submit = (By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[1]/form/div[5]/div/button')
