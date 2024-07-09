from behave import *
import time
from selenium.webdriver.common.by import By


@then('go to retry mapping tab')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="retry-map-tab"]').click()  # go to retry mapping tab


@then('click on show retry gateways button (retry)')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_retry_gateway_btn')
    button.is_enabled()  # button show retry gateways is enabled


@then('show retry gateways button should be disabled in one click (retry)')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_retry_gateway_btn')
    context.driver.execute_script("arguments[0].click();",
                                  button)  # check button show retry gateways should be disabled
    button.get_property('disabled')


@then('click on show button (retry)')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_retry_user_btn')
    button.is_enabled()  # button show retry users is enabled


@then('it should be disabled in one click (retry)')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_retry_user_btn')
    context.driver.execute_script("arguments[0].click();", button)  # check button should be disabled
    button.get_property('disabled')
