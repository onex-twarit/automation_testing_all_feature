from behave import *
import time
from selenium.webdriver.common.by import By


@then('verify present delete all button is disabled')
def step_impl(context):
    time.sleep(0.5)
    check = context.driver.find_element(By.ID, 'delete_all_btn').is_enabled()
    if check == False:
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('verify its enabled after clicking on search button with records')
def step_impl(context):
    # click on search
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    check = context.driver.find_element(By.ID, 'delete_all_btn').is_enabled()
    if check == True:
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"
