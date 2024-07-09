from behave import *
import time
from selenium.webdriver.common.by import By


@then('check DND numbers on confirmation window for group and recipients')
def dnd_numbers(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       "//label[text()='DND Numbers'][1]/following-sibling::div/p").text
    if text == "4":
        assert True, "Test passed"
    else:
        assert False, "Test failed"
