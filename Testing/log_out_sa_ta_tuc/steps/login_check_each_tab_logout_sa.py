from behave import *
import time
from selenium.webdriver.common.by import By


@then('open dashboard')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.ID, 'dashboard_title').text
    if text == "Dashboard":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then('log out')
def step_impl(context):
    # dropdown to get log out option
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'dropdown-caret')
    context.driver.execute_script("arguments[0].click();", button)

    # click on log out button
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'log-out')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to User Management')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_users')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to tenants tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'tenant_view')
    context.driver.execute_script("arguments[0].click();", button)


@then('click show tenants')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_tenant')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to User tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'user_view')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on search user')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'user_search')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Search tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on search on search tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'search_type')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Report')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_master_report')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Telco summary tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'telco-tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on search')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to MIS tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'pills-mis-data-tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Download data tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="pills-mis-data-tab"]')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Credits')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_credit_allocation')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Userwise allocation tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'pills-user-alloc')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on search userwise')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'usr-alloc-search')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to All allocation tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="pills-all-alloc"]')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on search all allocation')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'search_alloc')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to SMPP')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_smpps_view')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to SMPP tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'smpps_view')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on search SMPP')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'search_rule_type')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Bind History tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'bind_history')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Routing Reports')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_routing_report')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to TUC details tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'gateway_search')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Gateway details tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'tuc_search')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Master Credits')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_master_balance')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Master Credits tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'pills-user-alloc')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on show credits master')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_balance')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Super Admin History tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'pills-all-alloc')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on search super admin history')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'search_alloc')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Master Licenses')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_master_license')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Config')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_config')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Blacklist category tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'blacklist_cat_tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on show blacklist')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_blacklist')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Blacklist number tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'blacklist_num_tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on search blacklist number')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'add')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Whitelist category tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'whitelist_cat_tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on show whitelist')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_whitelist')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Whitelist number tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'whitelist_num_tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on search whitelist number')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'add')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to blacklist sender ID tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'blacklist_senderid')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on show blacklist number')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_sender_blacklist')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Spam')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_spam')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Spam category tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'spam_cat')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on show category spam')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_spam_cat')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to keywords tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'spam_keywords')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on search keywords')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to spam unassign tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'spam_unassign')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on show categories')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_unassign')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Notifications')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_notification')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on show notifications')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_notification')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Mapping Report')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_mapping_report')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to userwise discounting tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'userwise_discounting')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on search user discounting')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to detailed discounting tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'detailed_discounting')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on search detailed discounting')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to settings')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_setting')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Error code mapping tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'error-map-tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on Show ECM gateways')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_gateway')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on Show ECM TUCs')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_tuc')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Discount mapping tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'discount-map-tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on Show TUCs')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show-users')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Retry mapping tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'retry-map-tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on Show retry gateways')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_retry_gateway_btn')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on Show retry TUCs')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_retry_user_btn')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Backup gateway tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'backup_gw_setting_tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Analytics')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_analytics')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Error code summary tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'error_code_summary_tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on search EC summary')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'fetch_error_code_search_button')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to DLT rejected counts tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'dlt_rejected_count')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on search DLT rejected')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'fetch_dlt_rejected_search_button')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Latency Hour-Wise Report tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'latency_hour_report')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on search latency report')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to comparison graph tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'comparison_graph')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to content monitor tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'content_monitor_tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Routing')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_routing')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to create rule tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'create_rule_tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to view rule tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'view_rule_tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on search view rule')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'search_rule_type')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Options')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_option')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to carrier tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'option_carrier')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on show carrier')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_carrier')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to vendor tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'option_vendor')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on show vendor')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_vendor')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to circle tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'option_circle')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on show circle')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_circle')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to type tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'option_type')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on show type')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_type')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to API Key')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_api_key')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on search api key')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'search_api_type')
    context.driver.execute_script("arguments[0].click();", button)
