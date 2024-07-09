from behave import *
import time
from selenium.webdriver.common.by import By


@then('go to Routing, go to view rule tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="menu_routing"]/p')  # go to Routing
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="view_rule_tab"]').click()  # go to view rule tab


@then('click on search, \'record not found\' label should come')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="search_rule_type"]')  # click on search
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="error_label_text"]').text

    if text == "Record not found":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"
