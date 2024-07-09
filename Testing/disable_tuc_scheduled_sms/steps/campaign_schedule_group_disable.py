from behave import *
from selenium.webdriver.common.by import By
import time


@then('add group campaign')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'groupDropdownCamp').send_keys("twarit group(22)")  # adding group in campaign sms

