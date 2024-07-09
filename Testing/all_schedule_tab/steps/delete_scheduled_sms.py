from behave import *
import time
from selenium.webdriver.common.by import By


@then('delete the scheduled sms')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'delete_button_3711')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'campaign_sms_confirm_delete_delete')
    context.driver.execute_script("arguments[0].click();", button)
