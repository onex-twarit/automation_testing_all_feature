from behave import *
import time
from selenium.webdriver.common.by import By


@then('go to SMPPC tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'smppc_view')
    context.driver.execute_script("arguments[0].click();", button)


@then('verify the labels for the dropdowns(carrier, vendor, type, circle, gateways ID)')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign"]/div[1]/div/div[1]/label').text
    if text == "Carrier":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"

    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign"]/div[1]/div/div[2]/label').text
    if text == "Vendor":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"

    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign"]/div[1]/div/div[3]/label').text
    if text == "Type":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"

    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign"]/div[1]/div/div[4]/label').text
    if text == "Circle":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"

    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign"]/div[1]/div/div[5]/label').text
    if text == "Gateway ID":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"


@then('verify the button show, search, add SMPPC are present')
def step_impl(context):
    # show button present
    time.sleep(1)
    text = context.driver.find_element(By.ID, 'apply_filter').is_displayed()
    if text:
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"

    # search button present
    time.sleep(1)
    text = context.driver.find_element(By.ID, 'search_host').is_displayed()
    if text:
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"

    # add SMPPC button present
    time.sleep(1)
    text = context.driver.find_element(By.ID, 'create_smppc').is_displayed()
    if text:
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"

