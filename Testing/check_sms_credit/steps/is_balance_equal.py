from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


@given('Launch the browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@then('open login page')
def step_impl(context):
    context.driver.get('http://localhost:8000/index')


@then('Enter user name and password for tuc user')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("ICICIAdmin")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("password")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="login_button"]').click()


@then('open dashboard page for tuc user')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, "//*[@id='dashboard_title']").text
    if text == "Dashboard":
        assert True, "Test Passed"

    time.sleep(2)
    avail_balance = context.driver.find_element(By.XPATH, '//*[@id="available_credits"]').text
    context.available_bal = int(str(avail_balance).replace(",", ""))


@then('go to NEW SMS then to quick unicode')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="new_sms"]')
    context.driver.execute_script("arguments[0].click();", button)
    # context.driver.find_element(By.XPATH, '//*[@id="new_sms"]').click()                         # go to new sms button
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="uicode_sms_title"]').click()  # go to unicode sms button
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="pills-campaign-tab"]').click()  # go to unicode SMS tab


@then('present fields to be filled and check current credit')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="recipient_numbers"]').send_keys(9462747020)  # adding recipients
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="insert_template"]').click()  # go to insert template
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="template_type_id"]').send_keys(
        "Service Implicit(2)")  # select template type
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="template_name"]').send_keys("Hindi Short")  # select template name
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="dest_language"]').send_keys("Hindi")  # select language
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="insert_template_to_msg"]').click()  # click on select button


@then('check on recurrence, set timing and click on send')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.NAME, 'recurrence_check')
    context.driver.execute_script("arguments[0].click();", button)  # check recurrence

    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="repetation_type_dropdown"]').send_keys("Daily")

    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="recurrence_hour"]').send_keys(17)

    time.sleep(1)
    button = context.driver.find_element(By.NAME, 'unicode_check')
    context.driver.execute_script("arguments[0].click();", button)  # check allow unicode

    time.sleep(1)
    context.driver.find_element(By.NAME, 'multipart_check').click()  # check allow multipart sms
    time.sleep(1)
    # context.driver.find_element(By.XPATH, '//*[@id="send"]').click()                               # click on send button
    button = context.driver.find_element(By.ID,
                                         'send')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(4)
    context.driver.find_element(By.XPATH, '//*[@id="confirm_send_sms"]').click()  # click on proceed to send


@then('after clicking on proceed substract total credits from current credit and check')
def step_impl(context):
    time.sleep(2)
    total_ded = context.driver.find_element(By.XPATH,
                                            '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/table/tbody/tr[2]/td[10]').text
    context.total_deductions = int(str(total_ded).replace(",", ""))

    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="new_sms"]').click()

    curr_bal = context.driver.find_element(By.ID, 'available_credits').text
    time.sleep(2)
    current_bal = int(str(curr_bal).replace(",", ""))

    assert current_bal == context.available_bal - context.total_deductions


@then('close the browser')
def step_impl(context):
    time.sleep(2)
    context.driver.close()
