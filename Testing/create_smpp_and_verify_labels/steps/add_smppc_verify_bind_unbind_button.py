from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then('click on add SMPPC button')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, "create_smppc")
    context.driver.execute_script("arguments[0].click();", button)


@then('fill the presents fields for smppc')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, "name").send_keys("smppc auto")

    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, "carrier_id"))
    select.select_by_visible_text("carrier one")

    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, "vendor"))
    select.select_by_visible_text("vendor one")

    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, "accounttype"))
    select.select_by_visible_text("Service Implicit")

    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, "circle_id"))
    select.select_by_visible_text("circle one")

    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, "gateway_id"))
    select.select_by_visible_text("gatewaysChild")

    time.sleep(0.5)
    context.driver.find_element(By.ID, "smpplogin").send_keys("abcde")

    time.sleep(0.5)
    context.driver.find_element(By.ID, "username").send_keys("username")

    time.sleep(0.5)
    context.driver.find_element(By.ID, "password").send_keys("abcde")

    time.sleep(0.5)
    context.driver.find_element(By.ID, "host").send_keys("127.0.0.1")

    time.sleep(0.5)
    context.driver.find_element(By.ID, "port").send_keys("9000")

    time.sleep(0.5)
    context.driver.find_element(By.ID, "cost").send_keys("30")

    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, "mode"))
    select.select_by_visible_text("TRANSCEIVER(TRX)")

    time.sleep(0.5)
    context.driver.find_element(By.ID, "tps").send_keys("100")

    time.sleep(0.5)
    context.driver.find_element(By.ID, "num_binds").send_keys("10")


@then('click on create SMPPC')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, "save_smppc")
    context.driver.execute_script("arguments[0].click();", button)


@then('verify bind and unbind buttons are present on the created SMPPC')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[3]/table/tbody/tr[1]/th[1]').text
    if text == 'Name/Carrier/Vendor/AccountType/Circle':
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"

    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[3]/table/tbody/tr[1]/th[1]').text
    if text == 'Name/Carrier/Vendor/AccountType/Circle':
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"
