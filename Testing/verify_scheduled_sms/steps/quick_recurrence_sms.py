from behave import *
import time
from datetime import date, timedelta
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

current_time = datetime.datetime.now()
from datetime import datetime

now = datetime.now()


@then('add campaign for recurrence SMS')
def add_campaign_recurrence_sms(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'add_campaign_button')
    context.driver.execute_script("arguments[0].click();",
                                  button)  # click on add campaign button on campaign name field

    time.sleep(0.5)
    context.driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/input').send_keys(
        "quick recurrence")  # campaign name

    time.sleep(0.5)
    context.driver.find_element(By.ID, 'add_campaign').click()  # click on add button


@then('check recurrence')
def check_recurrence(context):
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
    date_present = date.today() + timedelta(days=2)
    context.driver.find_element(By.ID, "date2").send_keys(date_present.strftime('%d/%m/%Y'))

    time.sleep(1)
    fill_time = datetime.now() + timedelta(minutes=65)
    select = Select(context.driver.find_element(By.ID, 'recurrence_hour'))
    select.select_by_visible_text((fill_time + timedelta(minutes=1)).strftime('%H'))

    time.sleep(1)
    fill_time = datetime.now() + timedelta(minutes=30)
    select = Select(context.driver.find_element(By.ID, 'recurrence_minute'))
    select.select_by_visible_text((fill_time + timedelta(minutes=1)).strftime('%M'))


@then('click on schedule, then on schedule now button')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'send')
    context.driver.execute_script("arguments[0].click();", button)  # click on schedule button

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'confirm_send_sms')
    context.driver.execute_script("arguments[0].click();", button)  # click on schedule now button


@then('verify the recurrence sms')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, "//td[contains(text(),'Recurrence')]/following::td[2]").text
    if text == "123456":
        assert True, "Test Passed"
    else:
        assert False, "verify in view schedule tab-----> Failed"


@then('verify the quick recurrence SMS')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, "//div[contains(text(),'quick recurrence')]/following::td[3]").text
    if text == "Recurrence":
        assert True, "Test Passed"
    else:
        assert False, "scheduled campaign -----> Failed"


@then('find the quick recurrence campaign name and verify')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "//div[contains(text(),'quick recurrence')]/following::td[3]").text
    if text == "Recurrence":
        assert True, "Test Passed"
    else:
        assert False, "MIS(WEB) -----> Failed"
