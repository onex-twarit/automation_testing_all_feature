from selenium.webdriver import ActionChains, Keys

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime, timezone, date

import pytz
from behave import *
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

service = Service(executable_path='/home/twarit/Downloads/chromedriver-linux64/chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


@given(u'launch chrome browser')
def ChromeBrowserLaunch(context):
    try:
        time.sleep(0.5)
        context.driver = driver
        context.driver.maximize_window()
    except NameError:
        print("Chrome browser did not open")
    else:
        print("Chrome browser open successfully")


@when(u'open Onextel Homepage "{homepage}"')
def OpenHomepage(context, homepage):
    context.driver.maximize_window()
    try:
        context.driver.get(homepage)
    except NameError:
        print(f"{homepage} unable to load")
    else:
        print(f"{homepage} loaded successfully")


@then(u'Enter Username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.maximize_window()
    time.sleep(1)
    context.driver.find_element(By.ID, "email").send_keys(user)
    context.driver.find_element(By.ID, "password").send_keys(pwd)


@then(u'Check Terms And Conditions Check Box is preselected')
def step_impl(context):
    checkbox = context.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[3]/label/input").is_selected()
    if checkbox:
        assert True, f"Check box is selected"
    else:
        assert False, f"Check box is not selected"


@then(u'Click on login button')
def step_impl(context):
    context.driver.implicitly_wait(20)
    button = context.driver.find_element(By.ID, "login_button")
    context.driver.execute_script("arguments[0].click();", button)


def clickables(value):
    button = driver.find_element(By.XPATH, value)
    driver.execute_script("arguments[0].click();", button)


# -----------------------------------------------------------------------------

@then('go to NEW SMS then to quick english sms')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="new_sms"]').click()  # go to new sms button
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="quick_eng_sms_title"]').click()  # go to quick english sms button
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="pills-campaign-tab"]').click()  # go to quick english SMS tab


@then('add recipients')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="recipient_numbers"]').send_keys(9462747020, "\n")  # add recipients
    context.driver.find_element(By.XPATH, '//*[@id="recipient_numbers"]').send_keys(6375418252)
    # time.sleep(1)
    # context.driver.find_element(By.XPATH, '//*[@id="new_sms"]').click()


@then('present fields to be filled')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="groupDropdown"]').send_keys("scrub dnd group (3)")  # adding group

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


@then('check on schedule sms, split into campaigns and click on send')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.NAME, 'schedule_check')
    context.driver.execute_script("arguments[0].click();", button)  # check schedule box

    time.sleep(1)
    tz = pytz.timezone("Asia/Kolkata")
    # curr = datetime.now(tz).strftime("%H:%M:%S")
    curr = "23:59:59"
    print(curr)

    # today_date = date.today()
    # print("date todaygrgfgfgf >>", today_date)

    # select = Select(context.driver.find_element(By.ID, 'schedule_row_hour'))
    # select.select_by_visible_text("23")
    #
    # select = Select(context.driver.find_element(By.ID, 'schedule_row_min'))
    # select.select_by_visible_text("59")

    hours = curr[0:2]
    minutes = curr[3:5]
    print("Current Hour is:" + hours)
    print("Current Minute is:" + minutes)
    min = int(minutes)
    # min = min + 17
    print(min)
    first_option_day = Select(context.driver.find_element(By.ID, 'schedule_row_day')).first_selected_option.text
    print("1-------", first_option_day)

    if hours == "23" and min == "59":
        hours = str(00)
        min = min + 17
        today_date = date.today()
        print("date today >>", today_date)
        day = today_date.day + 1
        int_day_to_str = str(day)
        month = today_date.month
        int_month_to_str = str(month)
        year = today_date.year
        int_year_to_str = str(year)
        first_option_day = Select(context.driver.find_element(By.ID, 'schedule_row_day')).first_selected_option.text
        print("2-------", first_option_day)
        if len(int_day_to_str) == 1:
            two_digit_day_num = '0' + int_day_to_str
            print("new date", two_digit_day_num)

            time.sleep(0.5)
            select = Select(context.driver.find_element(By.ID, 'schedule_row_day'))
            select.select_by_visible_text(two_digit_day_num)
        first_option_day = Select(context.driver.find_element(By.ID, 'schedule_row_day')).first_selected_option.text
        print("3-------", first_option_day)
        if len(int_month_to_str) == 1:
            two_digit_month_num = '0' + int_month_to_str
            print("new month", two_digit_month_num)

            time.sleep(0.5)
            select = Select(context.driver.find_element(By.ID, 'schedule_row_day'))
            select.select_by_visible_text(two_digit_month_num)

        if hours == "23" and minutes == "59":
            hours = str(00)
            min = min + 17

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

    time.sleep(1)
    button = context.driver.find_element(By.ID, 'new_sms')
    context.driver.execute_script("arguments[0].click();", button)  # send button

    n = 1 / 0
    print(n)


@then('again on new window click on proceed')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="confirm_send_sms"]').click()  # proceed button "proceed"

    time.sleep(1)
    button = context.driver.find_element(By.ID, 'send')
    context.driver.execute_script("arguments[0].click();", button)  # send button


# @then('check if message is sent')
# def step_impl(context):
#     time.sleep(2)
#     text = context.driver.find_element(By.XPATH, '//*[@id="dashboard"]/div[2]/div[1]/h4').text
#     if text == "Following Splits are Successfully Scheduled!!":
#         assert True, "Test Passed"
# -----------------------------------------------------------------------------

@then(u'Close driver window')
def step_impl(context):
    time.sleep(0.5)
    context.driver.quit()

# @then('new window for confirmation')
# def step_impl(context):
#     time.sleep(2)
#     context.driver.find_element(By.XPATH, '//*[@id="proceed"]').click()  # confirmation button "yes"


# def single_to_double():
#     user_input = "7"
#
#     if len(user_input) == 1:
#         two_digit_num = '0' + user_input
#
#         print(int(two_digit_num) + 1)
#     else:
#         print(user_input)
#
#
# #
# #
# single_to_double()
