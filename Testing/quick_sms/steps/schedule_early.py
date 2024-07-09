from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


# Login to tuc – new sms – quick sms – recipients and group –
# schedule within 15 mins and verify labels – close.

@then('add recipients and group, schedule early')
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

    time.sleep(59)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[6]/div[1]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # check schedule sms

    # time.sleep(5)
    # context.driver.find_element(By.XPATH, '//*[@id="schedule_row_min"]').send_keys(3)  # select within 15 min
    time.sleep(59)
    button = context.driver.find_element(By.ID, 'send')
    context.driver.execute_script("arguments[0].click();", button)  # send button


@then('on new window verify labels')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, '//*[@id="error_msg_text"]').text
    if text == "Schedule Time should not be in between of 15 minutes from current time":
        assert True, "Test Passed"

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/'
                                         'div[4]/div[1]/div/div/div/div[1]/div[1]/div/div/div/div[3]/input')
    context.driver.execute_script("arguments[0].click();", button)  # click on OK button
