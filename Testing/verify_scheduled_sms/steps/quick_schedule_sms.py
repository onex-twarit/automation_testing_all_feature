from behave import *
from selenium.webdriver.common.by import By
import time
from pytz import timezone
import datetime
from selenium.webdriver.support.select import Select

current_time = datetime.datetime.now()
from datetime import datetime

now = datetime.now()


@then('add campaign for schedule SMS')
def add_campaign_schedule_sms(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'add_campaign_button')
    context.driver.execute_script("arguments[0].click();",
                                  button)  # click on add campaign button on campaign name field

    time.sleep(0.5)
    context.driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/input').send_keys(
        "quick schedule")  # campaign name

    time.sleep(0.5)
    context.driver.find_element(By.ID, 'add_campaign').click()  # click on add button


@then('check schedule sms box')
def check_schedule_sms(context):
    time.sleep(2)
    button = context.driver.find_element(By.NAME, "schedule_check")
    context.driver.execute_script("arguments[0].click();", button)

    curr = datetime.now(timezone("Asia/Kolkata")).strftime("%H:%M:%S")
    print(curr)
    hours = curr[0:2]
    minutes = curr[3:5]
    print("Current Hour is:" + hours)
    print("Current Minute is:" + minutes)
    min = int(minutes)
    min = min + 17
    print(min)
    if min >= 60:
        val = min - 60
        if hours == "23":
            hours = str(00)
            print("Hour is:" + hours)
        else:
            hour = int(hours) + 1
            if hour < 10:
                hours = '0' + str(hour)
                print("Hour is:" + hours)
            else:
                hours = str(hour)
                print("Hour is:" + hours)
        if val <= 9:
            minutes = '0' + str(val)
            print("Minutes is:" + minutes)

        else:
            minutes = str(val)
            print("Minutes is:" + minutes)
    else:
        minutes = str(min)
        print(hours)
        print("Minutes is:" + minutes)
    time.sleep(1)
    select = Select(

        context.driver.find_element(By.XPATH, "//label[text()='Hour'][1]/following-sibling::select"))
    select.select_by_value(hours)
    time.sleep(1)
    select = Select(

        context.driver.find_element(By.XPATH, "//label[text()='Minute'][1]/following-sibling::select"))
    select.select_by_value(minutes)


@then('click on send, then send now')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'send')
    context.driver.execute_script("arguments[0].click();", button)  # click on send button

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'confirm_send_sms')
    context.driver.execute_script("arguments[0].click();", button)  # click on send now button


@then('click on New SMS')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'new_sms')
    context.driver.execute_script("arguments[0].click();", button)  # click on new sms button


@then('go to View Schedule tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign-summary-tab"]')
    context.driver.execute_script("arguments[0].click();", button)


@then('verify the schedule sms')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, "//td[contains(text(),'Schedule')]/following::td[2]").text
    if text == "123456":
        assert True, "Test Passed"
    else:
        assert False, "verify in view schedule tab-----> Failed"


@then('verify the quick schedule SMS')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, "//div[contains(text(),'quick schedule')]/following::td[3]").text
    if text == "Schedule":
        assert True, "Test Passed"
    else:
        assert False, "scheduled campaign -----> Failed"


@then('find the quick schedule campaign name and verify')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "//div[contains(text(),'quick schedule')]/following::td[3]").text
    if text == "Schedule":
        assert True, "Test Passed"
    else:
        assert False, "MIS(WEB) -----> Failed"
