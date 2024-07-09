from behave import *
import time
from selenium.webdriver.common.by import By


@then('add group')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'groupDropdown').send_keys("twarit group(22)")  # adding group
