from behave import *
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.Login import Login
from pages.Tuc import Tuc
from pages.Credits import Credits


# ************************************** Login TA first time **************************************
@given('open onextel Homepage "{url}"')
def OpenHomepage(context, url):
    url = context.test_data['TUC'][url]
    print(context)
    try:
        context.driver.get(url)
    except NameError:
        print(f"{url} unable to load")
    else:
        print(f"{url} loaded successfully")


@when('Enter Tenant Username "{ta_username}" and password "{ta_password}"')
def step_impl(context, ta_username, ta_password):
    ta_username = context.test_data['TUC'][ta_username]
    ta_password = context.test_data['TUC'][ta_password]
    time.sleep(0.5)
    Login(context.driver).enter_txt_field(Login.input_field_login, ta_username)
    time.sleep(0.5)
    Login(context.driver).enter_txt_field(Login.input_field_password, ta_password)


@when('Verify that on the dashboard the tenant admin has a left-side menu option “User Management”')
def step_impl(context):
    Login(context.driver).verify_labels(Login.user_management_left_menu, "User Management")


@when('Verify the dashboard page opens')
def step_impl(context):
    Login(context.driver).verify_labels(Login.dashboard_page_label, "Dashboard")


# ************************************** Create Tenant User Client **************************************
@given('go to User Management page')
def step_impl(context):
    time.sleep(1)
    Login(context.driver).click_button(Login.user_management_left_menu)


@when('go to TUC tab')
def step_impl(context):
    time.sleep(0.5)
    Login(context.driver).click_button(Tuc.tuc_tab)


@when('click on the Add TUC button')
def step_impl(context):
    time.sleep(0.5)
    Login(context.driver).click_button(Tuc.add_tuc_button)


@when('Verify the create TUC web page form is loaded')
def step_impl(context):
    Login(context.driver).verify_labels(Login.create_tuc_page_label, "Tuc Info")


@when('Enter the data for creation of TUC "{tuc_name}", "{validity}"')
def step_impl(context, tuc_name, validity):
    context.tuc_name = context.test_data['TUC'][tuc_name]
    validity = context.test_data['TUC'][validity]

    # tuc name
    context.driver.find_element(By.ID, 'name').send_keys(context.tuc_name)

    Login(context.driver).select_from_dropdown((By.ID, "otp_acc_type"), "On Delivery")

    Login(context.driver).select_from_dropdown((By.ID, "trans_acc_type"), "On Delivery")

    Login(context.driver).select_from_dropdown((By.ID, "promo_acc_type"), "On Delivery")

    Login(context.driver).select_from_dropdown((By.ID, "gov_acc_type"), "On Delivery")

    Login(context.driver).select_from_dropdown((By.ID, "sim_acc_type"), "On Delivery")

    Login(context.driver).select_from_dropdown((By.ID, "default_acc_type"), "On Delivery")

    Login(context.driver).select_from_dropdown((By.ID, "billing_type"), "PREPAID")

    context.driver.find_element(By.ID, 'validity').send_keys(validity)

    # select gateway
    checkbox_default_gateway = context.driver.find_element(By.NAME, 'onex_gateway').is_selected()
    if checkbox_default_gateway:
        Login(context.driver).click_btn_js(Tuc.onex_gateway)


@when('give licences, "{child_tuc_}", "{s_mpps}", "{sms_api_}"')
def step_impl(context, child_tuc_, s_mpps, sms_api_):
    child_tuc_ = context.test_data['TUC'][child_tuc_]
    s_mpps = context.test_data['TUC'][s_mpps]
    sms_api_ = context.test_data['TUC'][sms_api_]

    # give licenses
    Login(context.driver).clear_element(Tuc.tenant_child_tuc_txtbox_id)
    Login(context.driver).enter_txt_field(Tuc.tenant_child_tuc_txtbox_id, child_tuc_)

    Login(context.driver).clear_element(Tuc.tenant_smpps_textbox_id)
    Login(context.driver).enter_txt_field(Tuc.tenant_smpps_textbox_id, s_mpps)

    Login(context.driver).clear_element(Tuc.tenant_api_textbox_id)
    Login(context.driver).enter_txt_field(Tuc.tenant_api_textbox_id, sms_api_)


@when('click on create TUC button')
def step_impl(context):
    button = context.driver.find_element(By.ID, "save_tuc")
    context.driver.execute_script("arguments[0].click();", button)
    # Login(context.driver).click_button(Login.create_tuc_button)


@when('verify the new TUC is created (using search button, new tuc should be visible)')
def step_impl(context):
    Login(context.driver).click_button(Tuc.user_search)
    time.sleep(1)
    context.new_tuc_name = context.driver.find_element(By.XPATH,
                                                       f"//td[contains(text(),'{context.tuc_name}')]").text
    # print("new_tuc_name with id ", context.new_tuc_name)

    new_tuc = context.driver.find_element(By.XPATH,
                                          f'//td[contains(text(),"{context.new_tuc_name}")]').is_displayed()
    print("newly_tuc ", new_tuc)

    if new_tuc:
        assert True, "Test Passed"
    else:
        assert False, "Failed --->> no tuc present"


# ************************************** Create TUC user **************************************
@given('go to User tab')
def step_impl(context):
    time.sleep(0.5)
    Login(context.driver).click_button(Tuc.user_tab)


@when('click on the Add User tab')
def step_impl(context):
    time.sleep(0.5)
    Login(context.driver).click_button(Tuc.add_user_tab)


@when('click on the Add User button')
def step_impl(context):
    time.sleep(0.5)
    Login(context.driver).click_button(Tuc.tenant_adduser_btn_id)


@when('Verify the create user web page form is loaded')
def step_impl(context):
    time.sleep(0.5)
    Login(context.driver).verify_labels(Login.create_user_page_label, "User Info")


@when(
    'Enter the data for TUC user "{tuc_username}", "{password}", "{first_name}", "{last_name}", "{email}", "{mob_num}", "{comp_name}", "{web}"')
def step_impl(context, tuc_username, password, first_name, last_name, email, mob_num, comp_name, web):
    context.tuc_username = context.test_data['TUC'][tuc_username]
    password = context.test_data['TUC'][password]
    first_name = context.test_data['TUC'][first_name]
    last_name = context.test_data['TUC'][last_name]
    email = context.test_data['TUC'][email]
    mob_num = context.test_data['TUC'][mob_num]
    comp_name = context.test_data['TUC'][comp_name]
    web = context.test_data['TUC'][web]

    # tuc username
    Login(context.driver).clear_element(Tuc.tuc_username)
    Login(context.driver).enter_txt_field(Tuc.tuc_username, context.tuc_username)
    # new user password
    Login(context.driver).clear_element(Login.input_field_password)
    Login(context.driver).enter_txt_field(Login.input_field_password, password)
    # first name
    Login(context.driver).enter_txt_field(Tuc.first_name, first_name)
    # last name
    Login(context.driver).enter_txt_field(Tuc.last_name, last_name)
    # email
    Login(context.driver).enter_txt_field(Tuc.email, email)
    # mob number
    Login(context.driver).enter_txt_field(Tuc.mobile_number, mob_num)
    # company name
    Login(context.driver).enter_txt_field(Tuc.company_name, comp_name)
    # web
    Login(context.driver).enter_txt_field(Tuc.web, web)


@when('select role type as TUC admin, then select name of newly created TUC "{tuc_name}"')
def step_impl(context, tuc_name):
    tuc_name = context.test_data['TUC'][tuc_name]
    # role type
    Login(context.driver).select_from_dropdown((By.ID, "role_type"), "TUC Admin")

    time.sleep(1)
    # Login(context.driver).select_from_dropdown((By.ID, "tuc"), context.new_tuc_name)

    select_one = Select(context.driver.find_element(By.ID, 'tuc'))
    new_var = select_one.options
    print("dropdown ", new_var)
    for var in new_var:
        print("text ", var.text)
        if tuc_name in var.text:
            Login(context.driver).select_from_dropdown((By.ID, "tuc"), var.text)

    selected_option = Select(context.driver.find_element(By.ID, 'tuc')).first_selected_option.text
    print(type(selected_option))


@when('click on create user button')
def step_impl(context):
    time.sleep(0.5)
    Login(context.driver).click_button(Tuc.tenant_createuser_btn_id)


@when('verify the new user is created (using search button, new user should be visible)')
def step_impl(context):
    time.sleep(0.5)
    Login(context.driver).click_button(Tuc.user_search)

    time.sleep(0.5)
    new_tuc_user_name = context.driver.find_element(By.XPATH,
                                                    f"//td[contains(text(),'{context.tuc_username}')]").is_displayed()
    if new_tuc_user_name:
        assert True, "Test Passed"
    else:
        assert False, "Failed --->> create TUC page"


@when('log out')
def step_impl(context):
    time.sleep(0.5)
    Login(context.driver).click_button(Tuc.log_out_dropdown)

    time.sleep(0.5)
    Login(context.driver).click_button(Tuc.log_out)


@when('verify the login page is visible')
def step_impl(context):
    time.sleep(1)
    username_field = context.driver.find_element(By.ID, "email").is_displayed()
    if username_field:
        assert True, "Test Passed"
    else:
        assert False, "Failed --->> login page verification"

    time.sleep(1)
    password_field = context.driver.find_element(By.ID, "password").is_displayed()
    if password_field:
        assert True, "Test Passed"
    else:
        assert False, "Failed --->> login page verification"


# ************************************** Login TUC first time **************************************


@when('Enter Username for tuc "{tuc_username}" and password "{tuc_invalid_pass}"')
def step_impl(context, tuc_username, tuc_invalid_pass):
    tuc_username = context.test_data['TUC'][tuc_username]
    tuc_invalid_pass = context.test_data['TUC'][tuc_invalid_pass]

    context.driver.maximize_window()
    time.sleep(0.5)
    # Login(context.driver).clear_element(Login.input_field_login)
    Login(context.driver).enter_txt_field(Login.input_field_login, tuc_username)
    # Login(context.driver).clear_element(Login.input_field_password)
    Login(context.driver).enter_txt_field(Login.input_field_password, tuc_invalid_pass)


@when('Verify that on the dashboard the tenant admin has a left-side menu option DLT')
def step_impl(context):
    time.sleep(1)
    Login(context.driver).verify_labels(Tuc.dlt_left_menu, "DLT")

