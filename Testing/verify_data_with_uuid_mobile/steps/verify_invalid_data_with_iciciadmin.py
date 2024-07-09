from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then(u'select filter as mobile, send invalid data(sales)')
def step_impl(context):
    time.sleep(1)
    select = Select(context.driver.find_element(By.ID, "select_filter"))
    select.select_by_visible_text('Mobile')

    time.sleep(1)
    context.driver.find_element(By.ID, "number").send_keys("6262923191")


@then(u'verify invalid data')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="tablePanel"]/p').text
    if text == "No data found":
        assert True, "Test Passed"
    else:
        assert False, "verify invalid data --->> Failed"


@then(u'select filter as sender ID with mobile, send invalid data(sales)')
def step_impl(context):
    time.sleep(1)
    select = Select(context.driver.find_element(By.ID, "select_filter"))
    select.select_by_visible_text('Sender ID with Mobile')

    time.sleep(1)
    context.driver.find_element(By.ID, "number").send_keys("6262923191")
    time.sleep(1)
    context.driver.find_element(By.ID, "sender_id").send_keys("123456")
