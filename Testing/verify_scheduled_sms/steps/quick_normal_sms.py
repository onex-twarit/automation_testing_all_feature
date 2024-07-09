from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from behave import *
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.by import By


@then('go to New SMS')
def go_to_new_sms(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'new_sms').click()  # go to NEW SMS


@then('go to Quick English SMS')
def go_to_quick_sms(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, 'quick_eng_sms_title')
    context.driver.execute_script("arguments[0].click();", button)  # go to quick english SMS


@then('add campaign for normal SMS')
def add_campaign_normal_sms(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'add_campaign_button')
    context.driver.execute_script("arguments[0].click();",
                                  button)  # click on add campaign button on campaign name field

    time.sleep(0.5)
    context.driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/input').send_keys(
        "quick normal")  # campaign name
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'campaign_desc').send_keys("Desc")  # description
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'add_campaign').click()  # click on add button


@then('select sender ID')
def add_sender_id(context):
    temp = context.driver.find_element(By.ID, 'sender_id')  # select sender ID
    select = Select(temp)
    select.select_by_visible_text("123456")


@then('add recipients and select group')
def add_recipients_and_group(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'recipient_numbers').send_keys(9950500435)

    time.sleep(0.5)
    context.driver.find_element(By.ID, 'groupDropdown').send_keys("group one(1)")  # adding group


@then('insert template')
def insert_template(context):
    time.sleep(1)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(1)
    context.driver.find_element(By.ID, 'insert_template').click()  # go to insert template

    time.sleep(1)
    action = (ActionChains(context.driver))
    type = context.driver.find_element(By.ID, 'template_type_id')  # select template type
    action.move_to_element(type).click().perform()

    time.sleep(1)
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


@then('click on send then on send now')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'send')
    context.driver.execute_script("arguments[0].click();", button)  # click on send button

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'confirm_send_sms')
    context.driver.execute_script("arguments[0].click();", button)  # click on send now button


@then('go to reports')
def go_to_reports(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'menu_report')
    context.driver.execute_script("arguments[0].click();", button)  # click on reports from left menu


@then('then on scheduled campaigns tab, select TUC')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'pills-campaign-tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    context.driver.find_element(By.ID, 'tuc-report').send_keys("ICICIAdmin(2005)")


@then('click on search')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "search")
    context.driver.execute_script("arguments[0].click();", button)


@then('verify the quick normal SMS')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, "//div[contains(text(),'quick normal')]/following::td[3]").text
    if text == "-":
        assert True, "Test Passed"
    else:
        assert False, "scheduled campaign -----> Failed"


@then('go to MIS tab, click on total counts')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'pills-mis-data-tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # scroll down

    time.sleep(1)
    button = context.driver.find_element(By.XPATH, '//*[@id="total_msg_count"]/a')
    context.driver.execute_script("arguments[0].click();", button)  # click on total counts

    time.sleep(1)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)  # click on search


@then('find the quick normal campaign name and verify')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "//div[contains(text(),'quick normal')]/following::td[3]").text
    if text == "-":
        assert True, "Test Passed"
    else:
        assert False, "MIS(WEB) -----> Failed"
