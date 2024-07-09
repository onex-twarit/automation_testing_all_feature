import re
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from behave import *
import time
from selenium.webdriver.common.by import By

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


@then('Enter user name and password for TUC')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("tucOne")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Pass123@")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="login_button"]').click()


@then('open dashboard page, go to NEW SMS, then quick english SMS')
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

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="new_sms"]').click()  # go to NEW SMS

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="quick_eng_sms_title"]')
    context.driver.execute_script("arguments[0].click();", button)  # go to quick english SMS


@then('in Campaign name, click on add icon for new campaign')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="add_campaign_button"]')
    context.driver.execute_script("arguments[0].click();",
                                  button)  # click on add campaign button on campaign name field


@then('on new window, fill the present fields, click on Add')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/input').send_keys(
        "quick campaign")  # campaign name
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'campaign_desc').send_keys("Desc")  # description
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'add_campaign').click()  # click on add button


@then('add number in recipients, then select template, click on select')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="recipient_numbers"]').send_keys(9950500435)

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="insert_template"]').click()  # go to insert template

    time.sleep(0.5)
    action = (ActionChains(context.driver))
    type = context.driver.find_element(By.ID, 'template_type_id')  # select template type
    action.move_to_element(type).click().perform()

    time.sleep(1)
    action.key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).click().perform()

    time.sleep(0.5)
    context.driver.find_element(By.ID, 'modal_template_id').send_keys('English Short')

    time.sleep(1)
    context.driver.find_element(By.XPATH, "//li[@class='ui-menu-item']/div[text()='English Short']").click()

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'insert_template_to_msg')
    context.driver.execute_script("arguments[0].click();", button)  # click on select button


@then('click on send button, then click on send now button')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="send"]')
    context.driver.execute_script("arguments[0].click();", button)  # click on send button

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="confirm_send_sms"]')
    context.driver.execute_script("arguments[0].click();", button)  # click on send now button


@then('on new window click on New SMS button')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="confirm_send_sms"]')
    context.driver.execute_script("arguments[0].click();", button)  # click on select button


@then('verify the credits on the same window')
def step_impl(context):
    time.sleep(2)
    total_ded = context.driver.find_element(By.XPATH,
                                            '//*[@id="available_credits"]').text
    context.total_deductions = int(str(total_ded).replace(",", ""))

    assert context.available_bal == context.total_deductions + 1


@then('go to reports, in MIS tab click on the day/time, click on search')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="menu_report"]/img').click()  # go to reports

    time.sleep(0.5)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(1)
    context.driver.find_element(By.XPATH,
                                '//*[@id="customers"]/tbody/tr[28]/td[12]/a').click()  # click on day/time data

    time.sleep(1)
    button = context.driver.find_element(By.XPATH, '//*[@id="search"]')
    context.driver.execute_script("arguments[0].click();", button)  # click on search button


@then('find the latest entry and click under the action')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="view_details_2205"]/img')
    context.driver.execute_script("arguments[0].click();", button)  # click on day/time data


@then('check uuid and status')
def step_impl(context):
    time.sleep(1)
    pattern = r'^[a-zA-Z0-9]+$'
    text = context.driver.find_element(By.XPATH, '//*[@id="customers"]/tbody/tr[2]/td[3]').text  # check uuid

    if re.match(pattern, text):
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed, uuid"

    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="customers"]/tbody/tr[2]/td[12]').text  # check status
    if text == "Delivered" or "Failed" or "Submitted" or "Awaited":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed, status"


@then('close')
def step_impl(context):
    time.sleep(1)
    context.driver.close()
