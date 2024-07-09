from behave import *
import time
from selenium.webdriver.common.by import By


@then('click on API')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'api_tab').click()  # click on api


@then('enter unicode in sender ID field for api')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'api_senderid').send_keys("समाचार")  # # sender ID


@then('verify error label \'No report data avaialable\' for api')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.ID, 'mis_api_table_panel').text
    if text == "No report data avaialable":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('clear sender ID field for api')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'api_senderid').clear()  # clear sender ID


@then('enter unicode in API Key field for api')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'apikey').send_keys("समाचार")  # API key


@then('clear API Key field for api')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'apikey').clear()  # clear API key


@then('enter unicode in Campaign Name field for api')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'apicamp').send_keys("समाचार")  # Campaign Name


@then('clear Campaign Name field for api')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'apicamp').clear()  # clear Campaign Name


@then('enter unicode in Template ID field for api')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'templateid').send_keys("समाचार")  # Template ID


@then('clear Template ID field for api')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'templateid').clear()  # clear Template ID
