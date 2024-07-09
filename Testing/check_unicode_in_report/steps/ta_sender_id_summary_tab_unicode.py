from behave import *
import time
from selenium.webdriver.common.by import By


@then('click on Report, go to Sender ID summary tab')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="menu_report"]/p').click()  # click on report
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="pills-daily-summary-tab"]').click()  # go to Sender ID summary tab


@then('enter unicode in sender ID field for sender id summary tab')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'sender_id').send_keys("समाचार")  # sender ID


@then('verify error label \'No report data avaialable\' for sender id summary tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[4]/p').text
    if text == "No report data avaialable":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"
