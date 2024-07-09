from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then('open dashboard')
def open_dashboard(context):
    # verify, opened page is a dashboard page
    time.sleep(1)
    text = context.driver.find_element(By.ID, 'dashboard_title').text
    if text == "Dashboard":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click User Management, go to TUC')
def ta_um_tuc_tab(context):
    # click on user management
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/a[2]/p').click()

    # go to tuc tab
    time.sleep(2)
    button = context.driver.find_element(By.ID, 'tuc_view')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on search')
def click_search(context):
    # click on search in tuc tab
    time.sleep(2)
    button = context.driver.find_element(By.ID, 'user_search')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on edit(action)')
def ta_click_edit(context):
    # click on edit button after search in tuc tab
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, '//tr[3]//td[7]//a[1]')
    context.driver.execute_script("arguments[0].click();", button)


@then('enter the validity(70) in tuc')
def give_validity(context):
    # clear the validity field
    context.driver.find_element(By.ID, 'validity').clear()

    # pass value in validity field
    context.driver.find_element(By.ID, 'validity').send_keys(70)
    context.validity = context.driver.find_element(By.ID, 'validity').get_attribute('value')


@then('click on update')
def click_update(context):
    # click on update button after editing the tuc validity
    time.sleep(2)
    button = context.driver.find_element(By.ID, 'update_tuc')
    context.driver.execute_script("arguments[0].click();", button)


@then('verify the updated validity in ta')
def verify_validity_ta(context):
    # verify the validity in TA after editing
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign"]/div[2]/table[2]/tbody/tr[3]/td[4]').text
    if text == context.validity:
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('log out from TA')
def log_out_ta(context):
    # log out form ta and loginnnn.py TUC
    time.sleep(1)
    button = context.driver.find_element(By.XPATH, '//*[@id="dropdown-caret"]')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    button = context.driver.find_element(By.ID, 'log-out')
    context.driver.execute_script("arguments[0].click();", button)


@then(u'click on user management, go to TUC tab, tuc')
def step_impl(context):
    # click on user management
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/a[3]/p').click()

    # go to tuc tab
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'tuc_view')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on add tuc button')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'create_tuc')
    context.driver.execute_script("arguments[0].click();", button)


@then('fill the fields for ChildOne tuc(50)')
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
    context.driver.find_element(By.ID, 'validity').send_keys(50)

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


@then('click on create button')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'save_tuc')
    context.driver.execute_script("arguments[0].click();", button)


@then('fill the fields for ChildTwo tuc(30)')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'name').send_keys("ChildTwo")

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

    # ----------- give licences -----------

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
