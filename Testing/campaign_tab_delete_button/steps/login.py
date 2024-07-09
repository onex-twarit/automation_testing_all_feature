from behave import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='/home/twarit/Downloads/chromedriver-linux64/chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


@given(u'launch chrome browser')
def ChromeBrowserLaunch(context):
    try:
        time.sleep(0.5)
        context.driver = driver
        context.driver.maximize_window()
    except NameError:
        print("Chrome browser did not open")
    else:
        print("Chrome browser open successfully")


@when(u'open Onextel Homepage "{homepage}"')
def OpenHomepage(context, homepage):
    context.driver.maximize_window()
    try:
        context.driver.get(homepage)
    except NameError:
        print(f"{homepage} unable to load")
    else:
        print(f"{homepage} loaded successfully")


@then(u'Enter Username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.find_element(By.ID, "email").send_keys(user)
    context.driver.find_element(By.ID, "password").send_keys(pwd)


@then(u'Click on login button')
def step_impl(context):
    context.driver.implicitly_wait(20)
    button = context.driver.find_element(By.ID, "login_button")
    context.driver.execute_script("arguments[0].click();", button)


def clickables(value):
    button = driver.find_element(By.XPATH, value)
    driver.execute_script("arguments[0].click();", button)


@then(u'Close driver window')
def step_impl(context):
    time.sleep(0.5)
    context.driver.quit()
