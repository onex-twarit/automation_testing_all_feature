from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then('go to multiple dynamic sms')
def go_to_mul_dynamic(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'multi_dyn_sms_title')
    context.driver.execute_script("arguments[0].click();", button)


@then('upload multiple dynamic csv short file')
def mul_dynamic_csv_short_file(context):
    time.sleep(0.5)
    context.driver.switch_to.frame("up_onex_file")
    fileupload = context.driver.find_element(By.ID, 'file1')
    fileupload.send_keys(
        '/home/twarit/Downloads/runTest_files (1)/runTest_files/Multiple_Dynamic_Files/MDS_English_SMS.csv')


@then('select template content column')
def template_content_column(context):
    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, "template_content_column"))
    select.select_by_visible_text('Content/Template')


@then('check valid numbers on confirmation window for short template multiple dynamic')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       "//label[text()='Valid Numbers'][1]/following-sibling::div/p").text
    if text == "10":
        assert True, "Test passed"
    else:
        assert False, "Test failed"