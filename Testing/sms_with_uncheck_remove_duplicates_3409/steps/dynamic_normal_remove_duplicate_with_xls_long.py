from behave import *
import time
from selenium.webdriver.common.by import By


@then('upload dynamic xls long file')
def dynamic_xls_long_file(context):
    time.sleep(1)
    context.driver.switch_to.frame("up_onex_file")
    fileupload = context.driver.find_element(By.ID, 'file1')
    fileupload.send_keys(
        '/home/twarit/Downloads/runTest_files (1)/runTest_files/dynamic_file/valid_case/xls/english_long.xls')
