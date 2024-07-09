from behave import *
import time
from selenium.webdriver.common.by import By
from pages.Login import Login
from pages.Tuc import Tuc


# ************************************** Login TUC first time **************************************

@when('Enter Username for tuc "{tuc_username}" and password "{tuc_invalid_pass}"')
def step_impl(context, tuc_username, tuc_invalid_pass):
    tuc_username = context.test_data['TUC'][tuc_username]
    tuc_invalid_pass = context.test_data['TUC'][tuc_invalid_pass]

    context.driver.maximize_window()
    time.sleep(0.5)
    Login(context.driver).enter_txt_field(Login.input_field_login, tuc_username)
    Login(context.driver).enter_txt_field(Login.input_field_password, tuc_invalid_pass)


@when('Click on login button then enter valid password for tuc "{tuc_password}"')
def step_impl(context, tuc_password):
    tuc_password = context.test_data['TUC'][tuc_password]

    context.driver.implicitly_wait(20)
    Login(context.driver).click_button(Login.button_Signin)
    # login fails
    try:
        # Check if the error message element is present
        time.sleep(0.5)
        Login(context.driver).verify_labels(Login.invalid_password_xpath,
                                            "Invalid UserName or Password")
        time.sleep(0.5)
        Login(context.driver).click_button(Login.input_field_password)
        time.sleep(0.5)
        Login(context.driver).clear_element(Login.input_field_password)
        time.sleep(0.5)
        Login(context.driver).enter_txt_field(Login.input_field_password, tuc_password)
        time.sleep(0.5)
        Login(context.driver).click_button(Login.button_Signin)

    except Exception as e:
        print(f"Handling exception: {e}")


# Verify that on the dashboard the tenant admin has a left-side menu option “”

@when('Verify that on the dashboard the tenant admin has a left-side menu option “DLT”')
def step_impl(context):
    time.sleep(1)
    Login(context.driver).verify_labels(Tuc.dlt_left_menu, "DLT")


@when('Verify that on the dashboard the TUC has 5000 available credits')
def step_impl(context):
    time.sleep(0.5)
    avail_balance = context.driver.find_element(By.ID, 'available_credits').text
    context.available_bal = int(str(avail_balance).replace(",", ""))
    print("available balance ", context.available_bal)
    if context.available_bal == 5000:
        assert True, "Test Passed"
    else:
        assert False, "Failed "


@when('Close driver window')
def step_impl(context):
    time.sleep(0.5)
    context.driver.quit()
