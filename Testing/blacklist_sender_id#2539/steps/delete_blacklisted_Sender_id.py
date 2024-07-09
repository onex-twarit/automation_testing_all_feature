from behave import *
import time
from selenium.webdriver.common.by import By


@then('click on show button, delete the added sender ID')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="show_sender_blacklist"]')
    context.driver.execute_script("arguments[0].click();", button)  # click on show button

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="delete"]/img')
    context.driver.execute_script("arguments[0].click();", button)  # click on delete icon

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="delete"]')
    context.driver.execute_script("arguments[0].click();", button)  # on warning po-up click delete
