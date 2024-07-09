from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


@given('Launch the browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@then('open loginnnn.py page')
def step_impl(context):
    context.driver.get('http://localhost:8000/index')


@then('Enter user name and password')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("ICICIAdmin")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Pass123@")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="login_button"]').click()


@then('open dashboard page')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, "//*[@id='dashboard_title']").text
    if text == "Dashboard":
        assert True, "Test Passed"

    # checking for total available credits
    time.sleep(2)
    avail_balance = context.driver.find_element(By.XPATH, '//*[@id="available_credits"]').text
    context.available_bal = int(str(avail_balance).replace(",", ""))


@then('go to NEW SMS then to quick unicode sms')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="new_sms"]').click()  # go to new sms button
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="uicode_sms_title"]').click()  # go to unicode sms button
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="pills-campaign-tab"]').click()  # go to unicode sms tab


@then('add recipients, fill the present fields, schedule and split')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="recipient_numbers"]').send_keys(9876543210)  # add recipients 1

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="insert_template"]').click()  # go to insert template

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="template_type_id"]').send_keys(
        "Service Implicit(2)")  # select template type

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="template_name"]').send_keys("New Hindi")  # select template name

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="insert_template_to_msg"]').click()  # click on select button

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="dest_language"]').send_keys("Hindi")  # select Hindi

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[5]/div[1]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # check multipart

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[5]/div[2]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # check unicode

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[6]/div[1]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # check schedule box

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[6]/div[2]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # check multiple campaigns

    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="sms_body"]/div[7]/div[2]/div[2]/input').send_keys(1)  # sms count

    time.sleep(1)
    button = context.driver.find_element(By.ID, 'send')
    context.driver.execute_script("arguments[0].click();", button)  # send button

    time.sleep(1)
    button = context.driver.find_element(By.ID, 'proceed')
    context.driver.execute_script("arguments[0].click();", button)  # tap yes on warning window


# Login to tuc – new sms – unicode sms – send sms using recipients –
# split schedule – send – verify numbers – verify credits – close.

@then('verify number and credits')
def step_impl(context):
    # verify number
    time.sleep(2)
    text = context.driver.find_element(By.XPATH,
                                       '//*[@id="bd-example-modal-lg"]/div/div/div[2]/table/tbody/tr[3]/th[2]').text
    if text == 2:
        assert True, "Test Passed"

    time.sleep(1)
    button = context.driver.find_element(By.ID, 'confirm_send_sms')
    context.driver.execute_script("arguments[0].click();", button)  # proceed button

    time.sleep(1)
    button = context.driver.find_element(By.ID, 'new_sms')
    context.driver.execute_script("arguments[0].click();", button)  # new sms button

    # verifying the credits
    time.sleep(2)
    new_avail_bal = context.driver.find_element(By.XPATH, '//*[@id="available_credits"]').text
    context.new_avail_balance = int(str(new_avail_bal).replace(",", ""))

    assert context.available_bal == 2 + context.new_avail_balance


@then('close')
def step_impl(context):
    time.sleep(4)
    context.driver.close()
