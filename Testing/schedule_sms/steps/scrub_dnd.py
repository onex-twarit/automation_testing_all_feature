from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


@given('Launch browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@then('open the login page')
def step_impl(context):
    context.driver.get('http://localhost:8000/index')


@then('Enter the user name and password')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("ICICIAdmin")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("password")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="login_button"]').click()


@then('open the dashboard page')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, "//*[@id='dashboard_title']").text
    if text == "Dashboard":
        assert True, "Test Passed"

    # checking for total available credits
    time.sleep(2)
    avail_balance = context.driver.find_element(By.XPATH, '//*[@id="available_credits"]').text
    context.available_bal = int(str(avail_balance).replace(",", ""))


@then('go to NEW SMS then to the quick english sms tuc')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="new_sms"]').click()  # go to new sms button
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="quick_eng_sms_title"]').click()  # go to quick english sms button
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="pills-campaign-tab"]').click()  # go to quick english SMS tab


@then('add two recipients and check on remove duplicate')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="recipient_numbers"]').send_keys(9876543210,
                                                                                    "\n")  # add recipients 1
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="recipient_numbers"]').send_keys(9876543210)  # add recipients 2


# Login to tuc – new sms – quick sms – recipients – remove duplicate and
# click on scrub dnd – send – verify numbers – verify credits – close.


@then('present fields to be filled with check on scrub dnd')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="insert_template"]').click()  # go to insert template

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="template_type_id"]').send_keys(
        "Service Implicit(1)")  # select template type

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="template_name"]').send_keys("One Variable")  # select template name

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="insert_template_to_msg"]').click()  # click on select button

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[6]/div[2]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # check scrub dnd


@then('click on the send')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'send')
    context.driver.execute_script("arguments[0].click();", button)  # send button


@then('then verify for the duplicate num and the credits')
def step_impl(context):
    # checking for duplicate numbers
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '//*[@id="bd-example-modal-lg"]/div/div/div[2]/div[2]/div[5]/div/p').text
    if text == 1:
        assert True, "Test Passed"

    time.sleep(2)
    total_ded = context.driver.find_element(By.XPATH,
                                            '//*[@id="bd-example-modal-lg"]/div/div/div[2]/div[2]/div[10]/div/p').text
    context.total_deductions = int(str(total_ded).replace(",", ""))


@then('then click on the send now button')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'confirm_send_sms')
    context.driver.execute_script("arguments[0].click();", button)  # send now button


@then('then again click on the new sms button')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'confirm_send_sms')
    context.driver.execute_script("arguments[0].click();", button)  # on new window new sms button

    # verifying the credits
    time.sleep(2)
    new_avail_bal = context.driver.find_element(By.XPATH, '//*[@id="available_credits"]').text
    context.new_avail_balance = int(str(new_avail_bal).replace(",", ""))

    assert context.available_bal == 1 + context.new_avail_balance


@then('close browser')
def step_impl(context):
    time.sleep(4)
    context.driver.close()
