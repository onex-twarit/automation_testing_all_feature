from behave import *
from selenium.webdriver.common.by import By


@then('upload dynamic xlsx short file')
def dynamic_xlsx_short_file(context):
    context.driver.switch_to.frame("up_onex_file")
    fileupload = context.driver.find_element(By.ID, 'file1')
    fileupload.send_keys(
        '/home/twarit/Downloads/runTest_files (1)/runTest_files/dynamic_file/valid_case/xlsx/english_short.xlsx')
