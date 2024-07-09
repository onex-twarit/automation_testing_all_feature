from behave import *
import time
from selenium.webdriver.common.by import By


@then('click on delete all button')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'delete_all_btn')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on delete on warning window')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'delete_all')
    context.driver.execute_script("arguments[0].click();", button)
