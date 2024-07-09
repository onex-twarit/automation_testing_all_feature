from behave import *
from selenium.webdriver.common.by import By
import time


@then('click on campaign sms')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'camp_sms_title')
    context.driver.execute_script("arguments[0].click();", button)  # go to campaign SMS


@then('upload campaign file')
def step_impl(context):
    context.driver.switch_to.frame("up_onex_file")
    fileupload = context.driver.find_element(By.ID, 'file1')
    fileupload.send_keys('/home/twarit/Desktop/campaign_sms.csv')
