import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from pages.Credits import Credits
from pages.Usermanagement import UserManagement
from pages.Login import Login
from pages.Master_Credits import MasterCredits
from behave import *
from selenium.webdriver.common.by import By


@given('navigate to the login page at "{SAurl}"')
def step_impl(context, SAurl):
    url = context.test_data['SA'][SAurl]
    context.driver.get(url)


@when('enter username "{username}" and password "{password}"')
def step_impl(context, username, password):
    Login(context.driver).enter_txt_field(Login.input_field_login, context.test_data['SA'][username])
    Login(context.driver).enter_txt_field(Login.input_field_password, context.test_data['SA'][password])


@when(u'enter TA username "{user}" and password "{ta_pass}"')
def step_impl(context, user, ta_pass):
    Login(context.driver).enter_txt_field(Login.input_field_login, context.test_data['TA'][user])
    Login(context.driver).enter_txt_field(Login.input_field_password, context.test_data['TA'][ta_pass])


@when('click the login button')
def step_impl(context):
    Login(context.driver).click_button(Login.button_Signin)


@when('either dashboard page or change password page should appear "{sauserpassworddefault}","{sauserpasswordnew}"')
def step_impl(context, sauserpassworddefault, sauserpasswordnew):
    actions = ActionChains(context.driver)
    if len(context.driver.find_elements(By.ID, "dashboard_title")) > 0:
        Login(context.driver).verify_labels(Login.dashboard_page_label, "Dashboard")
        Login(context.driver).verify_labels(Login.user_management_pagelabel, "User Management")
    elif len(context.driver.find_elements(By.XPATH, "//p[text()='Change Password']")) > 0:
        context.driver.find_element(By.ID, "confirm_password").send_keys(context.test_data['SA'][sauserpasswordnew])
        context.driver.find_element(By.ID, "new_password").send_keys(context.test_data['SA'][sauserpasswordnew])
        context.driver.find_element(By.ID, "reset_button").click()
        Login(context.driver).verify_labels(Login.dashboard_page_label, "Dashboard")
        Login(context.driver).verify_labels(Login.user_management_pagelabel, "User Management")
    elif len(context.driver.find_elements(By.XPATH, "//span[text()='Invalid UserName or Password']")) > 0:
        Login(context.driver).clear_element(Login.input_field_password)
        actions.move_to_element(context.driver.find_element(By.XPATH, "//input[@id='password']")).double_click()
        actions.send_keys(context.test_data['SA'][sauserpasswordnew])
        actions.perform()
        Login(context.driver).click_button(Login.button_Signin)
        if len(context.driver.find_elements(By.ID, "dashboard_title")) > 0:
            Login(context.driver).verify_labels(Login.dashboard_page_label, "Dashboard")
            Login(context.driver).verify_labels(Login.user_management_pagelabel, "User Management")
        else:
            Login(context.driver).enter_txt_field(Login.cnfm_password_txtbox,
                                                  context.test_data['SA'][sauserpassworddefault])
            Login(context.driver).enter_txt_field(Login.new_password_txtbox,
                                                  context.test_data['SA'][sauserpassworddefault])
            Login(context.driver).click_button(Login.submit_btn)
            Login(context.driver).verify_labels(Login.dashboard_page_label, "Dashboard")
            Login(context.driver).verify_labels(Login.user_management_pagelabel, "User Management")
    else:
        Login(context.driver).verify_labels(Login.dashboard_page_label, "Dashboard")
        Login(context.driver).verify_labels(Login.user_management_pagelabel, "User Management")


@when(u'Click on User Management')
def step_impl(context):
    Login(context.driver).click_button(UserManagement.userManagementPage_id)


@when(u'Click on + Add Tenant Button')
def step_impl(context):
    Login(context.driver).click_button(UserManagement.addTenantButtonId)


@when(u'Enter tenant details Name "{tenant_name}" and "{description}" and "{child_tuc}" and "{smpps}" and "{sms_api}"')
def step_impl(context, tenant_name, description, child_tuc, smpps, sms_api):
    Login(context.driver).enter_txt_field(UserManagement.tenant_name_txtbox_id, context.test_data['TA'][tenant_name])
    Login(context.driver).enter_txt_field(UserManagement.tenant_desc_textbox_id, context.test_data['TA'][description])
    Login(context.driver).enter_txt_field(UserManagement.tenant_child_tuc_txtbox_id, context.test_data['TA'][child_tuc])
    Login(context.driver).enter_txt_field(UserManagement.tenant_smpps_textbox_id, context.test_data['TA'][smpps])
    Login(context.driver).enter_txt_field(UserManagement.tenant_api_textbox_id, context.test_data['TA'][sms_api])


@when(u'Click on Create button')
def step_impl(context):
    Login(context.driver).click_btn_js(UserManagement.create_tenant_btn_id)


@when(u'Click on Show Tenants Button')
def step_impl(context):
    Login(context.driver).click_button(UserManagement.tenant_show_btn_id)


@when(u'Verify Tenant "{tenant_name}" is created successfully')
def step_impl(context, tenant_name):
    time.sleep(1)
    final_txt = context.driver.find_element(By.XPATH,
                                            f"//td[contains(text(),'{context.test_data['TA'][tenant_name]}')]").text
    if context.test_data['TA'][tenant_name] in final_txt:
        assert True, f"finat_txt{final_txt}"
    else:
        assert False, f"exception occured {context.test_data['TA'][tenant_name]} finaltxt {final_txt}"


@when(u'Click on TA User')
def step_impl(context):
    Login(context.driver).click_button(UserManagement.tenant_usertab_id)


@when(u'Click on Add User Button')
def step_impl(context):
    Login(context.driver).click_button(UserManagement.tenant_adduser_btn_id)


@when(u'Enter tenant User details Name "{user}", Password "{ta_pass}", First Name "{fname}", Last Name "{lname}", '
      u'Email "{email}", Mobile Number "{mobileno}", Company Name "{company}", Website "{website}", Role "{userrole}",TA"{tenant_name}"')
def step_impl(context, user, ta_pass, fname, lname, email, mobileno, company, website, userrole, tenant_name):
    context.login = Login(context.driver)
    context.login.enter_txt_field(UserManagement.tenant_username_txt_id, context.test_data['TA'][user])
    context.login.enter_txt_field(UserManagement.tenant_password_txt_id, context.test_data['TA'][ta_pass])
    context.login.enter_txt_field(UserManagement.tenant_fname_txt_id, context.test_data['TA'][fname])
    context.login.enter_txt_field(UserManagement.tenant_lname_txt_id, context.test_data['TA'][lname])
    context.login.enter_txt_field(UserManagement.tenant_email_txt_id, context.test_data['TA'][email])
    context.login.enter_txt_field(UserManagement.tenant_mobno_txt_id, context.test_data['TA'][mobileno])
    context.login.enter_txt_field(UserManagement.tenant_web_txt_id, context.test_data['TA'][company])
    context.login.enter_txt_field(UserManagement.tenant_compname_txt_id, context.test_data['TA'][website])
    time.sleep(1.3)
    select = Select(Login(context.driver).get_element(UserManagement.tenant_roletype_txt_id))
    select.select_by_visible_text(context.test_data['TA'][userrole])
    time.sleep(1.3)
    select1 = Select(Login(context.driver).get_element(UserManagement.tenant_tenantname_option_id))
    tenant_options = select1.options
    for option in tenant_options:
        if context.test_data['TA'][tenant_name] in option.text:
            select1.select_by_visible_text(option.text)
            break


# @when(u'Click on Create user button')
# def step_impl(context):
#     Login(context.driver).click_btn_js(UserManagement.tenant_createuser_btn_id)


@when(u'Click on Search Button in User "{user}"')
def step_impl(context, user):
    time.sleep(0.5)
    Login(context.driver).enter_txt_field(UserManagement.search_user_field, context.test_data['TA'][user])
    time.sleep(0.5)
    aa = f"//li/a[contains(text(),'{context.test_data['TA'][user]}')]"
    time.sleep(0.5)
    a = context.driver.find_element(By.XPATH, aa).text
    Login(context.driver).clear_element(UserManagement.search_user_field)
    Login(context.driver).enter_txt_field(UserManagement.search_user_field, a)
    Login(context.driver).click_btn_js(UserManagement.tenant_searchuser_btn)


@when(u'Verify Tenant user "{user}" is created successfully')
def step_impl(context, user):
    time.sleep(1)
    taname = context.driver.find_element(By.XPATH, f"//td[text()='{context.test_data['TA'][user]}']").text
    if taname == context.test_data["TA"][user]:
        assert True, f"{taname} is present"
    else:
        assert False, f"{taname} is not present"


@given(u'Verify that the URL is working and login page is displayed.')
def step_impl(context):
    Login(context.driver).element_enabled(Login.input_field_login)
    Login(context.driver).element_enabled(Login.button_Signin)


@when(u'verify Create Tenant web page form is loaded')
def step_impl(context):
    Login(context.driver).verify_labels(UserManagement.create_tenant_label, "Create Tenant")


@when(u'Verify that the Create User web page form is loaded')
def step_impl(context):
    Login(context.driver).verify_labels(UserManagement.create_user_label, "Create User")


@when(u'Click on logout')
def step_impl(context):
    Login(context.driver).click_btn_js(Login.profile)
    Login(context.driver).click_btn_js(Login.logout)


@when(u'Verify that the system admin is logged out successfully')
def step_impl(context):
    Login(context.driver).verify_labels(Login.sign_in_label, "Sign In")
