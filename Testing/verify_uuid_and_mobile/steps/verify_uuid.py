from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

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
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Pass1234@")
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


@then('Select campaign name as \'uuid and mobile check\', then sender ID')
def step_impl(context):
    time.sleep(0.5)
    select_name = Select(context.driver.find_element(By.XPATH, '//*[@id="campaign_name"]'))  # select campaign name
    select_name.select_by_visible_text('uuid and mobile check(2203)')

    # time.sleep(0.5)
    # context.driver.execute_script("arguments[0].click();", button)  # click on search


@then('add number in recipients, then select template, click on select')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="recipient_numbers"]').send_keys(9950500435)

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
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/a[5]/p').click()  # go to reports

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="pills-mis-data-tab"]').click()  # go to MIS tab

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="search"]')
    context.driver.execute_script("arguments[0].click();", button)  # click on search button

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div/table/tbody/tr[24]/td[20]/a')
    context.driver.execute_script("arguments[0].click();", button)  # click on day/time data


@then('find the latest entry and click under the action')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, '//*[@id="search"]')
    context.driver.execute_script("arguments[0].click();", button)  # click on search button

    time.sleep(2)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[3]/div/table/tbody/tr[2]/td[27]/a/img')
    context.driver.execute_script("arguments[0].click();", button)  # click under the action


@then('take the mobile num and log out TUC')
def step_impl(context):
    time.sleep(2)
    context.uuid = context.driver.find_element(By.XPATH,
                                               '//*[@id="customers"]/tbody/tr[2]/td[3]').is_displayed()  # uuid
    time.sleep(2)
    context.mob_num = context.driver.find_element(By.XPATH,
                                                  '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div/div[3]/table/tbody/tr[2]/td[5]').is_displayed()  # mobile number

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'dropdown-caret')
    context.driver.execute_script("arguments[0].click();", button)  # go to profile dropdown

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'log-out')
    context.driver.execute_script("arguments[0].click();", button)  # click on log out


@then('Enter user name and password for SA')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("onexsa")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Pass123@")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="login_button"]').click()


@then('open dashboard page, go to Report, go to search tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "//*[@id='dashboard_title']").text
    if text == "Dashboard":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"

    time.sleep(1.5)
    context.driver.find_element(By.XPATH, '//*[@id="menu_master_report"]/p').click()  # go to Report

    time.sleep(1.5)
    button = context.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/ul/li[3]/a')
    context.driver.execute_script("arguments[0].click();", button)  # go to search tab


@then('enter the mobile number in the field, click on search')
def step_impl(context):
    time.sleep(1.5)
    context.driver.find_element(By.XPATH, '//*[@id="pills-daily-summary"]/div[1]/div/div[3]/input').send_keys(
        9950500435)

    time.sleep(1.5)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)  # click on search


@then('verify the details')
def step_impl(context):
    time.sleep(1)
    context.uuid_verify = context.driver.find_element(By.XPATH,
                                                      '//*[@id="pills-daily-summary"]/div[2]/table/tbody/tr[2]/td[1]/a').is_displayed()
    assert context.uuid == context.uuid_verify

    time.sleep(1)
    context.num_verify = context.driver.find_element(By.XPATH,
                                                     '//*[@id="pills-daily-summary"]/div[2]/table/tbody/tr[2]/td[2]').is_displayed()
    assert context.mob_num == context.num_verify


@then('close')
def step_impl(context):
    time.sleep(1)
    context.driver.close()
