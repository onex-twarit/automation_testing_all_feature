from behave import *
import time
from selenium.webdriver.common.by import By


@then('click on view all schedule')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'view_all_schedule')
    context.driver.execute_script("arguments[0].click();", button)


@then('verify present tuc search field')
def step_impl(context):
    time.sleep(0.5)
    text = context.driver.find_element(By.ID, 'get_tuc_dropdown_tucs_ids').text
    if text == "TUCs":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('verify limit box')
def step_impl(context):
    time.sleep(0.5)
    text = context.driver.find_element(By.ID, 'view_schedule_limit_label').is_displayed()
    if text == True:
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('verify search button')
def step_impl(context):
    time.sleep(0.5)
    text = context.driver.find_element(By.ID, 'search').is_displayed()
    if text == True:
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('verify delete all button')
def step_impl(context):
    time.sleep(0.5)
    text = context.driver.find_element(By.ID, 'delete_all_btn').is_displayed()
    if text == True:
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"
