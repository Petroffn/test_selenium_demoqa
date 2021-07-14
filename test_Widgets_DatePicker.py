import allure
from allure_commons.types import Severity
from selenium import webdriver



@allure.title('Test')
@allure.severity(Severity.BLOCKER)

def test_Widgets_DP_01():
    driver = webdriver.Chrome()
    with allure.step('Open Data Picker page'):
        driver.get('https://demoqa.com/date-picker')
        driver.set_window_size(1920, 1080)

    import time
    time.sleep(3)

    with allure.step('Select data'):
        datefield = driver.find_element_by_id("datePickerMonthYearInput")
        datefield.click()

        years = driver.find_elements_by_css_selector("select[class*='year-select'] option")
        for year in years:
            if year.text == "2000":
                year.click()
                time.sleep(5)
                break

        months = driver.find_elements_by_css_selector("select[class*='month-select'] option")
        for month in months:
            if month.text == "June":
                month.click()
                time.sleep(5)
                break

        days = driver.find_elements_by_css_selector("div[class*='datepicker__day']")
        for day in days:
            if day.text == "15":
                day.click()
                break

def test_Widgets_DP_02():
    driver = webdriver.Chrome()
    with allure.step('Open Data Picker page'):
        driver.get('https://demoqa.com/date-picker')
        driver.set_window_size(1920, 1080)

    import time
    time.sleep(3)

    with allure.step('Select data and time'):
        datefield = driver.find_element_by_id("dateAndTimePickerInput")
        datefield.click()

        years = driver.find_elements_by_css_selector("select[class*='year-select'] option")
        for year in years:
            if year.text == "2000":
                year.click()
                time.sleep(5)
                break

        months = driver.find_elements_by_css_selector("select[class*='month-select'] option")
        for month in months:
            if month.text == "June":
                month.click()
                time.sleep(5)
                break

        days = driver.find_elements_by_css_selector("div[class*='datepicker__day']")
        for day in days:
            if day.text == "15":
                day.click()
                time.sleep(5)
                break

        times = driver.find_elements_by_css_selector("div[class*='time__header']")
        for time in times:
            if time.text == "15:15":
                day.click()
                time.sleep(5)
                break