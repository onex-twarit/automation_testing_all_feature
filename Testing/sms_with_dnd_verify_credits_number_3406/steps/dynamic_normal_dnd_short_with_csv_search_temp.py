from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then('go to dynamic sms')
def go_to_dynamic_sms(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'dynamic_sms_title')
    context.driver.execute_script("arguments[0].click();", button)


@then('upload dynamic csv file')
def upload_dynamic_csv_file(context):
    time.sleep(0.5)
    context.driver.switch_to.frame("up_onex_file")
    fileupload = context.driver.find_element(By.ID, 'file1')
    fileupload.send_keys(
        '/home/twarit/Desktop/dnd_dynamic.csv')


@then('select recipient column')
def select_recipient_column(context):
    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, "recipient_column"))
    select.select_by_visible_text('Mobile')


@then('select variable column')
def select_variable_column(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="dynamic_columns_panel"]/div/div/div[1]/ul/li[2]').click()

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="dynamic_columns_panel"]/div/div/div[2]/button[1]').click()
