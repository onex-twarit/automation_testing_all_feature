from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then('go to dynamic sms')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'dynamic_sms_title')
    context.driver.execute_script("arguments[0].click();", button)


@then('upload dynamic csv short file')
def step_impl(context):
    time.sleep(0.5)
    context.driver.switch_to.frame("up_onex_file")
    fileupload = context.driver.find_element(By.ID, 'file1')
    fileupload.send_keys(
        '/home/twarit/Downloads/runTest_files (1)/runTest_files/dynamic_file/valid_case/csv/english_short.csv')


@then('select recipient column')
def step_impl(context):
    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, "recipient_column"))
    select.select_by_visible_text('Mobile')


@then('select variable column')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="dynamic_columns_panel"]/div/div/div[1]/ul/li[2]').click()

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="dynamic_columns_panel"]/div/div/div[2]/button[1]').click()


@then('check valid numbers on confirmation window for short template dynamic')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       "//label[text()='Valid Numbers'][1]/following-sibling::div/p").text
    if text == "10":
        assert True, "Test passed"
    else:
        assert False, "Test failed"
