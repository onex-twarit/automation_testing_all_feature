from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then('fill the details to create SMPP with LATIN-1 encoding type')
def step_impl(context):
    # enter TUC name
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'ownertuc').send_keys("ICICIAdmin(2005)")

    # system id / user id
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'systemid').send_keys("1234567")
    context.type = context.driver.find_element(By.ID, 'systemid').text

    # enter password
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'password').send_keys("password")

    # system type
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'systemtype').send_keys("systemTwo")

    # Account type
    time.sleep(1)
    select = Select(context.driver.find_element(By.ID, 'accounttype'))
    select.select_by_visible_text("Service Implicit")

    # limit SMS/Day
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'limitday').send_keys("30")

    # Limit SMS/ Hour
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'limithour').send_keys("10")

    # Encoding type (GSM-7)
    time.sleep(1)
    select = Select(context.driver.find_element(By.ID, 'encoding_type'))
    select.select_by_visible_text("LATIN-1")
    context.encoding_type_2 = context.driver.find_element(By.ID, 'encoding_type').text

    # SMPP Bind Type (select TRX)
    time.sleep(1)
    select = Select(context.driver.find_element(By.ID, 'mode'))
    select.select_by_visible_text("TRANSCEIVER(TRX)")

    # Total TPS
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'total_tps').send_keys("200")

    # Max Binds
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'max_binds').send_keys("10")

    # Keep Alive
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'keep_alive').send_keys("5")


@then('click on edit SMPP for LATIN-1 encoding type')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         "//td[contains(text(),'1234567')]/following::td[5]/a[@title='Edit']")
    context.driver.execute_script("arguments[0].click();", button)


@then('verify the LATIN-1 encoding type')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.ID, 'encoding_type').text
    if text == context.encoding_type_2:
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then('encoding type LATIN-1 to LATIN-9')
def step_impl(context):
    time.sleep(1)
    select = Select(context.driver.find_element(By.ID, 'encoding_type'))
    select.select_by_visible_text("LATIN-9")
    context.encoding_type_latin9 = context.driver.find_element(By.ID, 'encoding_type').text


@then('verify the updated LATIN-9 encoding type')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.ID, 'encoding_type').text
    if text == context.encoding_type_latin9:
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"
