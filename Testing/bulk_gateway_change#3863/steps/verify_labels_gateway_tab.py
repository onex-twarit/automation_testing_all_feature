from behave import *
import time
from selenium.webdriver.common.by import By


@then('go to HUB')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_hub')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Gateway tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'gateway_view')
    context.driver.execute_script("arguments[0].click();", button)


@then('verify Gateway, SMPPC, Routing, Default Gateway headers are present')
def step_impl(context):
    # Gateway label
    time.sleep(1)
    text = context.driver.find_element(By.ID, 'gateway_view').text
    if text == "Gateway":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"

    # SMPPC label
    time.sleep(1)
    text = context.driver.find_element(By.ID, 'smppc_view').text
    if text == "SMPPC":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"

    # Routing label
    time.sleep(1)
    text = context.driver.find_element(By.ID, 'routing_view').text
    if text == "Routing":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"

    # Default Gateway label
    time.sleep(1)
    text = context.driver.find_element(By.ID, 'default_gateway').text
    if text == "Default Gateway":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"


@then('verify the labels for the dropdowns(carrier, circle, gateways ID)')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign"]/div[1]/div[1]/div[1]/label').text
    if text == "Carrier":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"

    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign"]/div[1]/div[1]/div[2]/label').text
    if text == "Circle":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"

    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign"]/div[1]/div[1]/div[3]/label').text
    if text == "Gateway ID":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"


@then('verify the button show, reset add gateway are present')
def step_impl(context):
    # show button present
    time.sleep(1)
    text = context.driver.find_element(By.ID, 'apply_filter').is_displayed()
    if text:
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"

    # reset button present
    time.sleep(1)
    text = context.driver.find_element(By.ID, 'reset_btn').is_displayed()
    if text:
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"

    # add gateway button present
    time.sleep(1)
    text = context.driver.find_element(By.ID, 'create_gateway').is_displayed()
    if text:
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"
