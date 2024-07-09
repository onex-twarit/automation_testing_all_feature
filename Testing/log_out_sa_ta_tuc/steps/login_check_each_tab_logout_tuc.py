from behave import *
import time
from selenium.webdriver.common.by import By


@then('go to Campaign')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_campaigns')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on Show Campaign')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_campaign')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to DLT')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_manage')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Entity IDs tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'entityid_tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on show entity ID')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_entityid')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Sender IDs tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'senderid_tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on show sender ID')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_senderid')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Template tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'template_tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Bulk Upload tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'bulktemplate_tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to URL tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'url_tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on Show SMPP')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_smpp_tuc')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to API')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_api')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on Show API')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'view_api')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Phonebook')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_phonebook')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Groups tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'groups')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on Show Group')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show-group')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Contacts tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'contacts')
    context.driver.execute_script("arguments[0].click();", button)
