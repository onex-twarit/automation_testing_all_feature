from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then('open dashboard')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.ID, 'dashboard_title').text
    if text == "Dashboard":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on credits')
def click_credits(context):
    # click on credits from ta
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, '//*[@id="menu_credit_allocation"]/p')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on update credit button')
def click_update_credit(context):
    # click on update credit button
    time.sleep(2)
    button = context.driver.find_element(By.ID, 'updateCredit')
    context.driver.execute_script("arguments[0].click();", button)


@then('fill the present fields')
def update_credit_popup(context):
    # select tuc to give credits
    time.sleep(2)
    select = Select(context.driver.find_element(By.ID, 'select_tuc'))
    select.select_by_visible_text("SBIUser(2012)")

    # click on add-credit button
    time.sleep(2)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[4]/div/div[1]/input')
    context.driver.execute_script("arguments[0].click();", button)

    # pass the amount of credits
    time.sleep(2)
    context.driver.find_element(By.ID, 'credits_amount').send_keys(75000)


@then('click on update')
def click_update(context):
    # on new pop-up, click on update button
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'update_credits')
    context.driver.execute_script("arguments[0].click();", button)
