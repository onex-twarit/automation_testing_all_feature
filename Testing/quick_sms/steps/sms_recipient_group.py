from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


# Login to tuc – new sms – quick sms – send sms using recipients and group –
# split schedule – send – verify numbers – verify credits – close.

@given('Launch the browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@then('open login page')
def step_impl(context):
    context.driver.get('http://localhost:8000/index')


@then('Enter user name and password for tuc')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("ICICIAdmin")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("password")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="login_button"]').click()


@then('open dashboard page tuc')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, "//*[@id='dashboard_title']").text
    if text == "Dashboard":
        assert True, "Test Passed"

    # checking for total available credits
    time.sleep(2)
    avail_balance = context.driver.find_element(By.XPATH, '//*[@id="available_credits"]').text
    context.available_bal = int(str(avail_balance).replace(",", ""))


@then('go to new sms then to quick sms')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="new_sms"]').click()  # go to new sms button
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="quick_eng_sms_title"]').click()  # go to quick english sms button
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="pills-campaign-tab"]').click()  # go to quick english SMS tab


@then('add recipients and group, uncheck remove dup then check split schedule')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="recipient_numbers"]').send_keys(9876543210)  # add recipients

    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="groupDropdown"]').send_keys("new test(3)")  # adding group

    time.sleep(2)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[1]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # uncheck remove duplicates

    # template add
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="insert_template"]').click()  # go to insert template

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="template_type_id"]').send_keys(
        "Service Implicit(2)")  # select template type

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="template_name"]').send_keys("One Variable")  # select template name

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="insert_template_to_msg"]').click()  # click on select button

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[6]/div[1]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # check schedule sms

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[6]/div[2]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # check multiple campaigns

    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="sms_body"]/div[7]/div[2]/div[2]/input').send_keys(4)  # sms count


@then('send it and then verify numbers and credits')
def step_impl(context):
    # click on send button
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'send')
    context.driver.execute_script("arguments[0].click();", button)  # click on send button

    # on warning window click on yes
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'proceed')
    context.driver.execute_script("arguments[0].click();", button)

    # on split confirmation window ---->

    # verify for the numbers
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '//*[@id="bd-example-modal-lg"]/div/div/div[2]/table/tbody/tr[3]/th[2]').text
    if text == 4:
        assert True, "Test Passed"

    # and credit check
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '//*[@id="bd-example-modal-lg"]/div/div/div[2]/table/tbody/tr[3]/th[3]').text
    if text == 4:
        assert True, "Test Passed"

    # proceed button
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'confirm_send_sms')
    context.driver.execute_script("arguments[0].click();", button)

    # new sms button
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'new_sms')
    context.driver.execute_script("arguments[0].click();", button)

    # verifying the credits
    time.sleep(2)
    new_avail_bal = context.driver.find_element(By.XPATH, '//*[@id="available_credits"]').text
    context.new_avail_balance = int(str(new_avail_bal).replace(",", ""))

    assert context.available_bal == 4 + context.new_avail_balance


@then('close the browser')
def step_impl(context):
    time.sleep(4)
    context.driver.close()
