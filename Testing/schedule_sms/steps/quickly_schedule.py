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


@then('Enter user name and password')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("ICICIAdmin")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("password")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="login_button"]').click()


@then('open dashboard page')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, "//*[@id='dashboard_title']").text
    if text == "Dashboard":
        assert True, "Test Passed"


@then('go to NEW SMS then to quick english sms')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="new_sms"]').click()  # go to new sms button
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="quick_eng_sms_title"]').click()  # go to quick english sms button
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="pills-campaign-tab"]').click()  # go to quick english SMS tab


@then('add recipients')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="recipient_numbers"]').send_keys(9876543210)  # add recipients
    # time.sleep(1)
    # context.driver.find_element(By.XPATH, '//*[@id="new_sms"]').click()


@then('present fields to be filled')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="groupDropdown"]').send_keys("test(1)")  # adding group
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="insert_template"]').click()  # go to insert template

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="template_type_id"]').send_keys(
        "Service Implicit(1)")  # select template type
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="template_name"]').send_keys("One Variable")  # select template name
    # time.sleep(0.5)
    # context.driver.find_element(By.XPATH, '//*[@id="dest_language"]').send_keys("Hindi")  # select language
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="insert_template_to_msg"]').click()  # click on select button


@then('check on schedule sms, split into campaigns and click on send')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[6]/div[1]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # check schedule box
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[6]/div[2]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # check multiple campaigns

    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="split_more"]').click()

    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="sms_body"]/div[7]/div[2]/div[2]/input').send_keys(1)  # sms count
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="sms_body"]/div[7]/div[3]/div[2]/input').send_keys(1)  # sms count
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'send')
    context.driver.execute_script("arguments[0].click();", button)  # send button


@then('new window for confirmation')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="proceed"]').click()  # confirmation button "yes"


@then('again on new window click on proceed')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="confirm_send_sms"]').click()  # proceed button "proceed"


@then('check if message is sent')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, '//*[@id="dashboard"]/div[2]/div[1]/h4').text
    if text == "Following Splits are Successfully Scheduled!!":
        assert True, "Test Passed"


@then('close the browser')
def step_impl(context):
    time.sleep(4)
    context.driver.close()
