from behave import *
from selenium.webdriver.common.by import By
import time


@then('click on dynamic sms')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'dynamic_sms_title')
    context.driver.execute_script("arguments[0].click();", button)  # go to dynamic SMS


@then('upload dynamic file')
def step_impl(context):
    context.driver.switch_to.frame("up_onex_file")
    fileupload = context.driver.find_element(By.ID, 'file1')
    fileupload.send_keys('/home/twarit/Desktop/dynamic_sms.csv')
