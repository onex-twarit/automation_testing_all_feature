from behave import *
import time
from selenium.webdriver.common.by import By


@then('click on dashboard verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_dashboard')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="menu_dashboard"]/p').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on campaign verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_campaigns')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="menu_campaigns"]/p').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on User Management verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_users')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="menu_users"]/p').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on TUC tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'tuc_view')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="tuc_view"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on User tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'user_view')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="user_view"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Credits verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_credit_allocation')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="menu_credit_allocation"]/p').value_of_css_property(
        'color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Userwise Allocation tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'pills-user-alloc')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="pills-user-alloc"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on All Allocation tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'pills-all-alloc')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="pills-all-alloc"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Reports verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_report')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="menu_report"]/p').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on MIS tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'pills-mis-data-tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="pills-mis-data-tab"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Summary tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'pills-summary-tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="pills-summary-tab"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Campaign summary tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'pills-campaign-summary-tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign-summary-tab"]').value_of_css_property(
        'color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Search tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'pills-search-tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="pills-search-tab"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Sender ID summary tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'pills-daily-summary-tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="pills-daily-summary-tab"]').value_of_css_property(
        'color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Template Wise Report tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'pills-template-report-tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="pills-template-report-tab"]').value_of_css_property(
        'color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Clicker data tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'pills-clicker-data-tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="pills-clicker-data-tab"]').value_of_css_property(
        'color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Clicker details tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="pills-clicker-data-tab"]')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="pills-clicker-data-tab"]').value_of_css_property(
        'color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Scheduled Campaigns tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'pills-campaign-tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign-tab"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Download data tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'pills-download-data-tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="pills-download-data-tab"]').value_of_css_property(
        'color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


# -------------------------------------------------------------------------------------

@then('click on Telco Reports verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_telco_reports')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="menu_telco_reports"]/p').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Partner summary tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'partner-tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="partner-tab"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on TUC summary tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'tucsummary-tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="tucsummary-tab"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on DLT verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_manage')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="menu_manage"]/p').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Entity IDs tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'entityid_tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="entityid_tab"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Sender IDs tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'senderid_tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="senderid_tab"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Template tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'template_tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="template_tab"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Bulk Upload tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'bulktemplate_tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="bulktemplate_tab"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on URL tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'url_tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="url_tab"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on SMPP verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_smpps_view')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="menu_smpps_view"]/p').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on SMPP tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'smpps_view')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="smpps_view"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on API verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_api')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="menu_api"]/p').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on API tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_api')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="menu_api"]/p').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Phonebook verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_phonebook')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="menu_phonebook"]/p').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Groups tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'groups')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="groups"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Contacts tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'contacts')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="contacts"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Config verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_config')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="menu_config"]/p').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Blacklist category tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'blacklist_cat_tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="blacklist_cat_tab"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Blacklist number tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'blacklist_num_tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="blacklist_num_tab"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on add blacklist number tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'add_blacklist')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="add_blacklist"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on upload blacklist number tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'update_blacklist')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="update_blacklist"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on download blacklist number tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'download_blacklist')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="download_blacklist"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Whitelist category tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'whitelist_cat_tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="whitelist_cat_tab"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Whitelist number tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'whitelist_num_tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="whitelist_num_tab"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on add whitelist number tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'add_whitelist')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="add_whitelist"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on upload whitelist number tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'update_whitelist')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="update_whitelist"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on download whitelist number tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'download_whitelist')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="download_whitelist"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Notifications verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_notification')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="menu_notification"]/p').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Analytics verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_analytics')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="menu_analytics"]/p').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Error Code Hourly tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'error_code_summary_tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="error_code_summary_tab"]').value_of_css_property(
        'color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on DLT Rejected Count verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'dlt_rejected_count')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="dlt_rejected_count"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Latency Hour-Wise report tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'latency_hour_report')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="latency_hour_report"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Comparision Graph tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'comparison_graph')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="comparison_graph"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Content Monitor tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'content_monitor_tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="content_monitor_tab"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Error Code Summary tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'error_code_summary_datewise_tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH,
                                             '//*[@id="error_code_summary_datewise_tab"]').value_of_css_property(
        'color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on All Schedule verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_all_schedule')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="menu_all_schedule"]/p').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on View All schedule tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'view_all_schedule')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="view_all_schedule"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"
