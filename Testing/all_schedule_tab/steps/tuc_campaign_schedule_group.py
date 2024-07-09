from behave import *
from selenium.webdriver.common.by import By
import time


@then('add group for campaign, for tuc')
def step_impl(context):
    time.sleep(0.5)

    context.driver.find_element(By.ID, 'groupDropdownCamp').send_keys("group one(1)")  # adding group

