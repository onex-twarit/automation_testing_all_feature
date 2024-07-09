from behave import *
import time
from selenium.webdriver.common.by import By


@then('select group')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="groupDropdown"]').send_keys("new test(3)")  # adding group

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="insert_template"]').click()  # go to insert template

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="template_type_id"]').send_keys(
        "Service Implicit(2)")  # select template type

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="template_name"]').send_keys("One Variable")  # select template name

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="insert_template_to_msg"]').click()  # click on select button


@then('check on schedule sms within 15 min')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[6]/div[1]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # check schedule sms

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="schedule_row_min"]').send_keys(34)  # select within 15 min
