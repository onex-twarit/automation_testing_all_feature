from behave import *
import time
from selenium.webdriver.common.by import By


@then('click on schedule, then on schedule now button')
def click_sms_schedule(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'send')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    button = context.driver.find_element(By.ID, 'confirm_send_sms')
    context.driver.execute_script("arguments[0].click();", button)
