from behave import *
import time
from selenium.webdriver.common.by import By


@then('go to Settings, go to discounting mapping tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="menu_setting"]/p')  # go to Settings
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="discount-map-tab"]').click()  # go to discounting mapping tab


@then('click on show users button, error label \'no data exists\' should come')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="show-users"]')  # go to Settings
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign"]/div[2]/div/b').text

    if text == "No Data Exists":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"


@then('go to retry mapping tab, click on show retry gateways button')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="retry-map-tab"]').click()  # go to retry mapping tab

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="show_retry_gateway_btn"]')  # click on show retry gateways
    context.driver.execute_script("arguments[0].click();", button)


@then('error label \'no gateway data available\' should come')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign"]/div[2]').text

    if text == "No gateway data available":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"


@then('click on show retry users button, label \'No data available\' should come')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="show_retry_user_btn"]')  # click on show retry users
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign"]/div[2]').text

    if text == "No data available":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"


@then('go to backup gateway tab, label \'not able to get data\' should come')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="backup_gw_setting_tab"]').click()  # go to backup gateway tab

    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign"]/div/p').text

    if text == "Not able to get data":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"
