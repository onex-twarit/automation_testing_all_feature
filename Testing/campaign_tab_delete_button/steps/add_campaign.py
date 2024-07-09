from behave import *
import time
from selenium.webdriver.common.by import By


@then('click on \'Add Campaign\' button')
def click_Add_Campaign(context):
    # click on add campaign button
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'campaign_create')
    context.driver.execute_script("arguments[0].click();", button)


@then('enter quick campaign name')
def quick_campaign_name(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'campaign_name').send_keys("quick campaign")


@then('enter new quick campaign name')
def quick_campaign_name(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'campaign_name').send_keys("new quick campaign")


@then('enter description')
def campaign_description(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'campaign_desc').send_keys("desc")


@then('click on add button')
def click_add_button(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'add_campaign')
    context.driver.execute_script("arguments[0].click();", button)


@then('enter unicode campaign name')
def quick_campaign_name(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'campaign_name').send_keys("unicode campaign")


@then('enter new unicode campaign name')
def quick_campaign_name(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'campaign_name').send_keys("new unicode campaign")


@then('enter dynamic campaign name')
def quick_campaign_name(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'campaign_name').send_keys("dynamic campaign")


@then('enter multiple dynamic campaign name')
def quick_campaign_name(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'campaign_name').send_keys("multiple dynamic campaign")


@then('enter campaign name')
def quick_campaign_name(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'campaign_name').send_keys("camp campaign")

