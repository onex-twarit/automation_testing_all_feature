from behave import *
import time
from selenium.webdriver.common.by import By


@then(u'check DND numbers on split confirmation window for group and recipients')
def dnd_numbers_recipients_group(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       "//label[text()='DND']/following-sibling::p[1]").text
    if text == "4":
        assert True, "Test passed"
    else:
        assert False, "Test failed"
