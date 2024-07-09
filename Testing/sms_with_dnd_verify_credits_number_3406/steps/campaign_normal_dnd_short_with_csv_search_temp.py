from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then('go to campaign sms')
def go_to_campaign_name(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'camp_sms_title')
    context.driver.execute_script("arguments[0].click();", button)


@then('upload campaign csv file')
def upload_campaign_csv_file(context):
    time.sleep(0.5)
    context.driver.switch_to.frame("up_onex_file")
    fileupload = context.driver.find_element(By.ID, 'file1')
    fileupload.send_keys(
        '/home/twarit/Desktop/dnd_nums.csv')



