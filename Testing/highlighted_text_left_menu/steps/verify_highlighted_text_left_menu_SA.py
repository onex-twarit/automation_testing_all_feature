from behave import *
import time
from selenium.webdriver.common.by import By


@then('click on Tenants tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'tenant_view')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="tenant_view"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on super admin user tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'super_admin_user_tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="super_admin_user_tab"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on platform user tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'platform_user_tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="platform_user_tab"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Report verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_master_report')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="menu_master_report"]/p').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Report Search tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/ul/li[3]/a')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/ul/li[3]/a').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Report Download data tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/ul/li[4]/a')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH,
                                             '/html/body/div[1]/div[2]/div[3]/div[2]/ul/li[4]/a').value_of_css_property(
        'color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Master Credits verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_master_balance')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="menu_master_balance"]/p').value_of_css_property(
        'color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on master credits tab verify the highlighted text color')
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


@then('click on super admin history tab verify the highlighted text color')
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


@then('click on Master Licenses verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_master_license')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="menu_master_license"]/p').value_of_css_property(
        'color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Spam verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_spam')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="menu_spam"]/p').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on spam category tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'spam_cat')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="spam_cat"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on keywords tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'spam_keywords')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="spam_keywords"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on spam unassign tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'spam_unassign')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="spam_unassign"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Mapping Report verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_mapping_report')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="menu_mapping_report"]/p').value_of_css_property(
        'color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on userwise discounting tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'userwise_discounting')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="userwise_discounting"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on detailed discounting tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'detailed_discounting')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="detailed_discounting"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Settings verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_setting')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="menu_setting"]/p').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on error code mapping tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'error-map-tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="error-map-tab"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on discount mapping tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'discount-map-tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="discount-map-tab"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on retry mapping tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'retry-map-tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="retry-map-tab"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on backup gateway tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'backup_gw_setting_tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="backup_gw_setting_tab"]').value_of_css_property(
        'color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Routing verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_routing')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="menu_routing"]/p').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on create rule tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'create_rule_tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="create_rule_tab"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on view rule verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'view_rule_tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="view_rule_tab"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Options verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_option')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="menu_option"]/p').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on carrier tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'option_carrier')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="option_carrier"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on vendor tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'option_vendor')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="option_vendor"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on circle tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'option_circle')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="option_circle"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on type tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'option_type')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="option_type"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on API Key verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_api_key')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="menu_api_key"]/p').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"
