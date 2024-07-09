from behave import *
import time
from selenium.webdriver.common.by import By


@then('go to Latency Hour-Wise Report tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, "latency_hour_report")
    context.driver.execute_script("arguments[0].click();", button)


@then('click on search, latency hour')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, "search")
    context.driver.execute_script("arguments[0].click();", button)


@then('verify the error label, latency hour')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="summary_stat_panel_para"]/b').text
    if text == "Please select a Valid TUC":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"


@then('search on TUCs field with numeric input, latency hour')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, 'tuc-report').send_keys("1234")


@then('search on TUCs field with alpha-numeric input, latency hour')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, 'tuc-report').clear()
    context.driver.find_element(By.ID, 'tuc-report').send_keys("abc1234")


@then('search on TUCs field with special-character input, latency hour')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, 'tuc-report').clear()
    context.driver.find_element(By.ID, 'tuc-report').send_keys("@#$%^&&*()ABC123")
