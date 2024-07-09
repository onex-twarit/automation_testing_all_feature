from behave import *
import time
from selenium.webdriver.common.by import By


@then('go to SMPP')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_smpps_view')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to SMPP tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'smpps_view')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on search SMPP')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'search_rule_type')
    context.driver.execute_script("arguments[0].click();", button)


@then('verify the reset bind button beside search')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.ID, 'reset_bind').is_displayed()
    if text == True:
        assert True, "Test passed"
    else:
        assert False, "Test failed, button missing"


@then('verify the reset bind button present under action in SMPP')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '//*[@id="smpps_view_table"]/table/tbody/tr[2]/td[7]/button/img').is_displayed()
    if text == True:
        assert True, "Test passed"
    else:
        assert False, "Test failed, button missing"


@then('click on the reset bind button')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'reset_bind')
    context.driver.execute_script("arguments[0].click();", button)


@then('verify the labels or headers on the pop-up')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="contact"]/div/div/div/p').text
    if text == "Are you sure want to reset all binds ?":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then('click on cancel button')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'cancel_modal')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on close to close the pop-up')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'close')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on proceed button')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'proceed')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to HUB')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_hub')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to SMPPC tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'smppc_view')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on search SMPPC')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'search_host')
    context.driver.execute_script("arguments[0].click();", button)


@then('verify the reset bind button present under action in SMPPC')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="reset_bind1004"]/img').is_displayed()
    if text == True:
        assert True, "Test passed"
    else:
        assert False, "Test failed, button missing"
