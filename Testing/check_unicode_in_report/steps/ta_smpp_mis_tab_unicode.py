from behave import *
import time
from selenium.webdriver.common.by import By


@then('click on SMPP')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'smpp_tab').click()  # click on web


@then('enter unicode in sender ID field for smpp')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'smpp_senderid').send_keys("समाचार")  # sender ID


@then('verify error label \'No report data avaialable\' for smpp')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.ID, 'mis_smpp_table_panel').text
    if text == "No report data avaialable":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('clear sender ID field for smpp')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'smpp_senderid').clear()  # clear sender ID


@then('enter unicode in SMPP ID field for smpp')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'smppid').send_keys("समाचार")  # SMPP ID


@then('clear SMPP ID field for smpp')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'smppid').clear()  # SMPP ID


@then('enter unicode in Template ID field for smpp')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'templateid').send_keys("समाचार")  # template ID


@then('clear Template ID field for smpp')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'templateid').clear()  # clear Template ID
