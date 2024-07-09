from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

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


@then('open dashboard page SA')
def step_impl(context):
    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH, "//*[@id='dashboard_title']").text
    if text == "Dashboard":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('go to notification')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="menu_notification"]/p').click()  # go to notification


@then('click on show notification button')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_notification')
    button.is_enabled()  # check enabled button

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="show_notification"]').click()  # click 'show notification' button
    button.get_property('disabled')  # check disabled button


@then('check the notifications in the panel')
def step_impl(context):
    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH, '//*[@id="notification_table_subject_header"]').text
    if text == "Subject":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('close the browser')
def step_impl(context):
    time.sleep(0.5)
    context.driver.close()
