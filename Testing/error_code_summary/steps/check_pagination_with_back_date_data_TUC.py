from datetime import date, timedelta
from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then('enter back in \'From Date\' and recent in \'To Date\'')
def step_impl(context):
    time.sleep(1)
    date_past = date.today() - timedelta(days=35)
    context.driver.find_element(By.ID, "date1").send_keys(date_past.strftime('%d/%m/%Y'))

    time.sleep(1)
    date_present = date.today()
    context.driver.find_element(By.ID, "date2").send_keys(date_present.strftime('%d/%m/%Y'))


@then('set rows limit to 5')
def step_impl(context):
    # change limit to 10
    time.sleep(0.5)
    set_limit = Select(context.driver.find_element(By.ID, 'page record_limit'))
    set_limit.select_by_visible_text("5")


@then('check pagination with limit 5')
def step_impl(context):
    time.sleep(1)
    element = context.driver.find_element(By.XPATH, "//table[@id='latency-report-table']")
    length = len(element.find_elements(By.TAG_NAME, "tr"))
    if length == 7:
        assert True, "---------->>  Pagination is working fine"
    else:
        assert False, "---------->>  Pagination Failed"


@then('set rows limit to 10')
def step_impl(context):
    # change limit to 10
    time.sleep(0.5)
    set_limit = Select(context.driver.find_element(By.ID, 'page record_limit'))
    set_limit.select_by_visible_text("10")


@then('check pagination with limit 10')
def step_impl(context):
    time.sleep(1)
    element = context.driver.find_element(By.XPATH, "//table[@id='latency-report-table']")
    length = len(element.find_elements(By.TAG_NAME, "tr"))
    if length == 12:
        assert True, "---------->>  Pagination is working fine"
    else:
        assert False, "---------->>  Pagination Failed"
