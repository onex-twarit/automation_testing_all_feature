from behave import *
import time
from selenium.webdriver.common.by import By


@then('click on add user tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'add_user_tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="add_user_tab"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on user unblock tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'unblock_user_tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="unblock_user_tab"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on All TUC tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'all_tucs')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="all_tucs"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on UM Search tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="search"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Account manager tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'acc_mgr')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="acc_mgr"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on manager allocation tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'man_allocation_tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="man_allocation_tab"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on TUC allocation tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'tuc_allocation_tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="tuc_allocation_tab"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on View manager tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'view_man_tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="view_man_tab"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Telco summary tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'telco-tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="telco-tab"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Bind History tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'bind_history')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="bind_history"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on HUB verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_hub')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="menu_hub"]/p').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Gateway tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'gateway_view')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="gateway_view"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on SMPPC tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'smppc_view')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="smppc_view"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Routing tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'routing_view')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="routing_view"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Default gateway tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'default_gateway')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="default_gateway"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Routing Reports verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_routing_report')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="menu_routing_report"]/p').value_of_css_property(
        'color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on TUC details tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'gateway_search')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="gateway_search"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on gateway details tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'tuc_search')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="tuc_search"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on URL verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_url_tnt')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="menu_url_tnt"]/p').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on blacklist sender ID tab verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'blacklist_senderid')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="blacklist_senderid"]').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Test SMS verify the highlighted text color')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_test_sms')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text_color = context.driver.find_element(By.XPATH, '//*[@id="menu_test_sms"]/p').value_of_css_property('color')
    if text_color == "rgba(194, 43, 49, 1)":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"
