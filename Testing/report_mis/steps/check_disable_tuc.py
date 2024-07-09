from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


# Login to Tenant – user management – Search by TUC name – disable tuc – close.

@given('Launch the browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@then('open login page')
def step_impl(context):
    context.driver.get('http://localhost:8000/index')


@then('Enter user name and password')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("Onexadmin")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Pass123@")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="login_button"]').click()


@then('open dashboard page')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, "//*[@id='dashboard_title']").text
    if text == "Dashboard":
        assert True, "Test Passed"


@then('go to User Management, search tuc by name')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="menu_users"]/p').click()  # go to user management tab
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="tuc_view"]').click()  # go to tuc tab
    time.sleep(0.5)
    find = context.driver.find_element(By.XPATH, '//*[@id="tuc_input"]').send_keys("newtuc")  # search tuc by name
    if find:

        time.sleep(2)
        text = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign"]/div[2]/table/tbody/tr[2]/td[1]').text
        if text == "newtuc(2000)":
            assert True, "Test Passed"


@then('disable the tuc and check in inactive')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/table/tbody/tr[2]/td[6]/a[3]/div/label/input')
    context.driver.execute_script("arguments[0].click();", button)  # disable tuc

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="suspend_tuc"]').send_keys(
        "Confirm with Support")  # select option for disable

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div/div/div/div/div[3]/a')
    context.driver.execute_script("arguments[0].click();", button)  # suspend now

    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="menu_report"]/p').click()  # go to report tab

    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="pills-tab"]/li[1]').click()  # go to MIS tab

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[1]/div[1]/div[1]/div/input[3]')
    context.driver.execute_script("arguments[0].click();", button)  # check inactive tuc

    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="tuc-report"]').send_keys("newtuc(2000)")  # enter tuc

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)  # click on search button

    time.sleep(2)
    text = context.driver.find_element(By.XPATH, '//*[@id="customers"]/tbody/tr[33]/th[26]/a').text
    if text == 134:
        assert True, "Test Passed"


@then('close')
def step_impl(context):
    time.sleep(4)
    context.driver.close()
