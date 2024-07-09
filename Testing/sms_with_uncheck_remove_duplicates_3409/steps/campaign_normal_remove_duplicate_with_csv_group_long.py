from behave import *
import time
from selenium.webdriver.common.by import By


@then('check valid numbers on confirmation window for group long template campaign')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       "//label[text()='Valid Numbers'][1]/following-sibling::div/p").text
    if text == "5":
        assert True, "Test passed"
    else:
        assert False, "Test failed"
