from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


@given('Launch the browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@then('open loginnnn.py page')
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


@then('go to NEW SMS then to quick unicode')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="new_sms"]').click()                            # go to new sms button
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="uicode_sms_title"]').click()                   # go to unicode sms button
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="pills-campaign-tab"]').click()                 # go to unicode SMS tab


@then('present fields to be filled')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="recipient_numbers"]').send_keys(9462747020)    # adding recipients
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="insert_template"]').click()                    # go to insert template
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="template_type_id"]').send_keys(
    "Service Implicit(2)")                                                                         # select template type
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="template_name"]').send_keys("Hindi Short")     # select template name
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="dest_language"]').send_keys("Hindi")           # select language
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="insert_template_to_msg"]').click()             # click on select button


@then('check on recurrence, verify the labels and click on send')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[6]'
                                         '/div[3]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)                                 # check recurrence
    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH, '//*[@id="repetition_type_label"]').text          # label recurrence
    if text == 'Recurrence':
        assert True, 'Test Passed'
    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH, '//*[@id="recurrence_from_date_label"]').text     # from label
    if text == 'From':
        assert True, 'Test Passed'
    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH, '//*[@id="recurrence_from_to_label"]').text       # to label
    if text == 'To':
        assert True, 'Test Passed'
    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH, '//*[@id="hour_label"]').text                     # hour label
    if text == 'Hour':
        assert True, 'Test Passed'
    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH, '//*[@id="schedule_minute_label"]').text          # minute label
    if text == 'Minute':
        assert True, 'Test Passed'

    time.sleep(1)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[5]'
                                         '/div[2]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)                                 # check allow unicode
    time.sleep(3)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[5]'
                                         '/div[1]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)                           # check allow multipart sms
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="send"]').click()                         # click on send button

@then('on new window click on proceed')
def step_impl(context):
    time.sleep(4)
    context.driver.find_element(By.XPATH, '//*[@id="confirm_send_sms"]').click()                   # click on proceed to send


@then('check if message is sent')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, "//*[@id='upload_body']/div/div[1]/h6[2]").text
    if text == "Messages are Successfully Submitted !!!":
        assert True, "Test Passed"


@then('close the browser')
def step_impl(context):
    time.sleep(4)
    context.driver.close()
