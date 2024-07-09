from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


@given('Launch browser tuc user')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@then('open loginnnn.py page for tuc user')
def step_impl(context):
    context.driver.get('http://localhost:8000/index')


@then('Enter user name and password for tuc user')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("ICICIAdmin")
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("password")


@then('Click on the Sign in button for tuc user')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="login_button"]').click()


@then('Welcome to dashboard page for tuc user')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, "//*[@id='dashboard_title']").text
    if text == "Dashboard":
        assert True, "Test Passed"


@then('go to DLT and add Entity ID')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="menu_manage"]/p').click()   # go to entity tab
    time.sleep(2)
    context.driver.find_element(By.ID, 'create_entityid').click()               # add entity id
    time.sleep(2)
    context.driver.find_element(By.ID, 'entity_id').send_keys(123)              # enter entity id
    time.sleep(2)
    context.driver.find_element(By.ID, 'entity_name').send_keys("ONEXTEL")      # enter name
    time.sleep(2)
    context.driver.find_element(By.ID, 'add_entityid').click()                  # button for adding entity id


@then('add sender ID')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, 'senderid_tab').click()                        # sender id tab
    time.sleep(2)
    context.driver.find_element(By.ID, 'create_senderid').click()                     # add button sender id
    time.sleep(2)
    context.driver.find_element(By.ID, 'sender_name').send_keys(123456)               # enter sender id
    time.sleep(2)
    context.driver.find_element(By.ID, 'sender_entity_id').send_keys("ONEXTEL(123)")  # entity name
    time.sleep(2)
    context.driver.find_element(By.ID, 'add_sender_id').click()                       # button for adding sender id


@then('add template')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, 'template_tab').click()                              # click on template tab
    time.sleep(2)
    context.driver.find_element(By.ID, 'create_template').click()                           # add template button
    time.sleep(2)
    context.driver.find_element(By.ID, 'template_name').send_keys("One Variable")           # enter template name
    time.sleep(2)
    context.driver.find_element(By.ID, 'template_id').send_keys(1234567890)                 # enter template ID
    time.sleep(2)
    context.driver.find_element(By.ID, 'template_type_id').send_keys("Service Implicit")    # enter template type
    time.sleep(2)
    context.driver.find_element(By.ID, 'template_entity_id').send_keys("ONEXTEL(123)")      # select entity ID
    time.sleep(2)
    context.driver.find_element(By.ID, 'template_sender_id').send_keys(123456)              # enter sender ID
    time.sleep(2)
    context.driver.find_element(By.ID, 'template_content').send_keys("Hello {#var#}, Welcome.")  # give content
    time.sleep(2)
    context.driver.find_element(By.ID, 'add_template').click()                              # add template button

