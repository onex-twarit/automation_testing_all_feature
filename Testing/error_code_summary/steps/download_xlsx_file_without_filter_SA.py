from behave import *
import time
from selenium.webdriver.common.by import By


@then('go to Report')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "menu_master_report")
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Download Data tab SA')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.XPATH, "//a[text()='Download Data']")
    context.driver.execute_script("arguments[0].click();", button)
