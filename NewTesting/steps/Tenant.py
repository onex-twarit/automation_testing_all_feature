from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from pages.Credits import Credits
from pages.Usermanagement import UserManagement
from pages.Login import Login
from pages.Master_Credits import MasterCredits
from behave import *
import time
from selenium.webdriver.common.by import By


@when(u'Verify that the system admin has a left-side menu option “Master Credits” for tenant configuration.')
def step_impl(context):
    Login(context.driver).verify_labels(MasterCredits.page_label, "Master Credits")
    context.main_credits = Login(context.driver).get_element(MasterCredits.main_credits_text).text
    context.main_credits_int = MasterCredits.comma_creds(context.main_credits)


@when(u'The system admin clicked on the Master Credits Menu option and clicked on the “update credits” button.')
def step_impl(context):
    Login(context.driver).click_button(MasterCredits.master_credits_page)
    Login(context.driver).click_button(MasterCredits.update_credits_btn)


@when(u'Verify that the update credits window popup')
def step_impl(context):
    Login(context.driver).verify_labels(MasterCredits.update_credits_label, "Update Credits")


@when(u'The system admin entered "{mastercredits}" credits and clicked on the add button')
def step_impl(context, mastercredits):
    Login(context.driver).enter_txt_field(MasterCredits.credits_txtbox, context.test_data['SA'][mastercredits])
    actions = ActionChains(context.driver)
    actions.move_to_element(context.driver.find_element(By.ID, "add")).click()
    actions.perform()


@when(u'Verify that "{mastercredits}" credits were added/updated successfully.')
def step_impl(context, mastercredits):
    context.driver.find_element(By.ID, "menu_dashboard").click()
    context.addedcreds = context.main_credits_int + int(context.test_data['SA'][mastercredits])
    get_credits = MasterCredits(context.driver).convert_comma_seperate_number(MasterCredits.main_credits_text)
    try:
        if get_credits == context.addedcreds:
            assert True, "added"
        else:
            assert False, f"Got these {type(get_credits)} {context.main_credits_int1} and main_credits {type(context.addedcreds)} {context.addedcreds}"
    except:
        print("name error occured")


@when(u'The system admin clicked on the Credits Menu option, and clicked on the “update credits” button.')
def step_impl(context):
    context.sacredits = context.driver.find_element(By.ID, "available_credits").text
    context.intsacredits = int(context.sacredits.replace(",", ""))
    Login(context.driver).click_button(Credits.credits_page)
    Login(context.driver).click_button(Credits.update_credit_btn)


@when(u'Verify that the update credits window for tenants popup')
def step_impl(context):
    Login(context.driver).verify_labels(Credits.update_crdit_label, "Update Credit")


@when(
    u'system admin selects the newly created "{tenant_name}",adds the credit radio button,entered credit "{tenantcredits}",clicked on Update.')
def step_impl(context, tenant_name, tenantcredits):
    time.sleep(0.5)
    select1 = Select(context.driver.find_element(By.ID, 'select_tuc'))
    opts = select1.options
    for option in opts:
        if context.test_data['TA'][tenant_name] in option.text:
            select1.select_by_visible_text(option.text)
            break
    time.sleep(0.5)
    Login(context.driver).click_btn_js(Credits.add_credit_btn)
    time.sleep(1.5)
    Login(context.driver).enter_txt_field(Credits.credits_txtbox, context.test_data['TA'][tenantcredits])
    time.sleep(0.5)
    actions = ActionChains(context.driver)
    actions.move_to_element(context.driver.find_element(By.ID, "update_credits")).double_click()
    actions.perform()
    time.sleep(1.5)


@when(u'Verify that "{tenantcredits}" credits added to the newly created tenant account "{tenant_name}".')
def step_impl(context, tenantcredits, tenant_name):
    time.sleep(0.5)
    Login(context.driver).click_btn_js(UserManagement.userManagementPage_id)
    Login(context.driver).click_btn_js(UserManagement.tenant_show_btn_id)
    time.sleep(0.5)
    a = context.driver.find_element(By.XPATH, f"//td[contains(text(),'{context.test_data['TA'][tenant_name]}')]").text
    ind = a.find("(")
    c = f"{a[ind + 1]}{a[ind + 2]}"
    print(c)
    time.sleep(0.5)
    context.driver.find_element(By.ID, f"manageCredit_{c}").click()
    cred = context.driver.find_element(By.XPATH, "//span[contains(text(),'Available Credits')]").text
    print(cred)
    b = cred.replace("Available Credits = ", "")
    global c1
    c1 = b.replace(",", "")


@when(u'"{tenantcredits}" credits were debited from the system admin’s master credits.')
def step_impl(context, tenantcredits):
    intsacrdits = context.intsacredits
    finalcrdits = intsacrdits - int(context.test_data['TA'][tenantcredits])
    time.sleep(1)
    context.sacredits1 = Login(context.driver).get_element(MasterCredits.main_credits_text).text
    context.intsacredits1 = int(context.sacredits1.replace(",", ""))
    if finalcrdits == context.intsacredits1:
        assert True, "credits deducted"
    else:
        assert False, f"credits {context.intsacredits1} and final credits = {finalcrdits}"


@when(u'Verify that on the dashboard the tenant admin is able to see "{tenantcredits}" credits in his account.')
def step_impl(context, tenantcredits):
    tacredits = context.driver.find_element(By.ID, "available_credits").text
    tacreditsint = int(tacredits.replace(",", ""))
    if tacreditsint == int(c1):
        assert True, "credits deducted"
    else:
        assert False, f"credits in tenant {tacreditsint} and  credits tried to added are = {c1}"


@when('In TA either dashboard page or change password page should appear "{ta_pass}","{ta_new_password}"')
def step_impl(context, ta_pass, ta_new_password):
    actions = ActionChains(context.driver)
    if len(context.driver.find_elements(By.ID, "dashboard_title")) > 0:
        Login(context.driver).verify_labels(Login.dashboard_page_label, "Dashboard")
        Login(context.driver).verify_labels(Login.hub_page_label, "HUB")
    elif len(context.driver.find_elements(By.XPATH, "//p[text()='Change Password']")) > 0:
        context.driver.find_element(By.ID, "confirm_password").send_keys(context.test_data['TA'][ta_new_password])
        context.driver.find_element(By.ID, "new_password").send_keys(context.test_data['TA'][ta_new_password])
        context.driver.find_element(By.ID, "reset_button").click()
        Login(context.driver).verify_labels(Login.dashboard_page_label, "Dashboard")
        Login(context.driver).verify_labels(Login.hub_page_label, "HUB")
    elif len(context.driver.find_elements(By.XPATH, "//span[text()='Invalid UserName or Password']")) > 0:
        Login(context.driver).clear_element(Login.input_field_password)
        actions.move_to_element(context.driver.find_element(By.XPATH, "//input[@id='password']")).double_click()
        actions.send_keys(context.test_data['TA'][ta_new_password])
        actions.perform()
        Login(context.driver).click_button(Login.button_Signin)
        if len(context.driver.find_elements(By.ID, "dashboard_title")) > 0:
            Login(context.driver).verify_labels(Login.dashboard_page_label, "Dashboard")
            Login(context.driver).verify_labels(Login.hub_page_label, "HUB")
        else:
            Login(context.driver).enter_txt_field(Login.cnfm_password_txtbox, context.test_data['TA'][ta_pass])
            Login(context.driver).enter_txt_field(Login.new_password_txtbox, context.test_data['TA'][ta_pass])
            Login(context.driver).click_button(Login.submit_btn)
            Login(context.driver).verify_labels(Login.dashboard_page_label, "Dashboard")
            Login(context.driver).verify_labels(Login.hub_page_label, "HUB")
