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
    context.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("tenantOne")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Pass123@@")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="login_button"]').click()


@then('open dashboard page, go to User Management')
def step_impl(context):
    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH, "//*[@id='dashboard_title']").text
    if text == "Dashboard":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/a[2]/p')  # go to User management
    context.driver.execute_script("arguments[0].click();", button)


@then('go to All TUC tab')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="all_tucs"]').click()  # go to all tuc tab


@then('click on \'show all tuc\' button')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_alltuc_clicked')
    button.is_enabled()  # button enabled

    button = context.driver.find_element(By.XPATH, '//*[@id="show_alltuc_clicked"]')  # click on show all tuc button
    context.driver.execute_script("arguments[0].click();", button)
    button.get_property('disabled')  # button disabled


@then('go to hub, then go to gateway tab click on show button')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/a[7]/p').click()  # go to hub

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="gateway_view"]').click()  # go to gateway tab

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'apply_filter')
    button.is_enabled()  # button enabled

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '//*[@id="apply_filter"]')  # click on show button
    context.driver.execute_script("arguments[0].click();", button)
    button.get_property('disabled')  # button disabled


@then('go to SMPPC tab, click on show button')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[2]/div[2]/div[2]/ul/li[2]').click()  # go to all tuc tab

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'search_host')
    button.is_enabled()  # button enabled

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="search_host"]')  # click on show all tuc button
    context.driver.execute_script("arguments[0].click();", button)
    button.get_property('disabled')  # button disabled


@then('close')
def step_impl(context):
    time.sleep(0.5)
    context.driver.close()
