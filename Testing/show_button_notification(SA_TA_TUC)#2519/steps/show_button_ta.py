import time
from selenium.webdriver.common.by import By
from behave import *


@then('Enter user name and password ta')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("tenantOne")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Pass123@@")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="login_button"]').click()


@then(u'open dashboard page ta')
def step_impl(context):
    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH, "//*[@id='dashboard_title']").text
    if text == "Dashboard":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"
