from behave import *
import time
from selenium.webdriver.common.by import By


@then('upload multiple dynamic xlsx file')
def upload_mul_dynamic_xlsx_file(context):
    time.sleep(0.5)
    context.driver.switch_to.frame("up_onex_file")
    fileupload = context.driver.find_element(By.ID, 'file1')
    fileupload.send_keys(
        '/home/twarit/Desktop/dnd_mds.xlsx')