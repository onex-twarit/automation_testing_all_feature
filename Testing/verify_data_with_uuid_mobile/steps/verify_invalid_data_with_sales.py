from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then(u'go to search tab select loanuser TUC')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "pills-search-tab")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    context.driver.find_element(By.ID, "tuc-report").send_keys("loanuser(2026)")


@then(u'select filter as mobile, send invalid data(loanuser)')
def step_impl(context):
    time.sleep(1)
    select = Select(context.driver.find_element(By.ID, "select_filter"))
    select.select_by_visible_text('Mobile')

    time.sleep(1)
    context.driver.find_element(By.ID, "number").send_keys("6262923190")


@then(u'select filter as sender ID with mobile, send invalid data(loanuser)')
def step_impl(context):
    time.sleep(1)
    select = Select(context.driver.find_element(By.ID, "select_filter"))
    select.select_by_visible_text('Sender ID with Mobile')

    time.sleep(1)
    context.driver.find_element(By.ID, "number").send_keys("6262923190")
    time.sleep(1)
    context.driver.find_element(By.ID, "sender_id").send_keys("123456")
