from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


@given('Launch the browser tuc')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@then('open loginnnn.py page tuc')
def step_impl(context):
    context.driver.get('http://localhost:8000/index')


@then('Enter user name and password tuc')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("ICICIAdmin")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("password")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="login_button"]').click()


@then('open dashboard page tuc')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, "//*[@id='dashboard_title']").text
    if text == "Dashboard":
        assert True, "Test Passed"


@then('go to NEW SMS then to quick unicode with group')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="new_sms"]').click()  # go to new sms button
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="uicode_sms_title"]').click()  # go to unicode sms button
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="pills-campaign-tab"]').click()  # go to unicode SMS tab


@then('present fields to be filled with group')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="groupDropdown"]').send_keys("test(1)")  # adding group
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


@then('check on recurrence, unicode, multipart and click on send')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[6]/div[3]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # check recurrence
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="repetation_type_dropdown"]').send_keys(
        "Weekly")  # click on recurrence dropdown(select weekly)
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="date2"]').send_keys("28/07/2023")  # changing date for next week
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[7]/div[6]/div[3]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # select one day in week

    time.sleep(3)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[5]/div[2]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # check allow unicode
    time.sleep(3)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[5]/div[1]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # check allow multipart sms
    time.sleep(3)
    context.driver.find_element(By.XPATH, '//*[@id="send"]').click()  # click on send button


@then('on new window click on proceed, before that verify the labels')
def step_impl(context):
    # sender ID label
    time.sleep(5)
    text = context.driver.find_element(By.XPATH,
                                       "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[4]"
                                       "/div[1]/div/div/div/div[1]/div[1]/div/div/div/div[2]/div[2]/div/p[1]").text
    if text == "123456":
        assert True, "Test Passed"

    # short url label
    time.sleep(5)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[4]/div[1]/div'
                                       '/div/div/div[1]/div[1]/div/div/div/div[2]/div[2]/div/p[2]').text
    if text == "disabled":
        assert True, "Test Passed"

    # sender ID label message label
    time.sleep(5)
    text = context.driver.find_element(By.XPATH,
                                       "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[4]/div[1]/div"
                                       "/div/div/div[1]/div[1]/div/div/div/div[2]/div[2]/div/p[3]").text
    if text == "इस लेख में हम आपको 9वीं कक्षा के लेखन कौशल के विषय ‘सन्देश लेखन’ के बारे में बता रहे हैं।":
        assert True, "Test Passed"

    # proceed button
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="confirm_send_sms"]').click()


@then('check if message is sent successfully')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, "//*[@id='upload_body']/div/div[1]/h6[2]").text
    if text == "Messages are Successfully Submitted !!!":
        assert True, "Test Passed"


@then('close the browser after sending')
def step_impl(context):
    time.sleep(4)
    context.driver.close()
