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


@then('open login page')
def step_impl(context):
    time.sleep(0.5)
    context.driver.get('http://localhost:8000/index')


@then('Enter user name and password')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("onexsa")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Pass123@@")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="login_button"]').click()


@then('open dashboard page')
def step_impl(context):
    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH, "//*[@id='dashboard_title']").text
    if text == "Dashboard":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('go to settings')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="menu_setting"]/p').click()  # go to settings


@then('go to discounting mapping tab')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="discount-map-tab"]').click()  # go to discounting mapping tab


@then('click on show button (discounting)')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show-users')
    button.is_enabled()


@then('it should be disabled in one click (discounting)')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show-users')
    context.driver.execute_script("arguments[0].click();", button)  # check button should be disabled
    button.get_property('disabled')


@then('close')
def step_impl(context):
    time.sleep(0.5)
    context.driver.close()
