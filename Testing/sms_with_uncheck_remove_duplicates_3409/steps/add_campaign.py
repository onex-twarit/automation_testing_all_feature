from behave import *
import time
from selenium.webdriver.common.by import By


@then('click campaign')
def tuc_click_campaign(context):
    # in tuc click on campaign
    time.sleep(1)
    button = context.driver.find_element(By.XPATH, '//*[@id="menu_campaigns"]/p')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on add campaign button')
def add_campaign_button(context):
    # click on add campaign button
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'campaign_create')
    context.driver.execute_script("arguments[0].click();", button)


@then('add campaign name, then click on add')
def campaign_popup(context):
    # add campaign name
    time.sleep(1)
    context.driver.find_element(By.ID, 'campaign_name').send_keys("remove duplicates")

    # click on add button on pop-up
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'add_campaign')
    context.driver.execute_script("arguments[0].click();", button)
