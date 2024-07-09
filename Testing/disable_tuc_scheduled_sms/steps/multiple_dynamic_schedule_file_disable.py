from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


@then('click on multiple dynamic sms')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'multi_dyn_sms_title')
    context.driver.execute_script("arguments[0].click();", button)  # go to multiple dynamic SMS


@then('upload multiple dynamic file')
def step_impl(context):
    context.driver.switch_to.frame("up_onex_file")
    fileupload = context.driver.find_element(By.ID, 'file1')
    fileupload.send_keys('/home/twarit/Desktop/multiple_dynamic_sms.csv')


@then('select column for recipients and template content')
def step_impl(context):
    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, 'recipient_column'))
    select.select_by_visible_text('Mobile')

    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, 'template_content_column'))
    select.select_by_visible_text('Content/Template')
