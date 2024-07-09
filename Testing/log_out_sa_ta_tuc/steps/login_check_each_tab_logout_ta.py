from behave import *
import time
from selenium.webdriver.common.by import By


@then('go to TUC tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'tuc_view')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on search TUC')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'user_search')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to All TUC tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'all_tucs')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on Show All TUC')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_alltuc_clicked')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Account Manager tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'acc_mgr')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Manager Allocation tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'man_allocation_tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to TUC Allocation tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'tuc_allocation_tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to View Manager tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'view_man_tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Reports')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_report')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Summary tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'pills-summary-tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Campaign summary tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'pills-campaign-summary-tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Sender ID Summary tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'pills-daily-summary-tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Clicker Data tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'pills-clicker-data-tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on search clicker data')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'clicker_data_search_btn')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Clicker Details tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/ul/li[9]/a')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on search clicker details')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div/div[3]/a')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Scheduled Campaigns tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'pills-campaign-tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Telco Reports')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_telco_reports')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Partner Summary tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'partner-tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to TUC Summary tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'tucsummary-tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to HUB')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_hub')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Gateway tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'gateway_view')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on Show')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'apply_filter')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to SMPPC tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'smppc_view')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on search SMPPC')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'search_host')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Routing tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'routing_view')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Default Gateway tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'default_gateway')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to URL')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_url_tnt')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Test SMS')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_test_sms')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to All Schedule')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_all_schedule')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to View All Schedule tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'view_all_schedule')
    context.driver.execute_script("arguments[0].click();", button)
