from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from behave import *
from selenium.webdriver.common.by import By

import time
from pytz import timezone
import datetime
from selenium.webdriver.support.select import Select

current_time = datetime.datetime.now()
from datetime import datetime

now = datetime.now()

service = Service(executable_path='/home/twarit/Downloads/chromedriver-linux64/chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


@given('Launch the browser')
def step_impl(context):
    time.sleep(0.5)
    context.driver = driver
    context.driver.maximize_window()


@then('open login page')
def step_impl(context):
    time.sleep(0.5)
    context.driver.get('http://localhost:8000/index')


@then('Enter user name and password for tuc')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("ICICIAdmin")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Onextel@123")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="login_button"]').click()


@then('open dashboard page')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "//*[@id='dashboard_title']").text
    if text == "Dashboard":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"

    time.sleep(2)
    avail_balance = context.driver.find_element(By.XPATH, '//*[@id="available_credits"]').text
    context.available_bal = int(str(avail_balance).replace(",", ""))


@then('click on new sms, click on multiple dynamic sms')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="new_sms"]').click()  # go to NEW SMS

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'multi_dyn_sms_title')
    context.driver.execute_script("arguments[0].click();", button)  # go to multiple dynamic SMS


@then('upload file')
def step_impl(context):
    time.sleep(1)
    context.driver.switch_to.frame("up_onex_file")
    fileupload = context.driver.find_element(By.ID, 'file1')
    fileupload.send_keys('/home/twarit/Desktop/multiple_dynamic_sms.csv')


@then('add campaign \'multiple dynamic schedule\', fill the present fields, click on Add')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, 'add_campaign_button')
    context.driver.execute_script("arguments[0].click();",
                                  button)  # click on add campaign button on campaign name field

    time.sleep(1)
    context.driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[1]/input').send_keys(
        "multiple dynamic schedule")  # campaign name
    time.sleep(1)
    context.driver.find_element(By.ID, 'campaign_desc').send_keys("Desc")  # description
    time.sleep(1)
    context.driver.find_element(By.ID, 'add_campaign').click()  # click on add button


@then('select column for recipients and template content')
def step_impl(context):
    time.sleep(0.5)
    select = Select(driver.find_element(By.ID, 'recipient_column'))
    select.select_by_visible_text('Mobile')

    time.sleep(0.5)
    select = Select(driver.find_element(By.ID, 'template_content_column'))
    select.select_by_visible_text('Content/Template')


@then('check schedule box')
def step_impl(context):
    time.sleep(2)
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


@then('click on schedule, then on schedule now button')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'send')
    context.driver.execute_script("arguments[0].click();", button)  # click on schedule button

    time.sleep(1)
    button = context.driver.find_element(By.ID, 'confirm_send_sms')
    context.driver.execute_script("arguments[0].click();", button)  # click on schedule now button


@then('click on New SMS')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'new_sms')
    context.driver.execute_script("arguments[0].click();", button)  # click on new sms button


@then('go to Reports, go to MIS tab, click on total counts')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="menu_report"]/p').click()  # go to report tab

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="pills-tab"]/li[1]').click()  # go to MIS tab

    time.sleep(0.5)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div/table/tbody/tr[33]/th[26]/a')
    context.driver.execute_script("arguments[0].click();", button)  # click on total counts in report


@then('search with campaign name \'multiple dynamic schedule\'')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.ID, 'web_camp').send_keys('multiple dynamic schedule')  # search with campaign name

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)  # click on search button


@then('verify with name \'multiple dynamic schedule\'')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[3]/div/table/tbody/tr[2]/td[4]/div').text
    if text == 'multiple dynamic schedule':
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('go to summary tab check all and web')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'pills-summary-tab').click()  # go to summary tab

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)  # click on search button

    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[3]/table/tbody/tr[3]/th[3]').text
    if text == "2":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"

    time.sleep(0.5)
    select = Select(driver.find_element(By.ID, 'source_type_summary'))
    select.select_by_visible_text('WEB')

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)  # click on search button

    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[3]/table/tbody/tr[3]/th[3]').text
    if text == "2":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('go to scheduled campaign, verify \'multiple dynamic schedule\' name')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'pills-campaign-tab')
    context.driver.execute_script("arguments[0].click();", button)  # go to scheduled campaign tab

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)  # click on search button

    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/table/tbody/tr[2]/td[4]/div').text
    if text == "multiple dynamic schedule":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('delete schedule')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/a[1]/img')
    context.driver.execute_script("arguments[0].click();", button)  # go to dashboard

    time.sleep(0.5)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'collapsable_schedule')
    context.driver.execute_script("arguments[0].click();", button)  # click scheduled sms dropdown

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[5]/div[2]/div/table/tbody/tr[2]/td[9]/a/img')
    context.driver.execute_script("arguments[0].click();", button)  # click delete

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'quick_sms_confirm_delete_delete')
    context.driver.execute_script("arguments[0].click();", button)  # click delete on warning pop-up


@then('close')
def step_impl(context):
    time.sleep(0.5)
    context.driver.close()
