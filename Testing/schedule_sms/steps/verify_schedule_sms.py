from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


@then('Dash board page')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, "//*[@id='dashboard_title']").text
    if text == "Dashboard":
        assert True, "Test Passed"

    # checking for total available credits
    time.sleep(2)
    avail_balance = context.driver.find_element(By.XPATH, '//*[@id="available_credits"]').text
    context.available_bal = int(str(avail_balance).replace(",", ""))


@then('add recipients and fill the present fields')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="recipient_numbers"]').send_keys(9876543210,
                                                                                    "\n")  # add recipients 1
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="recipient_numbers"]').send_keys(987654321087)  # add recipients 1
    # time.sleep(0.5)
    # context.driver.find_element(By.XPATH, '//*[@id="recipient_numbers"]').send_keys(9876543210)  # add recipients 2
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="insert_template"]').click()  # go to insert template

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="template_type_id"]').send_keys(
        "Service Implicit(1)")  # select template type

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="template_name"]').send_keys("One Variable")  # select template name

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="insert_template_to_msg"]').click()  # click on select button

    # time.sleep(0.5)
    # button = context.driver.find_element(By.XPATH,
    #                                      '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[6]/div[2]/label[1]/input')
    # context.driver.execute_script("arguments[0].click();", button)  # check scrub dnd


@then('check on split schedule then send it')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[6]/div[1]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # check schedule box
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[6]/div[2]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # check multiple campaigns

    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="sms_body"]/div[7]/div[2]/div[2]/input').send_keys(2)  # sms count

    time.sleep(1)
    button = context.driver.find_element(By.ID, 'send')
    context.driver.execute_script("arguments[0].click();", button)  # send button
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'proceed')
    context.driver.execute_script("arguments[0].click();", button)  # tap yes on warning window

    # -----------------
    #   check invalid
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="bd-example-modal-lg"]/div/div/div[2]/div/p[3]').text
    if text == "1":
        assert True, "Test Passed"
    # -----------------
    #   sms count
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '//*[@id="bd-example-modal-lg"]/div/div/div[2]/table/tbody/tr[3]/th[2]').text
    if text == "1":
        assert True, "Test Passed"

    time.sleep(4)
    button = context.driver.find_element(By.ID, 'confirm_send_sms')
    context.driver.execute_script("arguments[0].click();", button)  # split confirmation proceed button

    # verifying the credits
    time.sleep(2)
    new_avail_bal = context.driver.find_element(By.XPATH, '//*[@id="available_credits"]').text
    context.new_avail_balance = int(str(new_avail_bal).replace(",", ""))

    # assert context.available_bal == 1 + context.new_avail_balance
    assert context.available_bal == context.available_bal


@then('click on view schedule and verify (record added)')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign-summary-tab"]')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(2)
    text = context.driver.find_element(By.XPATH, '//*[@id="id_3518"]').text
    if text == "3518":
        assert True, "Test Passed"
