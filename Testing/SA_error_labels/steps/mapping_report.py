from behave import *
import time
from selenium.webdriver.common.by import By


@then('go to Mapping Report, go to userwise discounting tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="menu_mapping_report"]/p')  # go to Mapping report
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="userwise_discounting"]').click()  # go to userwise discounting tab


@then('click on search button, error label \'no data exists\' should come')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="search"]')  # click on search button
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign"]/div[4]/b').text

    if text == "No Data Exists":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"


@then('go to detailed discounting tab, click on search')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="detailed_discounting"]').click()  # go to detailed discounting tab

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="search"]')  # click on search button
    context.driver.execute_script("arguments[0].click();", button)


@then('error label \'no data exists\' should come')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign"]/div[4]/b').text

    if text == "No Data Exists":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"
