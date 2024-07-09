from behave import *
import time
from selenium.webdriver.common.by import By


@then('go to DLT Rejected Count tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'dlt_rejected_count')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on search for dlt rejected counts')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'fetch_dlt_rejected_search_button')
    context.driver.execute_script("arguments[0].click();", button)


@then('verify the error label, dlt rejected counts')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="pills-clicker-data"]/span').text
    if text == "Please enter a valid TUC":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"
