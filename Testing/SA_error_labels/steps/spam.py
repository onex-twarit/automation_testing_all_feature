from behave import *
import time
from selenium.webdriver.common.by import By


@then('go to Spam')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="menu_spam"]/p')  # go to spam
    context.driver.execute_script("arguments[0].click();", button)


@then('go to spam category tab, click on show category button')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[2]/div[2]/div[2]/ul/li[1]').click()  # go to spam category tab

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="show_spam_cat"]')  # click on show category button
    context.driver.execute_script("arguments[0].click();", button)


@then('error label \'No Data Available\' should come')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="tab_content"]').text

    if text == "No Data Available":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"


@then('go to keywords tab, click on search button')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="spam_keywords"]').click()  # go to keywords tab

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="search"]')  # click on search button
    context.driver.execute_script("arguments[0].click();", button)


@then('error label \'Please Select a valid category\' should come')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign"]/span').text

    if text == "Please Select a Category":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"


@then('go to spam unassign tab, click on show categories button')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="spam_unassign"]').click()  # go to spam unassign tab

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="show_unassign"]')  # click on show credits button
    context.driver.execute_script("arguments[0].click();", button)


@then('label \'No data available\' should come')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="spam_unassign_table_panel"]/b').text

    if text == "No Data Available":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"
