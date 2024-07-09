from behave import *
import time
from selenium.webdriver.common.by import By


@then('click on download button')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, "dropdownMenuLink")
    context.driver.execute_script("arguments[0].click();", button)


@then('click on download CSV')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "download_csv")
    context.driver.execute_script("arguments[0].click();", button)


@then('verify the label on the pop up \'Your Download Request Received!\'')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.ID, 'download_option_download_req_text').text
    if text == "Your Download Request Received!":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"


@then('click on OK')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, "okay")
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Reports')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'menu_report')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Download Data tab')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'pills-download-data-tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on download')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.XPATH, '//*[@id="report_download"]/img')
    context.driver.execute_script("arguments[0].click();", button)
