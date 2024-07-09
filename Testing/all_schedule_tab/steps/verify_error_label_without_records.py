from behave import *
import time
from selenium.webdriver.common.by import By


@then('click on search (without records)')
def step_impl(context):
    # click on search
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)


@then('verify error label \'No scheduled data found\'')
def step_impl(context):
    time.sleep(0.5)
    text = context.driver.find_element(By.ID, 'tuc_search_error').text
    if text == 'No scheduled data found':
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"
