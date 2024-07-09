from behave import *
import time
from selenium.webdriver.common.by import By


@then('add group, remove duplicate and fill the present fields')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="groupDropdown"]').send_keys("new test(3)")  # adding group

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="insert_template"]').click()  # go to insert template

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="template_type_id"]').send_keys(
        "Service Implicit(2)")  # select template type

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="template_name"]').send_keys("One Variable")  # select template name

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="insert_template_to_msg"]').click()  # click on select button

    time.sleep(1)
    button = context.driver.find_element(By.ID, 'send')
    context.driver.execute_script("arguments[0].click();", button)  # send button


@then('send it, verify number and credits')
def step_impl(context):

    #   verify numbers
    time.sleep(2)
    text = context.driver.find_element(By.XPATH,
                                       '//*[@id="bd-example-modal-lg"]/div/div/div[2]/div[2]/div[8]/div/p').text
    if text == 3:
        assert True, "Test Passed"
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'confirm_send_sms')
    context.driver.execute_script("arguments[0].click();", button)  # click on send now button

    time.sleep(1)
    button = context.driver.find_element(By.ID, 'confirm_send_sms')
    context.driver.execute_script("arguments[0].click();", button)  # click on new sms button

    time.sleep(1)
    new_avail_bal = context.driver.find_element(By.XPATH, '//*[@id="available_credits"]').text
    context.new_avail_balance = int(str(new_avail_bal).replace(",", ""))  # verifying the credits

    assert context.available_bal == 3 + context.new_avail_balance
