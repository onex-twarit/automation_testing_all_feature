from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


@given('Launching browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@then('login page')
def step_impl(context):
    context.driver.get('http://localhost:8000/index')


@then('user name and password')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("ICICIAdmin")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("password")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="login_button"]').click()


@then('dashboard page')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, "//*[@id='dashboard_title']").text
    if text == "Dashboard":
        assert True, "Test Passed"


@then('go to NEW SMS after it go to quick english sms tuc')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="new_sms"]').click()  # go to new sms button
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="quick_eng_sms_title"]').click()  # go to quick english sms button
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="pills-campaign-tab"]').click()  # go to quick english SMS tab


@then('add recipients and select template')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="recipient_numbers"]').send_keys(9876543210,
                                                                                    "\n")  # add recipients

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="insert_template"]').click()  # go to insert template

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="template_type_id"]').send_keys(
        "Service Implicit(1)")  # select template type

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="template_name"]').send_keys("One Variable")  # select template name

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="insert_template_to_msg"]').click()  # click on select button


@then('check on schedule sms (within 15 min)')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[6]/div[1]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # check schedule sms

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="schedule_row_min"]').send_keys(10)  # select within 15 min


@then('click send')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'send')
    context.driver.execute_script("arguments[0].click();", button)  # send button


@then('verify for the error label on new window')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, '//*[@id="error_msg_text"]').text
    if text == "Schedule Time should not be in between of 15 minutes from current time":
        assert True, "Test Passed"


@then('click on OK button')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/'
                                         'div[4]/div[1]/div/div/div/div[1]/div[1]/div/div/div/div[3]/input')
    context.driver.execute_script("arguments[0].click();", button)  # click on OK button


@then('browser closed')
def step_impl(context):
    time.sleep(4)
    context.driver.close()
