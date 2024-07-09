from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then('open dashboard')
def open_dashboard(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "//*[@id='dashboard_title']").text
    if text == "Dashboard":
        assert True, "Test Passed"

    time.sleep(1)
    avail_balance = context.driver.find_element(By.XPATH, '//*[@id="available_credits"]').text
    context.available_bal = int(str(avail_balance).replace(",", ""))


@then('go to NEW SMS')
def go_to_new_sms(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="new_sms"]')
    context.driver.execute_script("arguments[0].click();", button)  # go to new sms button


@then('go to quick sms')
def go_to_quick_sms(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'quick_eng_sms_title')
    context.driver.execute_script("arguments[0].click();", button)


@then('select campaign and sender ID')
def select_campaign_and_senderid(context):
    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, 'campaign_name'))
    select.select_by_visible_text("scrub dnd campaign(2595)")

    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, 'sender_id'))
    select.select_by_visible_text("123456")


@then('add recipients')
def add_recipients(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="recipient_numbers"]').send_keys("9542886182\n")

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="recipient_numbers"]').send_keys("8605493727\n")

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="recipient_numbers"]').send_keys("6375418252\n")


@then('insert template english short with search type')
def template_english_short_search(context):
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
    select.select_by_visible_text('Search')

    time.sleep(0.5)
    select_tuc = context.driver.find_element(By.ID, 'modal_template_id')  # search for template

    time.sleep(0.5)
    select_tuc.send_keys("English S")
    time.sleep(0.5)
    select_tuc.send_keys(Keys.ARROW_DOWN)  # find from the suggestions
    time.sleep(0.5)
    select_tuc.send_keys(Keys.RETURN)

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'insert_template_to_msg')
    context.driver.execute_script("arguments[0].click();", button)  # click on select button


@then('check scrub DND')
def check_scrub_dnd(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.NAME, 'scrub_dnd')
    context.driver.execute_script("arguments[0].click();", button)  # check scrub DND


@then('click on send')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'send')
    context.driver.execute_script("arguments[0].click();", button)  # click on send button


@then('check DND numbers on confirmation window')
def dnd_numbers(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       "//label[text()='DND Numbers'][1]/following-sibling::div/p").text
    if text == "2":
        assert True, "Test passed"
    else:
        assert False, "Test failed"


@then('check valid numbers on confirmation window')
def valid_numbers(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       "//label[text()='Valid Numbers'][1]/following-sibling::div/p").text
    if text == "1":
        assert True, "Test passed"
    else:
        assert False, "Test failed"


@then('total required SMS credits')
def total_required_credits(context):
    time.sleep(1)
    context.credits = context.driver.find_element(By.XPATH,
                                                  "//label[text()='Total Required SMS Credits'][1]/following-sibling::div/p").text


@then('then send now')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'confirm_send_sms')
    context.driver.execute_script("arguments[0].click();", button)  # click on send now button


@then('click on New SMS')
def click_new_sms(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'new_sms')
    context.driver.execute_script("arguments[0].click();", button)  # click on new sms button


@then('verify deducted credits')
def verify_deducted_credits(context):
    # verifying the credits
    time.sleep(1)
    new_avail_bal = context.driver.find_element(By.XPATH, '//*[@id="available_credits"]').text
    context.new_avail_balance = int(str(new_avail_bal).replace(",", ""))

    assert context.available_bal == int(context.credits) + context.new_avail_balance
