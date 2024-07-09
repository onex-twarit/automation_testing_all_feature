from behave import *
import time
from selenium.webdriver.common.by import By


@then('go to error mapping tab')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="error-map-tab"]').click()  # go to error mapping tab


@then('click on show gateways button (error)')
def step_impl(context):

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_gateway')
    button.is_enabled()


@then('show gateways button should be disabled in one click (error)')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_gateway')
    context.driver.execute_script("arguments[0].click();", button)  # check button show gateways should be disabled
    button.get_property('disabled')


@then('click on show button (error)')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_tuc')
    button.is_enabled()  # check button is enabled


@then('it should be disabled in one click (error)')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_tuc')
    context.driver.execute_script("arguments[0].click();", button)  # check button should be disabled
    button.get_property('disabled')
