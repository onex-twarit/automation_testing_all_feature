from behave import *
import time
from selenium.webdriver.common.by import By


@then('add campaign name loanuser, then click on add')
def add_campaign(context):
    # add campaign name
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'campaign_name').send_keys("campaign loanuser")

    # click on add button on pop-up
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'add_campaign')
    context.driver.execute_script("arguments[0].click();", button)
