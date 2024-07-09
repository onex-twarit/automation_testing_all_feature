from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service = Service(executable_path='/home/twarit/Downloads/chromedriver-linux64/chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


@then('open dashboard page')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.ID, 'dashboard_title').text
    if text == "Dashboard":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on click on new sms, click on quick sms')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'new_sms').click()  # go to NEW SMS

    time.sleep(2)
    button = context.driver.find_element(By.ID, 'quick_eng_sms_title')
    context.driver.execute_script("arguments[0].click();", button)  # go to quick english SMS


@then('select campaign RCF(2348)')
def step_impl(context):
    time.sleep(1)
    select = Select(context.driver.find_element(By.ID, "campaign_name"))
    select.select_by_visible_text('RCF(2348)')


@then('select sender ID')
def step_impl(context):
    temp = context.driver.find_element(By.ID, 'sender_id')  # select sender ID
    select = Select(temp)
    select.select_by_visible_text("123456")


@then('add recipients')
def add_recipients(context):
    time.sleep(2)
    context.driver.find_element(By.ID, 'recipient_numbers').send_keys(9950500435)


@then('insert short template, select filter as dropdown')
def template_english_short_dropdown(context):
    time.sleep(1)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(1)
    context.driver.find_element(By.ID, 'insert_template').click()  # go to insert template

    time.sleep(1)
    context.driver.implicitly_wait(30)
    action = (ActionChains(context.driver))
    type = context.driver.find_element(By.ID, 'template_type_id')  # select template type

    action.move_to_element(type).click().perform()

    time.sleep(0.5)
    action.key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).click().perform()

    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, "template_filter_id"))
    select.select_by_visible_text('Dropdown')

    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, 'modal_template_id'))
    select.select_by_visible_text('English Short')

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'insert_template_to_msg')
    context.driver.execute_script("arguments[0].click();", button)  # click on select button


@then('click on send, then send now')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'send')
    context.driver.execute_script("arguments[0].click();", button)  # click on send button

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'confirm_send_sms')
    context.driver.execute_script("arguments[0].click();", button)  # click on send now button


@then('click on New SMS')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'new_sms')
    context.driver.execute_script("arguments[0].click();", button)  # click on new sms button
