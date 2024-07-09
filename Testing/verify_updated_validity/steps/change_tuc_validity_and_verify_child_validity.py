from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then('change the validity(40) in tuc')
def step_impl(context):
    # clear the validity field
    context.driver.find_element(By.ID, 'validity').clear()

    # pass value in validity field
    context.driver.find_element(By.ID, 'validity').send_keys(40)
    context.validity = context.driver.find_element(By.ID, 'validity').get_attribute('value')


@then('verify the updated validity(40) in ta')
def step_impl(context):
    # verify the validity in TA after editing
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign"]/div[2]/table[2]/tbody/tr[3]/td[4]').text
    if text == context.validity:
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('ChildOne will be 40')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/table[2]/tbody/tr[2]/td[4]').text
    if text == "40":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('ChildTwo will be same')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/table[2]/tbody/tr[3]/td[4]').text
    if text == "30":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"
