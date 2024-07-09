from selenium import webdriver
from selenium.webdriver import Keys
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
    context.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("tucOne")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Pass123@@")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="login_button"]').click()


@then('open dashboard page, go to user management')
def step_impl(context):
    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH, "//*[@id='dashboard_title']").text
    if text == "Dashboard":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/a[3]/p').click()  # go to user management


@then('go to TUC tab, search for any tuc, select and search')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="tuc_view"]').click()  # go to TUC tab

    time.sleep(0.5)
    select_tuc = context.driver.find_element(By.XPATH, '//*[@id="tuc_input"]')  # search for a tuc
    time.sleep(0.5)
    select_tuc.send_keys("t")
    time.sleep(0.5)
    select_tuc.send_keys(Keys.ARROW_DOWN)     # find from the suggestions
    time.sleep(0.5)
    select_tuc.send_keys(Keys.RETURN)

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '//*[@id="user_search"]')

    context.driver.execute_script("arguments[0].click();", button)  # click on search

    time.sleep(2)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div/table[2]/tbody/tr[1]/th[1]').text
    if text == "TUC Name":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('close')
def step_impl(context):
    time.sleep(0.5)
    context.driver.close()
