from behave import *
import time
from selenium.webdriver.common.by import By


@then('upload multiple dynamic csv long file')
def mul_dynamic_csv_long_file(context):
    time.sleep(0.5)
    context.driver.switch_to.frame("up_onex_file")
    fileupload = context.driver.find_element(By.ID, 'file1')
    fileupload.send_keys(
        '/home/twarit/Downloads/runTest_files (1)/runTest_files/Multiple_Dynamic_Files/MDS_English_Long_SMS.csv')


@then('check valid numbers on confirmation window for long template multiple dynamic')
def step_impl(context):
    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH,
                                       "//label[text()='Valid Numbers'][1]/following-sibling::div/p").text
    if text == "10":
        assert True, "Test passed"
    else:
        assert False, "Test failed"
