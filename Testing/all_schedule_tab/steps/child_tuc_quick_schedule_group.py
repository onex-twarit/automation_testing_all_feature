from behave import *
import time
from selenium.webdriver.common.by import By
import datetime

current_time = datetime.datetime.now()
from datetime import datetime

now = datetime.now()


@then('add group, all schedule')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'groupDropdown').send_keys("twarit group(22)")  # adding group

