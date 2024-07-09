from behave import *
import time
from selenium.webdriver.common.by import By


@then('go to Analytics')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, "menu_analytics")
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Error Code Hourly tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, "error_code_summary_tab")
    context.driver.execute_script("arguments[0].click();", button)


@then('search on TUCs field with numeric input')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="pills-clicker-data"]/div[1]/div[1]/div[1]/input').send_keys("1234")


@then('click on search')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, "fetch_error_code_search_button")
    context.driver.execute_script("arguments[0].click();", button)


@then('verify the error label')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="pills-clicker-data"]/span').text
    if text == "Please enter a valid tuc":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"


@then('search on TUCs field with alpha-numeric input')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="pills-clicker-data"]/div[1]/div[1]/div[1]/input').clear()
    context.driver.find_element(By.XPATH, '//*[@id="pills-clicker-data"]/div[1]/div[1]/div[1]/input').send_keys(
        "abc1234")


@then('search on TUCs field with special-character input')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="pills-clicker-data"]/div[1]/div[1]/div[1]/input').clear()
    context.driver.find_element(By.XPATH, '//*[@id="pills-clicker-data"]/div[1]/div[1]/div[1]/input').send_keys(
        "@#$%^&&*()ABC123")


@then('log out from sa')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'dropdown-caret')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'log-out')
    context.driver.execute_script("arguments[0].click();", button)


@then('log out from ta')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'dropdown-caret')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'log-out')
    context.driver.execute_script("arguments[0].click();", button)
