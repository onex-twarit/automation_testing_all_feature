from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from behave import *
import time
from selenium.webdriver.common.by import By

service = Service(executable_path='/home/twarit/Downloads/chromedriver-linux64/chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


@given('Launch the browser')
def step_impl(context):
    time.sleep(0.5)
    context.driver = driver
    context.driver.maximize_window()


@then(u'open login page')
def step_impl(context):
    time.sleep(0.5)
    context.driver.get('http://localhost:8000/index')


@then('Enter user name and password for SA')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("onexsa")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Pass123@")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="login_button"]').click()


@then('open dashboard page')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/p[1]').text
    if text == "Dashboard":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"


@then('go to User Management')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="menu_users"]/p')  # go to user management
    context.driver.execute_script("arguments[0].click();", button)


@then('go to user tab, click on search button')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/ul/li[2]').click()  # go to User tab

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="user_search"]')  # click on search button
    context.driver.execute_script("arguments[0].click();", button)


@then('error label \'No Record found\' should come')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign"]/div[2]/span').text

    if text == "No Record found":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"


@then('search tab, click on search button')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="search"]').click()  # go to search tab

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="search_type"]')  # click on search button
    context.driver.execute_script("arguments[0].click();", button)


@then('error label \'Please enter Sender ID\' should come')
def step_impl(context):
    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign"]/div[2]/span').text

    if text == 'Please enter Sender ID':
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"


@then('close')
def step_impl(context):
    time.sleep(0.5)
    context.driver.close()
