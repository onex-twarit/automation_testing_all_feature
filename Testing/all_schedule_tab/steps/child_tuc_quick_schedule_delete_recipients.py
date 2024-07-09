from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pytz import timezone
import datetime

current_time = datetime.datetime.now()
from datetime import datetime

now = datetime.now()


@then('click on New SMS button')
def click_new_sms(context):
    # click on new sms button and select type
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'new_sms')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on quick english sms')
def quick_sms(context):
    # click on quick english SMS
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'quick_eng_sms_title')
    context.driver.execute_script("arguments[0].click();", button)


@then('select campaign name for ChildOne')
def select_campaign_name(context):
    # select campaign name from dropdown
    time.sleep(1)
    select_name = context.driver.find_element(By.ID, 'campaign_name')
    select = Select(select_name)
    select.select_by_visible_text("all schedule campaign(2369)")


@then('select sender ID')
def select_sender_id(context):
    # select sender ID from dropdown
    time.sleep(1)
    select_name = context.driver.find_element(By.ID, 'sender_id')
    select = Select(select_name)
    select.select_by_visible_text("123456")


@then('add recipients')
def add_recipients(context):
    # add recipients
    time.sleep(1)
    context.driver.find_element(By.ID, 'recipient_numbers').send_keys(9950500435)


@then('insert template')
def insert_template(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="insert_template"]').click()  # go to insert template

    time.sleep(1)
    context.driver.implicitly_wait(30)
    action = (ActionChains(context.driver))
    type = context.driver.find_element(By.ID, 'template_type_id')  # select template type

    action.move_to_element(type).click().perform()

    time.sleep(0.5)
    action.key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).click().perform()

    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, "template_filter_id"))
    select.select_by_visible_text("Search")

    time.sleep(0.5)
    context.driver.find_element(By.ID, 'modal_template_id').send_keys('English Short')

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, "//li[@class='ui-menu-item']/div[text()='English Short']").click()

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'insert_template_to_msg')
    context.driver.execute_script("arguments[0].click();", button)  # click on select button

    time.sleep(0.5)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


@then('check schedule sms box, all schedule')
def schedule_checkbox(context):
    time.sleep(1)
    button = context.driver.find_element(By.NAME, "schedule_check")
    context.driver.execute_script("arguments[0].click();", button)

    curr = datetime.now(timezone("Asia/Kolkata")).strftime("%H:%M:%S")
    print(curr)
    hours = curr[0:2]
    minutes = curr[3:5]
    print("Current Hour is:" + hours)
    print("Current Minute is:" + minutes)
    min = int(minutes)
    min = min + 17
    print(min)
    if min >= 60:
        val = min - 60
        if hours == "23":
            hours = str(00)
            print("Hour is:" + hours)
        else:
            hour = int(hours) + 1
            if hour < 10:
                hours = '0' + str(hour)
                print("Hour is:" + hours)
            else:
                hours = str(hour)
                print("Hour is:" + hours)
        if val <= 9:
            minutes = '0' + str(val)
            print("Minutes is:" + minutes)

        else:
            minutes = str(val)
            print("Minutes is:" + minutes)
    else:
        minutes = str(min)
        print(hours)
        print("Minutes is:" + minutes)
    time.sleep(1)
    select = Select(

        context.driver.find_element(By.XPATH, "//label[text()='Hour'][1]/following-sibling::select"))
    select.select_by_value(hours)
    time.sleep(1)
    select = Select(

        context.driver.find_element(By.XPATH, "//label[text()='Minute'][1]/following-sibling::select"))
    select.select_by_value(minutes)


@then('click on schedule, then on schedule now button, all schedule')
def click_sms_schedule(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'send')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    context.check_time = context.driver.find_element(By.XPATH,
                                                     "//label[contains(text(),'Schedule Time')]/following-sibling::div/p").text

    time.sleep(1)
    button = context.driver.find_element(By.ID, 'confirm_send_sms')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on new sms')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'new_sms')
    context.driver.execute_script("arguments[0].click();", button)


@then('match the time of recent scheduled sms and delete')
def step_impl(context):
    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH, f'//td[contains(text(),"{context.check_time}")]').text
    if text == context.check_time:
        time.sleep(0.5)
        button = context.driver.find_element(By.XPATH, "//button[contains(@id,'delete_button')]")
        context.driver.execute_script("arguments[0].click();", button)

        time.sleep(0.5)
        button = context.driver.find_element(By.ID, 'campaign_sms_confirm_delete_delete')
        context.driver.execute_script("arguments[0].click();", button)
    else:
        assert False, "----->> Failed"
