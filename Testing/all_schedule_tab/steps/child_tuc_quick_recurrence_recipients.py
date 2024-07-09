from datetime import date, timedelta
from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import datetime

current_time = datetime.datetime.now()
from datetime import datetime

now = datetime.now()


@then('check recurrence box, all schedule')
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

