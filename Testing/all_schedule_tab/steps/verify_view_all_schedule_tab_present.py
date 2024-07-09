from behave import *
import time
from selenium.webdriver.common.by import By


@then('click on All Schedule')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="menu_all_schedule"]/p')
    context.driver.execute_script("arguments[0].click();", button)


@then('verify \'View All Schedule\' tab present')
def step_impl(context):
    time.sleep(0.5)
    text = context.driver.find_element(By.ID, 'view_all_schedule').text
    if text == "View All Schedule":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"
