from behave import *
import time
from selenium.webdriver.common.by import By


@then('add group')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'groupDropdown').send_keys("remove duplicates(2)")  # adding group


@then('check valid numbers on confirmation window for short template group')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       "//label[text()='Valid Numbers'][1]/following-sibling::div/p").text
    if text == "2":
        assert True, "Test passed"
    else:
        assert False, "Test failed"



