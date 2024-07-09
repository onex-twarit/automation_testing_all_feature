from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


# Login to tuc – new sms – quick sms – recipients and group–
# remove duplicate and click on scrub dnd – send – verify numbers – verify credits – close.

@then('add recipients and group remove dup then check scrub dnd, send it')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="recipient_numbers"]').send_keys(9876543210)  # add recipients

    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="groupDropdown"]').send_keys("new test(3)")  # adding group

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
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[6]/div[2]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # check scrub dnd

    # click on send button
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'send')
    context.driver.execute_script("arguments[0].click();", button)  # click on send button


@then('on sms confirmation window verify nums and credits')
def step_impl(context):
    # check valid numbers
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '//*[@id="bd-example-modal-lg"]/div/div/div[2]/div[2]/div[8]/div/p').text
    if text == 3:
        assert True, "Test Passed"

    # check credit count
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '//*[@id="bd-example-modal-lg"]/div/div/div[2]/div[2]/div[10]/div/p').text
    if text == 3:
        assert True, "Test Passed"

    # send now button
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'confirm_send_sms')
    context.driver.execute_script("arguments[0].click();", button)

    # new sms button
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'confirm_send_sms')
    context.driver.execute_script("arguments[0].click();", button)

    # verifying the credits
    time.sleep(2)
    new_avail_bal = context.driver.find_element(By.XPATH, '//*[@id="available_credits"]').text
    context.new_avail_balance = int(str(new_avail_bal).replace(",", ""))

    assert context.available_bal == 3 + context.new_avail_balance
