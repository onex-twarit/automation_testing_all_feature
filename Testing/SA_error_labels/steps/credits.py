from behave import *
import time
from selenium.webdriver.common.by import By


@then('go to Credits')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="menu_credit_allocation"]/p')  # go to credits
    context.driver.execute_script("arguments[0].click();", button)


@then('go to All allocation tab, click on search button')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="pills-all-alloc"]').click()  # go to All allocation tab

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="search_alloc"]')  # click on search button
    context.driver.execute_script("arguments[0].click();", button)


@then('error label \'No Credit Allocation Data Available\' should come')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign"]/div[2]/span').text

    if text == "No Credit Allocation Data Available":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"
