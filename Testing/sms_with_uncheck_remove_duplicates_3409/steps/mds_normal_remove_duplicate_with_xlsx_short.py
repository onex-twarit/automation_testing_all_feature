from behave import *
import time
from selenium.webdriver.common.by import By


@then('upload multiple dynamic xlsx short file')
def step_impl(context):
    time.sleep(0.5)
    context.driver.switch_to.frame("up_onex_file")
    fileupload = context.driver.find_element(By.ID, 'file1')
    fileupload.send_keys(
        '/home/twarit/Downloads/runTest_files (1)/runTest_files/Multiple_Dynamic_Files/MDS_English_SMS.xlsx')
