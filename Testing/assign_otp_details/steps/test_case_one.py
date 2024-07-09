from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


@given('Launch browser for tenant')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@then('open loginnnn.py page for tenant')
def step_impl(context):
    context.driver.get('http://localhost:8000/index')


@then('Enter user name and password for tenant')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("Onexadmin")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("password")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="login_button"]').click()


@then('dashboard page tenant')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, "//*[@id='dashboard_title']").text
    if text == "Dashboard":
        assert True, "Test Passed"


@then('go to assign otp details tab')
def step_impl(context):
    time.sleep(10)
    context.driver.find_element(By.XPATH, '//*[@id="profile_title"]').click()  # profile dropdown button
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="profiledropdown"]/li[5]/a').click()  # assign otp details button


@then('verify the present fields')
def step_impl(context):
    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH, '//*[@id="otp_descendant_selected"]').text  # select TUC field
    if text == "Select Tuc":
        assert True, "Test Passed"
    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH, '//*[@id="otp_api_key"]').text  # API key field
    if text == "API Key":
        assert True, "Test Passed"
    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH, '//*[@id="otp_sender_id"]').text  # sender ID field
    if text == "Sender ID":
        assert True, "Test Passed"
    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH, '//*[@id="otp_entity_id"]').text  # entity ID field
    if text == "Entity ID":
        assert True, "Test Passed"
    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH, '//*[@id="otp_template_id"]').text  # template ID field
    if text == "Template ID":
        assert True, "Test Passed"
    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH, '//*[@id="otp_msg_content"]').text  # content field
    if text == "Content":
        assert True, "Test Passed"


@then('close browser for tenant')
def step_impl(context):
    context.driver.close()
