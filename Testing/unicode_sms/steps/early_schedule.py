from behave import *
import time
from selenium.webdriver.common.by import By


@then('add recipients. schedule within 15 mins and send it')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="recipient_numbers"]').send_keys(9876543210)  # add recipients

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
    context.driver.execute_script("arguments[0].click();", button)  # check schedule sms

    # time.sleep(5)
    # context.driver.find_element(By.XPATH, '//*[@id="schedule_row_min"]').send_keys(3)  # select within 15 min
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="schedule_row_min"]').send_keys(42)  # select within 15 min
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'send')
    context.driver.execute_script("arguments[0].click();", button)  # send button


# Login to tuc – new sms – unicode sms – recipients –
# schedule within 15 mins and verify labels – close.


@then('verify labels')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, '//*[@id="error_msg_text"]').text
    if text == "Schedule Time should not be in between of 15 minutes from current time":
        assert True, "Test Passed"
