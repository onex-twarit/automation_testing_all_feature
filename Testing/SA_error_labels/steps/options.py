from behave import *
import time
from selenium.webdriver.common.by import By


@then('go to Options, go to carrier tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="menu_option"]/p')  # go to Options
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="option_carrier"]').click()  # go to carrier tab


@then('click on show carrier button, error label \'no data exist\' should come')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="show_data"]')  # click on show carrier button
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign"]/div[2]').text

    if text == "No Data Exist":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"


@then('go to vendor tab,')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="option_vendor"]').click()  # go to vendor tab


@then('click on show vendor button, error label \'no data exist\' should come')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="show_data"]')  # click on show vendor button
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign"]/div[2]').text

    if text == "No Data Exist":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"


@then('go to circle tab,')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="option_circle"]').click()  # go to circle tab


@then('click on show circle button, error label \'no data exist\' should come')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="show_data"]')  # click on show circle button
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="tab_content"]').text

    if text == "No Data Exist":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"


@then('go to type tab,')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="option_type"]').click()  # go to type tab


@then('click on show type button, error label \'no data exist\' should come')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="show_data"]')  # click on show type button
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign"]/div[2]').text

    if text == "No Data Exist":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"
