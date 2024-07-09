from behave import *
import time
from selenium.webdriver.common.by import By


@then('open dashboard')
def open_dashboard(context):
    # verify, opened page is a dashboard page
    time.sleep(0.5)
    text = context.driver.find_element(By.ID, 'dashboard_title').text
    if text == "Dashboard":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('verify \'All Schedule\' tab(left panel)')
def all_schedule_tab(context):
    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH, '//*[@id="menu_all_schedule"]/p').text
    if text == "All Schedule":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"
