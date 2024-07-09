from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then('fill the details to create SMPPC with LATIN-9 encoding type')
def step_impl(context):
    # enter TUC name
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'name').send_keys("smppcThree")

    # carrier name
    time.sleep(1)
    select = Select(context.driver.find_element(By.ID, 'carrier_id'))
    select.select_by_visible_text("carrier one")

    # vendor name
    time.sleep(1)
    select = Select(context.driver.find_element(By.ID, 'vendor'))
    select.select_by_visible_text("vendor one")

    # Account type
    time.sleep(1)
    select = Select(context.driver.find_element(By.ID, 'accounttype'))
    select.select_by_visible_text("Service Implicit")

    # circle name
    time.sleep(1)
    select = Select(context.driver.find_element(By.ID, 'circle_id'))
    select.select_by_visible_text("circle one")

    # gateway ID name
    time.sleep(1)
    select = Select(context.driver.find_element(By.ID, 'gateway_id'))
    select.select_by_visible_text("gatewaysChild")

    # SMPP login ID
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'smpplogin').send_keys("2222")

    # System ID
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'username').send_keys("3333")

    # Password
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'password').send_keys("password")

    # primary Host/IP
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'host').send_keys("1.1.1.1")

    # PORT
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'port').send_keys("9000")

    # SMS Cost
    time.sleep(1)
    context.driver.find_element(By.ID, 'cost').send_keys("30")

    # Auto Bind
    time.sleep(1)
    select = Select(context.driver.find_element(By.ID, 'auto_bind'))
    select.select_by_visible_text("True")

    # Support Flash
    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, 'supports_flash'))
    select.select_by_visible_text("False")

    # Encoding Type
    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, 'encoding_type'))
    select.select_by_visible_text("LATIN-9")
    context.encoding_type_3 = context.driver.find_element(By.ID, 'encoding_type').text

    # Bind Type
    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, 'mode'))
    select.select_by_visible_text("TRANSCEIVER(TRX)")

    # TPS
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'tps').send_keys("100")

    # No. of Binds
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'num_binds').send_keys("10")


@then('click on edit SMPPC for LATIN-9 encoding type')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         "//td[contains(text(),'smppcThree')]/following::td[5]/a[@title='Edit']")
    context.driver.execute_script("arguments[0].click();", button)


@then('verify the SMPPC LATIN-9 encoding type')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.ID, 'encoding_type').text
    if text == context.encoding_type_3:
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then('SMPPC encoding type LATIN-9 to GSM-7')
def step_impl(context):
    time.sleep(1)
    select = Select(context.driver.find_element(By.ID, 'encoding_type'))
    select.select_by_visible_text("GSM-7")
    context.encoding_type_gsm7 = context.driver.find_element(By.ID, 'encoding_type').text


@then('verify the updated SMPPC GSM-7 encoding type')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.ID, 'encoding_type').text
    if text == context.encoding_type_gsm7:
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"
