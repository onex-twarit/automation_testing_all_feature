from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then('click User Management, go to TUC')
def step_impl(context):  # click on user management
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="menu_users"]/p').click()

    # go to tuc tab
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'tuc_view')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on add tuc button')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'create_tuc')
    context.driver.execute_script("arguments[0].click();", button)


@then('fill the fields for ChildOne tuc')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'name').send_keys("ChildOne")

    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, 'otp_acc_type'))
    select.select_by_visible_text("On Delivery")

    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, 'trans_acc_type'))
    select.select_by_visible_text("On Delivery")

    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, 'promo_acc_type'))
    select.select_by_visible_text("On Delivery")

    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, 'gov_acc_type'))
    select.select_by_visible_text("On Delivery")

    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, 'sim_acc_type'))
    select.select_by_visible_text("On Delivery")

    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, 'default_acc_type'))
    select.select_by_visible_text("On Delivery")

    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, 'billing_type'))
    select.select_by_visible_text("POSTPAID")

    time.sleep(0.5)
    context.driver.find_element(By.ID, 'validity').send_keys(30)

    # give licences

    # child tuc
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'childtuc').send_keys(1)

    # smpps
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'smpps').clear()
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'smpps').send_keys(1)

    # sms api
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'smsapi').clear()
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'smsapi').send_keys(1)


@then('click on create tuc button')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'save_tuc')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to User')
def step_impl(context):
    # go to tuc tab
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'user_view')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on add user button')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, 'create_user')
    context.driver.execute_script("arguments[0].click();", button)


@then('fill the fields for ChildOne user')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'username').send_keys("ChildOne")

    time.sleep(0.5)
    context.driver.find_element(By.ID, 'password').send_keys("password")

    time.sleep(0.5)
    context.driver.find_element(By.ID, 'fname').send_keys("first")

    time.sleep(0.5)
    context.driver.find_element(By.ID, 'lname').send_keys("last")

    time.sleep(0.5)
    context.driver.find_element(By.ID, 'email').send_keys("email@gmail.com")

    time.sleep(0.5)
    context.driver.find_element(By.ID, 'mob_no').send_keys(9950500435)

    time.sleep(0.5)
    context.driver.find_element(By.ID, 'comp_name').send_keys("onextel")

    time.sleep(0.5)
    context.driver.find_element(By.ID, 'web').send_keys("web@web.com")

    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, 'role_type'))
    select.select_by_visible_text("TUC Admin")

    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, 'tuc'))
    select.select_by_visible_text("ChildOne(2022)")


@then('click on create user button')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'save_user')
    context.driver.execute_script("arguments[0].click();", button)


@then('log out from parent tuc')
def step_impl(context):
    # log out form parent tuc and login child TUC
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'dropdown-caret')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    button = context.driver.find_element(By.ID, 'log-out')
    context.driver.execute_script("arguments[0].click();", button)


@then('reset password and click on submit')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'new_password').send_keys("Onextel@123")

    time.sleep(0.5)
    context.driver.find_element(By.ID, 'confirm_password').send_keys("Onextel@123")
