from behave import *
import time
from selenium.webdriver.common.by import By


@then('go to Master Credits')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="menu_master_balance"]/p')  # go to Master credits
    context.driver.execute_script("arguments[0].click();", button)


@then('go to master credits tab, click on show credits button')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="pills-user-alloc"]').click()  # go to master credits tab

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="show_balance"]')  # click on show credits button
    context.driver.execute_script("arguments[0].click();", button)


@then('master credits should be \'0\'')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="current_balance"]').text

    if text == "0":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"


@then('go to super admin history tab, click on search button')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="pills-all-alloc"]').click()  # go to super admin history tab

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="search_alloc"]')  # click on search button
    context.driver.execute_script("arguments[0].click();", button)


@then('\'No data available\' error label should come')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign"]/div[2]/span').text

    if text == "No Data Available":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"
