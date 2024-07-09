from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then('click on Add SMPP')
def add_smpp(context):
    # adding a new smmp
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'create_smpps')
    context.driver.execute_script("arguments[0].click();", button)


@then('fill the details to create SMPP with GSM-7 encoding type')
def add_details_smpp(context):
    # enter TUC name
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'ownertuc').send_keys("ICICIAdmin(2005)")

    # system id / user id
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'systemid').send_keys("123456")
    context.type = context.driver.find_element(By.ID, 'systemid').text

    # enter password
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'password').send_keys("password")

    # system type
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'systemtype').send_keys("systemOne")

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
    select.select_by_visible_text("GSM-7")
    context.encoding_type_1 = context.driver.find_element(By.ID, 'encoding_type').text

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


@then('add the SMPP')
def save_smpp(context):
    # click on create smpp
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'save_smpps')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on edit SMPP for GSM-7 encoding type')
def edit_smpp(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         "//td[contains(text(),'123456')]/following::td[5]/a[@title='Edit']")
    context.driver.execute_script("arguments[0].click();", button)


@then('verify the GSM-7 encoding type')
def verify_smpp_gsm7(context):
    # verify the encoding type GSM-7
    time.sleep(1)
    text = context.driver.find_element(By.ID, 'encoding_type').text
    if text == context.encoding_type_1:
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then('click on cancel')
def click_cancel(context):
    # click on cancel button
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'cancel')
    context.driver.execute_script("arguments[0].click();", button)


@then('encoding type GSM-7 to LATIN-1')
def update_encoding_type(context):
    # change encoding type GSM-7 to LATIN-1
    time.sleep(1)
    select = Select(context.driver.find_element(By.ID, 'encoding_type'))
    select.select_by_visible_text("LATIN-1")
    context.encoding_type_latin1 = context.driver.find_element(By.ID, 'encoding_type').text


@then('click on update SMPP')
def click_update(context):
    # click on update to update with latest change
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'update_smpps')
    context.driver.execute_script("arguments[0].click();", button)


@then('verify the updated LATIN-1 encoding type')
def verify_updated_smpp(context):
    # verify the smpp after changing the encoding type
    time.sleep(1)
    text = context.driver.find_element(By.ID, 'encoding_type').text
    if text == context.encoding_type_latin1:
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

