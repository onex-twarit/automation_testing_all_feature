from behave import *
import time
from selenium.webdriver.common.by import By


@then('click on delete button on the scheduled sms')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'delete_all')
    context.driver.execute_script("arguments[0].click();", button)


@then('click within 15 min and verify the error label')
def step_impl(context):

@then('log out from child TUC')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'dropdown-caret')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'log-out')
    context.driver.execute_script("arguments[0].click();", button)



@then('match the time of the scheduled sms')
def step_impl(context):


@then('delete the entry from the TA')
def step_impl(context):
