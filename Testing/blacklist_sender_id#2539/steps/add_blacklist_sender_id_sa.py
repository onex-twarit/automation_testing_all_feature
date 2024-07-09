from selenium import webdriver
from selenium.webdriver import Keys
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


@then('Enter user name and password for sa')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("onexsa")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Pass123@@")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="login_button"]').click()


@then('open dashboard page, go to config')
def step_impl(context):
    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH, "//*[@id='dashboard_title']").text
    if text == "Dashboard":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="menu_config"]/p')
    context.driver.execute_script("arguments[0].click();", button)  # go to config


@then('go to Blacklist sender ID tab')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="blacklist_senderid"]').click()  # go to blacklist sender ID tab


@then('click on add sender ID blacklist button')
def step_impl(context):
    # click on add sender id blacklist button
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="add_sender_blacklist"]')
    context.driver.execute_script("arguments[0].click();", button)


@then('enter sender ID and description then click on add button')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="blacklist-name"]').send_keys(1234)

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="blacklist_desc"]').send_keys("desc")

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="create_blacklist"]')
    context.driver.execute_script("arguments[0].click();", button)  # click on add button


@then('logout sa and Enter user name and password for tuc')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="dropdown-caret"]')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="log-out"]')
    context.driver.execute_script("arguments[0].click();", button)

    # loginnnn.py tuc
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("tucOne")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Pass123@@")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="login_button"]').click()


@then('open dashboard page, click on New SMS button')
def step_impl(context):
    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH, "//*[@id='dashboard_title']").text
    if text == "Dashboard":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"

    time.sleep(25)
    button = context.driver.find_element(By.XPATH, '//*[@id="new_sms"]')
    context.driver.execute_script("arguments[0].click();", button)  # go to New SMS


@then('go to quick english SMS tab')
def step_impl(context):
    time.sleep(25)
    button = context.driver.find_element(By.XPATH, '//*[@id="quick_eng_sms_title"]')
    context.driver.execute_script("arguments[0].click();", button)  # go to quick english sms


@then('check in Sender ID field, it should not come')
def step_impl(context):
    time.sleep(0.5)
    dropdown = Select(context.driver.find_element(By.XPATH, '//*[@id="sender_id"]'))
    assert dropdown.first_selected_option.text == ""


# ************* alternate way *************
# @then('check in Sender ID field, it should not come')
# def step_impl(context):
#     time.sleep(0.5)
#     dropdown = Select(context.driver.find_element(By.XPATH, '//*[@id="sender_id"]'))
#     dropdown.select_by_value("")
#     assert True, "Test Passed"

@then('close')
def step_impl(context):
    time.sleep(0.5)
    context.driver.close()
