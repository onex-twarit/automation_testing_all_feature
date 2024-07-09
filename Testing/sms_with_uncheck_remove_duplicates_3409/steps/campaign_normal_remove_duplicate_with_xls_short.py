from behave import *
from selenium.webdriver.common.by import By
import time


@then('upload campaign xls file')
def campaign_xls_file(context):
    time.sleep(0.5)
    context.driver.switch_to.frame("up_onex_file")
    fileupload = context.driver.find_element(By.ID, 'file1')
    fileupload.send_keys(
        '/home/twarit/Downloads/runTest_files (1)/runTest_files/campaign_dup10.xls')
