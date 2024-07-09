from behave import *
from selenium.webdriver.common.by import By
import time


@then('verify deducted credits for long template split')
def step_impl(context):
    # verifying the credits
    time.sleep(2)
    new_avail_bal = context.driver.find_element(By.XPATH, '//*[@id="available_credits"]').text
    context.new_avail_balance = int(str(new_avail_bal).replace(",", ""))

    assert context.available_bal == 4 + context.new_avail_balance



