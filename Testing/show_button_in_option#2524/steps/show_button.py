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


@then('open loginnnn.py page')
def step_impl(context):
    time.sleep(0.5)
    context.driver.get('http://localhost:8000/index')


@then('Enter user name and password')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("onexsa")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Pass123@")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="login_button"]').click()


@then('open dashboard page, go to options')
def step_impl(context):
    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH, "//*[@id='dashboard_title']").text
    if text == "Dashboard":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="menu_option"]')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to carrier tab,check enable and disable show button, click on show carrier')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="option_carrier"]').click()  # go to carrier tab

    # click on add carrier button
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="add_carrier"]')
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="carrier_name"]').send_keys("carrier 4")

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="carrier_desc"]').send_keys("desc")

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="add_option"]')
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_data')
    button.is_enabled()  # check, button is enabled

    time.sleep(0.5)
    disabled_button = context.driver.find_element(By.XPATH, '//*[@id="show_data"]')
    context.driver.execute_script("arguments[0].click();", disabled_button)  # show carrier button
    disabled_button.get_property('disabled')  # check, button is disabled


@then('go to vendor tab,check enable and disable show button, click on show vendor')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="option_vendor"]').click()  # go to vendor tab

    button = context.driver.find_element(By.ID, 'show_data')
    button.is_enabled()

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="show_data"]')
    context.driver.execute_script("arguments[0].click();", button)  # show vendor button
    button.get_property('disabled')  # check, button is disabled


@then('go to circle tab,check enable and disable show button, click on show circle')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="option_circle"]').click()  # go to circle tab

    button = context.driver.find_element(By.ID, 'show_data')
    button.is_enabled()

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="show_data"]')
    context.driver.execute_script("arguments[0].click();", button)  # show circle button
    button.get_property('disabled')  # check, button is disabled


@then('go to type tab,check enable and disable show button, click on show type')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="option_type"]').click()  # go to type tab

    button = context.driver.find_element(By.ID, 'show_data')
    button.is_enabled()

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="show_data"]')
    context.driver.execute_script("arguments[0].click();", button)  # show type button
    button.get_property('disabled')  # check, button is disabled


@then('close')
def step_impl(context):
    time.sleep(0.5)
    context.driver.close()
