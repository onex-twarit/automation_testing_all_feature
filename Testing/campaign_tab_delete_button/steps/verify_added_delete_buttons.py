from behave import *
import time
from selenium.webdriver.common.by import By


@then('open dashboard')
def open_dashboard(context):
    # open dashboard page
    time.sleep(0.5)
    text = context.driver.find_element(By.ID, 'dashboard_title').text
    if text == "Dashboard":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed to open dashboard "


@then('go to Campaign tab')
def campaign_tab(context):
    # open campaign tab
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_campaigns')
    context.driver.execute_script("arguments[0].click();", button)


@then('verify campaign tab is opened')
def verify_campaign_page(context):
    # open and verify campaign page is opened
    time.sleep(0.5)
    text = context.driver.find_element(By.ID, 'campaign_title').text
    if text == "Campaign":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed to open campaign page "


@then('verify \'delete selected\' and \'delete all\' buttons are present')
def verify_the_delete_buttons(context):
    # check delete selected and delete all buttons are present
    time.sleep(0.5)
    text = context.driver.find_element(By.ID, 'delete_selected_campaign').is_displayed()
    if text:
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed to verify delete selected button "

    time.sleep(0.5)
    text = context.driver.find_element(By.ID, 'delete_all_campaign').is_displayed()
    if text:
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed to verify delete all button "
