from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then('upload multiple dynamic csv file with temp id')
def step_impl(context):
    time.sleep(0.5)
    context.driver.switch_to.frame("up_onex_file")
    fileupload = context.driver.find_element(By.ID, 'file1')
    fileupload.send_keys(
        '/home/twarit/Desktop/dnd_mds_tempid.csv')


@then('select template ID column')
def step_impl(context):
    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, 'templateid_column'))
    select.select_by_visible_text('Template ID')
