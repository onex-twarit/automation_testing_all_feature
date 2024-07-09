from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then('go to Routing Reports')
def left_menu_routing_reports(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_routing_report')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Gateway Details tab')
def gateway_details_tab(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'tuc_search')
    context.driver.execute_script("arguments[0].click();", button)


@then('select the GW id 207 from dropdown')
def select_gateway_id(context):
    time.sleep(1)
    select_name = context.driver.find_element(By.ID, 'gateway_id')
    select = Select(select_name)
    select.select_by_visible_text('Vodafone(207)')


@then('click on Bulk Change Gateway')
def bulk_change_gateway(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'bulk_change_gateway')
    context.driver.execute_script("arguments[0].click();", button)


@then('on warning window pop-up click proceed')
def proceed_on_warning_popup(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'first_proceed')
    context.driver.execute_script("arguments[0].click();", button)


@then('select the selected and select gateways from the dropdown')
def select_the_gateways(context):
    # first selected GW - 207
    time.sleep(1)
    select_name = context.driver.find_element(By.ID, 'selected_gateway_id')
    select = Select(select_name)
    select.select_by_visible_text('Vodafone(207)')

    # second selected GW - 208
    time.sleep(1)
    select_name = context.driver.find_element(By.ID, 'gateway_id')
    select = Select(select_name)
    select.select_by_visible_text('1(208)')


@then('click on proceed')
def click_on_proceed(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'Proceed')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on final proceed then ok')
def click_on_final_proceed(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'final-proceed')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'ok')
    context.driver.execute_script("arguments[0].click();", button)


@then('all the selected GW ID should be 208')
def check_gateway_id_208(context):
    # OTP Gateway
    time.sleep(0.5)
    otp_gw = Select(context.driver.find_element(By.ID, 'otp_gw')).first_selected_option.text

    if otp_gw == '1(208)':
        assert True, "Test Passed"
    else:
        assert False, "=> Failed, OTP GW ID mismatched"

    # promo Gateway
    time.sleep(0.5)
    promo_gw = Select(context.driver.find_element(By.ID, 'promo_gw')).first_selected_option.text
    if promo_gw == '1(208)':
        assert True, "Test Passed"
    else:
        assert False, "=> Failed, promo GW ID mismatched"

    # service implicit Gateway
    time.sleep(0.5)
    promo_gw = Select(context.driver.find_element(By.ID, 'serv_imp_gw')).first_selected_option.text
    if promo_gw == '1(208)':
        assert True, "Test Passed"
    else:
        assert False, "=> Failed, service implicit GW ID mismatched"

    # service explicit Gateway
    time.sleep(0.5)
    promo_gw = Select(context.driver.find_element(By.ID, 'serv_exp_gw')).first_selected_option.text
    if promo_gw == '1(208)':
        assert True, "Test Passed"
    else:
        assert False, "=> Failed, service explicit GW ID mismatched"

    # trans-promo Gateway
    time.sleep(0.5)
    promo_gw = Select(context.driver.find_element(By.ID, 'transpromo_gw')).first_selected_option.text
    if promo_gw == '1(208)':
        assert True, "Test Passed"
    else:
        assert False, "=> Failed, trans-promo GW ID mismatched"

    # govt. Gateway
    time.sleep(0.5)
    promo_gw = Select(context.driver.find_element(By.ID, 'govt_gw')).first_selected_option.text
    if promo_gw == '1(208)':
        assert True, "Test Passed"
    else:
        assert False, "=> Failed, govt GW ID mismatched"

    # Simroute Gateway
    time.sleep(0.5)
    promo_gw = Select(context.driver.find_element(By.ID, 'simroute_gw')).first_selected_option.text
    if promo_gw == '1(208)':
        assert True, "Test Passed"
    else:
        assert False, "=> Failed, Simroute GW ID mismatched"

