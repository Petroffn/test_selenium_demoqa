from selenium.webdriver.common.by import By


class TestRadioLocators:
    click_on_yes_button = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[2]/label')
    check_yes_button = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/p/span')
    click_on_impressive_butto = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[3]/label')
    check_impressive_button = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/p/span')
