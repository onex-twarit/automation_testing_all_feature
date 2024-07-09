from behave import *
import time
from selenium.webdriver.common.by import By


@then('go to Analytics')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, "menu_analytics")
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Error Code Summary tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, "error_code_summary_datewise_tab")
    context.driver.execute_script("arguments[0].click();", button)


@then('verify TUC label')
def step_impl(context):
    # TUC label
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="pills-clicker-data"]/div[1]/div[1]/div[1]/label').text
    if text == "TUCs":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"


@then('verify Date labels')
def step_impl(context):
    # from
    time.sleep(1)
    text = context.driver.find_element(By.ID, 'error_date_label_A').text
    if text == "From":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"
    # to
    time.sleep(1)
    text = context.driver.find_element(By.ID, 'error_date_label_B').text
    if text == "To":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"


@then('verify Error Code label')
def step_impl(context):
    # error code label
    time.sleep(1)
    text = context.driver.find_element(By.ID, 'error_code_summary_label').text
    if text == "Error Code":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"


@then('verify search button')
def step_impl(context):
    # search button present
    time.sleep(1)
    text = context.driver.find_element(By.ID, 'fetch_error_code_search_button').is_displayed()
    if text == True:
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"
