from behave import *
from selenium.webdriver.common.by import By
import time
from pytz import timezone
import datetime
from selenium.webdriver.support.select import Select

current_time = datetime.datetime.now()
from datetime import datetime

now = datetime.now()


@then('check split sms')
def split_sms(context):
    time.sleep(1)
    button = context.driver.find_element(By.NAME, 'schedule_check')
    context.driver.execute_script("arguments[0].click();", button)  # check schedule box
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


@then('then on click on Yes')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'proceed')
    context.driver.execute_script("arguments[0].click();", button)  # click on yes warning button


@then('check DND numbers on split confirmation window')
def dnd_numbers(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       "//label[text()='DND']/following-sibling::p[1]").text
    if text == "2":
        assert True, "Test passed"
    else:
        assert False, "Test failed"


@then('total required SMS credits on split confirmation window')
def total_required_credits(context):
    time.sleep(1)
    context.credits = context.driver.find_element(By.XPATH,
                                                  "//th[text()='Totals']/following-sibling::th[2]").text


@then('verify deducted credits split')
def verify_deducted_credits(context):
    # verifying the credits
    time.sleep(1)
    new_avail_bal = context.driver.find_element(By.XPATH, '//*[@id="available_credits"]').text
    context.new_avail_balance = int(str(new_avail_bal).replace(",", ""))

    assert context.available_bal == int(context.credits) + context.new_avail_balance
