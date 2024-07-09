from behave import *
import time
from selenium.webdriver.common.by import By


@then('add campaign \'split camp\', fill the present fields, click on Add')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="add_campaign_button"]')
    context.driver.execute_script("arguments[0].click();",
                                  button)  # click on add campaign button on campaign name field

    time.sleep(0.5)
    context.driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/input').send_keys(
        "split camp")  # campaign name
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'campaign_desc').send_keys("Desc")  # description
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'add_campaign').click()  # click on add button


@then('check schedule sms, split schedule for 1 hour')
def step_impl(context):
    time.sleep(1)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(1)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[6]/div[1]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # check schedule box

    time.sleep(1)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[6]/div[2]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # check split schedule box

    time.sleep(1)
    context.driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[7]/div[2]/div[1]/div[2]/div[1]/select').send_keys(
        18)

    time.sleep(1.5)
    context.driver.find_element(By.XPATH,
                                '//*[@id="sms_body"]/div[7]/div[2]/div[2]/input').send_keys(1)  # sms count


@then('click on schedule, then on yes, schedule now button')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'send')
    context.driver.execute_script("arguments[0].click();", button)  # click on schedule button

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'proceed')
    context.driver.execute_script("arguments[0].click();", button)  # click on yes warning button
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'confirm_send_sms')
    context.driver.execute_script("arguments[0].click();", button)  # click on schedule now button


@then('verify with name \'split camp\'')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[3]/div/table/tbody/tr[2]/td[4]/div').text
    if text == 'split camp':
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('go to scheduled campaign, verify \'split camp\' name')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, 'pills-campaign-tab')
    context.driver.execute_script("arguments[0].click();", button)  # go to scheduled campaign tab

    time.sleep(2)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)  # click on search button

    time.sleep(2)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/table/tbody/tr[2]/td[4]/div').text
    if text == "split camp":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"
