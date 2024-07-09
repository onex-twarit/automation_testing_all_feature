from behave import *
import time
from selenium.webdriver.common.by import By


@then('open dashboard')
def open_dashboard(context):
    time.sleep(0.5)
    text = context.driver.find_element(By.ID, 'dashboard_title').text
    if text == "Dashboard":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click campaign')
def tuc_click_campaign(context):
    # in tuc click on campaign
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_campaigns')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on add campaign button')
def add_campaign_button(context):
    # click on add campaign button
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'campaign_create')
    context.driver.execute_script("arguments[0].click();", button)


@then('add campaign name sales, then click on add')
def add_campaign(context):
    # add campaign name
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'campaign_name').send_keys("campaign sales")

    # click on add button on pop-up
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'add_campaign')
    context.driver.execute_script("arguments[0].click();", button)
