from behave import *
from selenium.webdriver.common.by import By
import time


@then('go to campaign sms')
def go_to_campaign_sms(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'camp_sms_title')
    context.driver.execute_script("arguments[0].click();", button)


@then('upload campaign csv file')
def campaign_csv_file(context):
    time.sleep(0.5)
    context.driver.switch_to.frame("up_onex_file")
    fileupload = context.driver.find_element(By.ID, 'file1')
    fileupload.send_keys(
        '/home/twarit/Downloads/runTest_files (1)/runTest_files/campaign_dup10.csv')

