from behave import *
import time
from selenium.webdriver.common.by import By


@then('add group')
def add_group(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'groupDropdown').send_keys("scrub dnd group(3)")  # adding group

