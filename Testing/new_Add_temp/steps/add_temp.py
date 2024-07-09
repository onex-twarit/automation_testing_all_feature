from behave import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='/home/twarit/Downloads/chromedriver-linux64/chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then('click DLT')
def click_dlt(context):
    time.sleep(1)
    button = context.driver.find_element(By.XPATH, '//*[@id="menu_manage"]/p')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to entity ID tab, click on add entity ID')
def add_entity_id(context):
    # click on entity ID tab
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'entityid_tab')
    context.driver.execute_script("arguments[0].click();", button)

    # click on add entity di button
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'create_entityid')
    context.driver.execute_script("arguments[0].click();", button)

    # enter entity id on new pop-up
    time.sleep(1)
    context.driver.find_element(By.ID, 'entity_id').send_keys(1001925513851834602)

    # enter entity name on new pop-up
    time.sleep(1)
    context.driver.find_element(By.ID, 'entity_name').send_keys("ONEXTEL MEDIA")

    # add enitity id button
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'add_entityid')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to sender ID tab, click on add sender ID(uncheck default)')
def add_sender_id(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'senderid_tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    button = context.driver.find_element(By.ID, 'create_senderid')
    context.driver.execute_script("arguments[0].click();", button)

    # enter sender ID
    time.sleep(1)
    context.driver.find_element(By.ID, 'sender_name').send_keys("ONEXTL")

    # select name from dropdown
    select_name = context.driver.find_element(By.ID, 'sender_entity_id')
    select = Select(select_name)
    select.select_by_visible_text("ONEXTEL MEDIA(1001925513851834602)")

    # uncheck box of set as default
    time.sleep(1)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div[2]/div[4]/div/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)

    # click on add button to add S ID
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'add_sender_id')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to template tab, click on add template')
def add_template(context):
    # click on template tab
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'template_tab')
    context.driver.execute_script("arguments[0].click();", button)

    # click on add template
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'create_template')
    context.driver.execute_script("arguments[0].click();", button)


@then('english, fill all the fields, then click on add')
def add_template_data(context):
    # enter template name
    time.sleep(1)
    context.driver.find_element(By.ID, 'template_name').send_keys("English Short")

    # enter template ID
    time.sleep(1)
    context.driver.find_element(By.ID, 'template_id').send_keys(1007027335661181164)

    # select template type
    time.sleep(1)
    text = context.driver.find_element(By.ID, "template_type_id")
    select = Select(text)
    select.select_by_visible_text("Service Implicit")

    # select template entity id
    time.sleep(1)
    text = context.driver.find_element(By.ID, "template_entity_id")
    select = Select(text)
    select.select_by_visible_text("ONEXTEL MEDIA(1001925513851834602)")

    # select template sender id
    time.sleep(1)
    text = context.driver.find_element(By.ID, "template_sender_id")
    select = Select(text)
    select.select_by_visible_text("ONEXTL")

    # give the content to template
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="template_content"]').send_keys(
        "Your secured Login OTP is {#var#}.\nOnextel")

    # click on add button to add template
    time.sleep(2)
    button = context.driver.find_element(By.ID, 'add_template')
    context.driver.execute_script("arguments[0].click();", button)


@given(u'launch chrome browser')
def ChromeBrowserLaunch(context):
    try:
        time.sleep(0.5)
        context.driver = driver
        context.driver.maximize_window()
    except NameError:
        print("Chrome browser did not open")
    else:
        print("Chrome browser open successfully")


@when(u'open Onextel Homepage "{homepage}"')
def OpenHomepage(context, homepage):
    context.driver.maximize_window()
    try:
        context.driver.get(homepage)
    except NameError:
        print(f"{homepage} unable to load")
    else:
        print(f"{homepage} loaded successfully")


@then(u'Enter Username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.find_element(By.ID, "email").send_keys(user)
    context.driver.find_element(By.ID, "password").send_keys(pwd)


@then(u'Click on login button')
def step_impl(context):
    context.driver.implicitly_wait(20)
    button = context.driver.find_element(By.ID, "login_button")
    context.driver.execute_script("arguments[0].click();", button)


def clickables(value):
    button = driver.find_element(By.XPATH, value)
    driver.execute_script("arguments[0].click();", button)


@then(u'Close driver window')
def step_impl(context):
    time.sleep(0.5)
    context.driver.quit()
