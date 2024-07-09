from behave import *
import time
from datetime import date, timedelta
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

current_time = datetime.datetime.now()
from datetime import datetime

now = datetime.now()


@then('add campaign \'campaign recurrence\', fill the present fields, click on Add')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, 'add_campaign_button')
    context.driver.execute_script("arguments[0].click();",
                                  button)  # click on add campaign button on campaign name field

    time.sleep(1)
    context.driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/input').send_keys(
        "campaign recurrence")  # campaign name
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'campaign_desc').send_keys("Desc")  # description
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'add_campaign').click()  # click on add button


@then('check recurrence')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.NAME, 'recurrence_check')
    context.driver.execute_script("arguments[0].click();", button)  # check schedule box

    time.sleep(1)
    recurrence = context.driver.find_element(By.ID, "repetation_type_dropdown")
    select = Select(recurrence)
    select.select_by_visible_text("Daily")

    time.sleep(1)
    date_past = date.today()
    context.driver.find_element(By.ID, "date1").send_keys(date_past.strftime('%d/%m/%Y'))

    time.sleep(1)
    date_present = date.today() + timedelta(days=10)
    context.driver.find_element(By.ID, "date2").send_keys(date_present.strftime('%d/%m/%Y'))

    time.sleep(1)
    fill_time = datetime.now() + timedelta(minutes=65)
    select = Select(context.driver.find_element(By.ID, 'recurrence_hour'))
    select.select_by_visible_text((fill_time + timedelta(minutes=1)).strftime('%H'))

    time.sleep(1)
    fill_time = datetime.now() + timedelta(minutes=30)
    select = Select(context.driver.find_element(By.ID, 'recurrence_minute'))
    select.select_by_visible_text((fill_time + timedelta(minutes=1)).strftime('%M'))


@then('search with campaign name \'campaign recurrence\'')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, 'web_camp').send_keys('campaign recurrence')  # search with campaign name

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)  # click on search button


@then('verify with name \'campaign recurrence\'')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[3]/div/table/tbody/tr[2]/td[4]/div').text
    if text == 'campaign recurrence':
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('go to scheduled campaign, verify \'campaign recurrence\' name')
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
    if text == "campaign recurrence":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"

