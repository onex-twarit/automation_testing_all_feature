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
    time.sleep(2)
    context.driver = driver
    context.driver.maximize_window()


@then('open login page')
def step_impl(context):
    time.sleep(2)
    context.driver.get('http://localhost:8000/index')


@then('Enter user name and password for tuc')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("tucOne")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Pass123@")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="login_button"]').click()


@then('open dashboard page tuc')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, "//*[@id='dashboard_title']").text
    if text == "Dashboard":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('go to DLT then to template tab')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="menu_manage"]').click()  # go to DLT
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="template_tab"]').click()  # go to template tab
    # time.sleep(0.5)
    # context.driver.find_element(By.XPATH, '//*[@id="pills-campaign-tab"]').click()  # go to quick english SMS tab


@then('select ALL from the search type dropdown')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="search"]').click()  # click on search

    time.sleep(4)
    dropdown = driver.find_element(By.XPATH, '//*[@id="template_type"]')  # select value from dropdown
    drp = Select(dropdown)
    drp.select_by_visible_text("Template ID")
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="template_search_id"]').send_keys(12345)  # passing the value
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="search"]').click()  # click on search
    time.sleep(3)
    text = context.driver.find_element(By.XPATH,
                                       "/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[3]/table/tbody/tr[2]/td[5]").text
    if text == 12345:
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"

    time.sleep(3)
    context.driver.find_element(By.XPATH, '//*[@id="reset"]').click()  # click on reset
    time.sleep(3)


@then('click on search')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '//*[@id="search"]')

    context.driver.execute_script("arguments[0].click();", button)  # click on search


@then('close the browser')
def step_impl(context):
    time.sleep(0.5)
    context.driver.close()
