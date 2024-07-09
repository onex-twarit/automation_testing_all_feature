from behave import *
import time
from selenium.webdriver.common.by import By


@then('upload dynamic csv long file')
def dynamic_csv_long_file(context):
    context.driver.switch_to.frame("up_onex_file")
    fileupload = context.driver.find_element(By.ID, 'file1')
    fileupload.send_keys(
        '/home/twarit/Downloads/runTest_files (1)/runTest_files/dynamic_file/valid_case/csv/english_long.csv')


@then('check valid numbers on confirmation window for long template dynamic')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       "//label[text()='Valid Numbers'][1]/following-sibling::div/p").text
    if text == "10":
        assert True, "Test passed"
    else:
        assert False, "Test failed"
