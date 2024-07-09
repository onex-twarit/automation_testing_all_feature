from behave import *
import time
from selenium.webdriver.common.by import By


@then('go to SMPP')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="menu_smpps_view"]/p')  # go to SMPP
    context.driver.execute_script("arguments[0].click();", button)


@then('go to SMPP tab, click on search button')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/ul/li[1]').click()  # go to SMPP tab

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="search_rule_type"]')  # click on search button
    context.driver.execute_script("arguments[0].click();", button)


@then('error label \'No Record found\' will come')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="smpps_view_table"]/span').text

    if text == "No Record found":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"
