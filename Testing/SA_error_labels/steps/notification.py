from behave import *
import time
from selenium.webdriver.common.by import By


@then('go to Notification, click on show notification button')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="menu_notification"]/p')  # go to notification
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="show_notification"]')  # click on show notification button
    context.driver.execute_script("arguments[0].click();", button)


@then('label \'No Record Found\' should come')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="idtable"]').text

    if text == "No Record Found":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"
