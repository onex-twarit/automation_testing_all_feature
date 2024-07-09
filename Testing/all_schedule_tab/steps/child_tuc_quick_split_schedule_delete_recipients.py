from behave import *
import time
from pytz import timezone
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

current_time = datetime.datetime.now()
from datetime import datetime

now = datetime.now()


@then('check schedule sms, then on split schedule box, all schedule')
def step_impl(context):
    # click on schedule checkbox
    time.sleep(1)
    button = context.driver.find_element(By.NAME, "schedule_check")
    context.driver.execute_script("arguments[0].click();", button)

    # click on split into multiple campaign check box
    time.sleep(1)
    button = context.driver.find_element(By.NAME, "split_check")
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
    context.driver.find_element(By.XPATH,
                                "//div[contains(@class,'form-row row gx-0')][1]//label[text()='SMS Count'][1]/following-sibling::input").send_keys(
        "1")


@then('click on schedule, then on yes, schedule now button, all schedule')
def click_sms_schedule(context):
    # click on schedule button
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'send')
    context.driver.execute_script("arguments[0].click();", button)  # click on schedule button

    # click on yes on new warning pop-up
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'proceed')
    context.driver.execute_script("arguments[0].click();", button)  # click on yes warning button
    time.sleep(1)

    context.check_time = context.driver.find_element(By.XPATH,
                                                     "//td[contains(text(),'')]").text

    # click on schedule now button
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'confirm_send_sms')
    context.driver.execute_script("arguments[0].click();", button)  # click on schedule now button


@then('match the time of recent split scheduled sms and delete')
def step_impl(context):
    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH, f'//td[contains(text(),"{context.check_time}")]').text
    if text == context.check_time:
        time.sleep(0.5)
        button = context.driver.find_element(By.XPATH, "//button[contains(@id,'delete_button')]")
        context.driver.execute_script("arguments[0].click();", button)

        time.sleep(0.5)
        button = context.driver.find_element(By.ID, 'campaign_sms_confirm_delete_delete')
        context.driver.execute_script("arguments[0].click();", button)
    else:
        assert False, "----->> Failed"