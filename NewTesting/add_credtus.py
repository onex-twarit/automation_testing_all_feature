from behave import *
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.Login import Login
from pages.Tuc import Tuc
from pages.Credits import Credits


# ************************************** Add credits to TUC **************************************
@when('go to Credits page')
def step_impl(context):
    time.sleep(1)
    Login(context.driver).click_btn_js(Credits.credits_left_menu)

    time.sleep(0.5)
    avail_balance = context.driver.find_element(By.XPATH, '//*[@id="available_credits"]').text
    context.available_bal = int(str(avail_balance).replace(",", ""))
    print(avail_balance)


@when('go to Userwise Allocation tab')
def step_impl(context):
    time.sleep(0.5)
    Login(context.driver).click_button(Credits.userwise_allocation)


@when('click on Update Credit button')
def step_impl(context):
    time.sleep(0.5)
    Login(context.driver).click_button(Credits.update_credit_btn)


@when('on the update credit pop select the newly created TUC "{tuc_name}" from dropdown')
def step_impl(context, tuc_name):
    tuc_name = context.test_data['TUC'][tuc_name]
    time.sleep(1)
    select_two = Select(context.driver.find_element(By.ID, 'select_tuc'))
    new_var_two = select_two.options
    for var in new_var_two:
        if tuc_name in var.text:
            Login(context.driver).select_from_dropdown((By.ID, "select_tuc"), var.text)


@when('click on Add credits button and enter the credits "{credits_tuc}"')
def step_impl(context, credits_tuc):
    credits_tuc = context.test_data['TUC'][credits_tuc]

    Login(context.driver).click_button(Credits.add_credits_radio_button)

    Login(context.driver).enter_txt_field(Credits.credits_txtbox, credits_tuc)


@when('click on update button')
def step_impl(context):
    # actions = ActionChains(context.driver)
    # actions.move_to_element(context.driver.find_element(By.ID, "update_credits_btn")).double_click()
    # actions.perform()
    time.sleep(1.5)
    Login(context.driver).click_button(Credits.update_credits_btn)


@when('verify the credits are credited to the TUC and debited from TA')
def step_impl(context):
    time.sleep(0.5)
    new_avail_bal = context.driver.find_element(By.XPATH, '//*[@id="available_credits"]').text
    context.new_avail_balance = int(str(new_avail_bal).replace(",", ""))
    print("after deduction ", context.new_avail_balance)
    assert context.available_bal == 5000 + context.new_avail_balance  # verifying the credits


# ********************************* Login TUC and verify the available credits *********************************
@when('In Tuc either dashboard page or change password page should appear "{tuc_invalid_pass}","{tuc_password}"')
def step_impl(context, tuc_invalid_pass, tuc_password):
    time.sleep(1)
    actions = ActionChains(context.driver)
    if len(context.driver.find_elements(By.ID, "dashboard_title")) > 0:
        Login(context.driver).verify_labels(Login.dashboard_page_label, "Dashboard")
        Login(context.driver).verify_labels(Login.user_management_pagelabel, "User Management")
    elif len(context.driver.find_elements(By.XPATH, "//p[text()='Change Password']")) > 0:
        context.driver.find_element(By.ID, "confirm_password").send_keys(context.test_data['TUC'][tuc_password])
        context.driver.find_element(By.ID, "new_password").send_keys(context.test_data['TUC'][tuc_password])
        context.driver.find_element(By.ID, "reset_button").click()
        Login(context.driver).verify_labels(Login.dashboard_page_label, "Dashboard")
        Login(context.driver).verify_labels(Login.user_management_pagelabel, "User Management")
    elif len(context.driver.find_elements(By.XPATH, "//span[text()='Invalid UserName or Password']")) > 0:
        Login(context.driver).clear_element(Login.input_field_password)
        actions.move_to_element(context.driver.find_element(By.XPATH, "//input[@id='password']")).double_click()
        actions.send_keys(context.test_data['TUC'][tuc_password])
        actions.perform()
        Login(context.driver).click_button(Login.button_Signin)
        if len(context.driver.find_elements(By.ID, "dashboard_title")) > 0:
            Login(context.driver).verify_labels(Login.dashboard_page_label, "Dashboard")
            Login(context.driver).verify_labels(Login.user_management_pagelabel, "User Management")
        else:
            Login(context.driver).enter_txt_field(Login.cnfm_password_txtbox,
                                                  context.test_data['TUC'][tuc_invalid_pass])
            Login(context.driver).enter_txt_field(Login.new_password_txtbox,
                                                  context.test_data['TUC'][tuc_invalid_pass])
            Login(context.driver).click_button(Login.submit_btn)
            Login(context.driver).verify_labels(Login.dashboard_page_label, "Dashboard")
            Login(context.driver).verify_labels(Login.user_management_pagelabel, "User Management")
    else:
        Login(context.driver).verify_labels(Login.dashboard_page_label, "Dashboard")
        Login(context.driver).verify_labels(Login.user_management_pagelabel, "User Management")


@when('Verify that on the dashboard the TUC has 5000 available credits')
def step_impl(context):
    time.sleep(0.5)
    avail_balance = context.driver.find_element(By.ID, 'available_credits').text
    context.available_bal = int(str(avail_balance).replace(",", ""))
    print("available baddlance ", context.available_bal)
    if context.available_bal == 5000:
        assert True, "Test Passed"
    else:
        assert False, "Failed "


@when('Close driver window')
def step_impl(context):
    time.sleep(0.5)
    context.driver.quit()
