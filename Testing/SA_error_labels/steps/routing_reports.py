from behave import *
import time
from selenium.webdriver.common.by import By


@then('go to Routing Reports')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="menu_routing_report"]/p')  # go to routing reports tab
    context.driver.execute_script("arguments[0].click();", button)


@then('go to TUC Details tab, \'TUC doesn\'t exists\' error label should come')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="gateway_search"]').click()  # go to TUC details tab

    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign"]/div[1]/div/p').text

    if text == "TUC doesn't exixts":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"


@then('go to gateway details tab, click on search')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="tuc_search"]').click()  # go to gateway details tab

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="search"]')  # click on search button
    context.driver.execute_script("arguments[0].click();", button)


@then('error label should come for SMPPC and TUC using gateway')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign"]/div[2]/div').text

    if text == "Smppc for Gateway\nNo Data Exists":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"

    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign"]/div[3]/div').text

    if text == "Tucs using Gateway\nNo Data Exists":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"
