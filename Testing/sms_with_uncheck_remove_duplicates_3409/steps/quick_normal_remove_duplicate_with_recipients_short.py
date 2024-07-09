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
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="new_sms"]')
    context.driver.execute_script("arguments[0].click();", button)  # go to new sms button


@then('go to quick sms')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'quick_eng_sms_title')
    context.driver.execute_script("arguments[0].click();", button)


@then('select campaign and sender ID')
def step_impl(context):
    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, 'campaign_name'))
    select.select_by_visible_text("remove duplicates(2593)")

    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, 'sender_id'))
    select.select_by_visible_text("123456")


@then('add recipients')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="recipient_numbers"]').send_keys("6375418252\n")

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="recipient_numbers"]').send_keys("6375418252\n")

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="recipient_numbers"]').send_keys("9950500435\n")


@then('uncheck remove duplicate box')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.NAME, 'duplicate_check')
    context.driver.execute_script("arguments[0].click();", button)


@then('insert template english short')
def step_impl(context):
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
    select.select_by_visible_text('Dropdown')

    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, 'modal_template_id'))
    select.select_by_visible_text('English Short')

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'insert_template_to_msg')
    context.driver.execute_script("arguments[0].click();", button)  # click on select button


@then('click on send')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'send')
    context.driver.execute_script("arguments[0].click();", button)  # click on send button


@then('check duplicates on confirmation window')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       "//label[text()='Duplicate Numbers'][1]/following-sibling::div/p").text
    if text == "0":
        assert True, "Test passed"
    else:
        assert False, "Test failed"


@then('check valid numbers on confirmation window for short template')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       "//label[text()='Valid Numbers'][1]/following-sibling::div/p").text
    if text == "3":
        assert True, "Test passed"
    else:
        assert False, "Test failed"


@then('then send now')
def step_impl(context):
    time.sleep(1)
    context.credits = context.driver.find_element(By.XPATH,
                                                  "//label[text()='Total Required SMS Credits'][1]/following-sibling::div/p").text
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'confirm_send_sms')
    context.driver.execute_script("arguments[0].click();", button)  # click on send now button


@then('click on New SMS')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'new_sms')
    context.driver.execute_script("arguments[0].click();", button)  # click on new sms button


@then('verify deducted credits for short template')
def step_impl(context):
    # verifying the credits
    time.sleep(2)
    new_avail_bal = context.driver.find_element(By.XPATH, '//*[@id="available_credits"]').text
    context.new_avail_balance = int(str(new_avail_bal).replace(",", ""))

    assert context.available_bal == int(context.credits) + context.new_avail_balance
