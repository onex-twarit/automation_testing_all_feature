from behave import *
import time
from selenium.webdriver.common.by import By


@then('click on search')
def step_impl(context):
    # click on search
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)


@then('verify all the labels present in table')
def step_impl(context):
    # check tuc name label
    time.sleep(0.5)
    text = context.driver.find_element(By.ID, 'tuc_name_header').text
    if text == 'TUC Name':
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"

    # check type label
    time.sleep(0.5)
    text = context.driver.find_element(By.ID, 'type_header').text
    if text == 'Type':
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"

    # check sms type label
    time.sleep(0.5)
    text = context.driver.find_element(By.ID, 'sms_type_header').text
    if text == 'SMS Type':
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"

    # check schedule Id label
    time.sleep(0.5)
    text = context.driver.find_element(By.ID, 'schedule_id_header').text
    if text == 'Schedule ID':
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"

    # check sender ID label
    time.sleep(0.5)
    text = context.driver.find_element(By.ID, 'sender_id_header').text
    if text == 'Sender ID':
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"

    # check scheduled at label
    time.sleep(0.5)
    text = context.driver.find_element(By.ID, 'schedule_date_time_header').text
    if text == 'Scheduled At':
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"

    # check message label
    time.sleep(0.5)
    text = context.driver.find_element(By.ID, 'message_header').text
    if text == 'Message':
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"

    # check valid numbers label
    time.sleep(0.5)
    text = context.driver.find_element(By.ID, 'valid_nos_header').text
    if text == 'Valid Numbers':
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"

    # check message length label
    time.sleep(0.5)
    text = context.driver.find_element(By.ID, 'message_len_header').text
    if text == 'Message Length':
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"

    # check credits label
    time.sleep(0.5)
    text = context.driver.find_element(By.ID, 'credits_header').text
    if text == 'Credits':
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"

    # check status label
    time.sleep(0.5)
    text = context.driver.find_element(By.ID, 'status_header').text
    if text == 'Status':
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"

    # check action label
    time.sleep(0.5)
    text = context.driver.find_element(By.ID, 'action_header').text
    if text == 'Action':
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


