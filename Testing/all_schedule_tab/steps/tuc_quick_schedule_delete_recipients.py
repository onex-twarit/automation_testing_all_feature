from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then('select campaign name for ICICIAdmin')
def step_impl(context):
    # select campaign name from dropdown
    time.sleep(0.5)
    select_name = context.driver.find_element(By.ID, 'campaign_name')
    select = Select(select_name)
    select.select_by_visible_text("all schedule campaign(2370)")
