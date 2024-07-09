from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then('add recipients for iciciadmin')
def add_recipients(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'recipient_numbers').send_keys("6262923191")


@then('select campaign for ICICIAdmin')
def select_campaign(context):
    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, "campaign_name"))
    select.select_by_visible_text('campaign iciciadmin(2577)')


@then('click on view details with TUC name \'ICICIAdmin\'')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, "//td[contains(text(),'ICICIAdmin')]/following-sibling::td[26]/a")
    context.driver.execute_script("arguments[0].click();", button)


@then('store mobile number, uuid, sender ID for ICICIAdmin')
def step_impl(context):
    time.sleep(1)
    context.uuid = context.driver.find_element(By.XPATH,
                                               "//td[contains(text(),'ICICIAdmin')]/following-sibling::td[1]").text

    time.sleep(1)
    context.sender_id = context.driver.find_element(By.XPATH,
                                                    "//td[contains(text(),'ICICIAdmin')]/following-sibling::td[2]").text

    time.sleep(1)
    context.mobile_num = context.driver.find_element(By.XPATH,
                                                     "//td[contains(text(),'ICICIAdmin')]/following-sibling::td[3]").text


@then('go to search tab select ICICIAdmin TUC')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "pills-search-tab")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    context.driver.find_element(By.ID, "tuc-report").send_keys("ICICIAdmin(2005)")
