from behave import *
import time
from pytz import timezone
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

current_time = datetime.datetime.now()
from datetime import datetime

now = datetime.now()


@then('add campaign \'campaign file group split schedule\', fill the present fields, click on Add')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, '//*[@id="add_campaign_button"]')
    context.driver.execute_script("arguments[0].click();",
                                  button)  # click on add campaign button on campaign name field

    time.sleep(1)
    context.driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/input').send_keys(
        "campaign file group split schedule")  # campaign name
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'campaign_desc').send_keys("Desc")  # description
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'add_campaign').click()  # click on add button


@then('search with campaign name \'campaign file group split schedule\'')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, 'web_camp').send_keys(
        'campaign file group split schedule')  # search with campaign name

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)  # click on search button


@then('verify with name \'campaign file group split schedule\'')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[3]/div/table/tbody/tr[2]/td[4]/div').text
    if text == 'campaign file group split schedule':
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('go to scheduled campaign, verify \'campaign file group split schedule\' name')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'pills-campaign-tab')
    context.driver.execute_script("arguments[0].click();", button)  # go to scheduled campaign tab

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)  # click on search button

    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/table/tbody/tr[2]/td[4]/div').text
    if text == "campaign file group split schedule":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"
