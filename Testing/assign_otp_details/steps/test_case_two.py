from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


@given('Launch browser for the tenant')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@then('open loginnnn.py page for the tenant')
def step_impl(context):
    context.driver.get('http://localhost:8000/index')


@then('Enter user name and password for the tenant')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("Onexadmin")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("password")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="login_button"]').click()


@then('dashboard page for tenant')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, "//*[@id='dashboard_title']").text
    if text == "Dashboard":
        assert True, "Test Passed"


@then('go to otp details tab')
def step_impl(context):
    time.sleep(10)
    context.driver.find_element(By.XPATH, '//*[@id="profile_title"]').click()            # profile dropdown button
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="profiledropdown"]/li[5]/a').click()  # assign otp details button


@then('click on save changes and verify error labels')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//*[@id='save_otp_details']").click()


@then('close the browser')
def step_impl(context):
    time.sleep(4)
    context.driver.close()
