from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then('go to User Management')
def left_menu_user_management(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_users')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to TUC tab')
def go_to_tuc_tab(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'tuc_view')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on search TUC')
def click_on_search_tuc(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'user_search')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on ICICIAdmin TUC edit')
def click_on_edit_tuc(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         "//td[contains(text(),'ICICIAdmin')]/following-sibling::td//a[@title='Edit']")
    context.driver.execute_script("arguments[0].click();", button)


@then('change all the gateways type to Vodafone')
def change_gateways(context):
    # OTP Gateway
    time.sleep(0.5)
    temp = context.driver.find_element(By.ID, 'otp_gw')
    select = Select(temp)
    select.select_by_visible_text("Vodafone(207)")

    # promo Gateway
    time.sleep(0.5)
    temp = context.driver.find_element(By.ID, 'promo_gw')
    select = Select(temp)
    select.select_by_visible_text("Vodafone(207)")

    # service implicit Gateway
    time.sleep(0.5)
    temp = context.driver.find_element(By.ID, 'serv_imp_gw')
    select = Select(temp)
    select.select_by_visible_text("Vodafone(207)")

    # service explicit Gateway
    time.sleep(0.5)
    temp = context.driver.find_element(By.ID, 'serv_exp_gw')
    select = Select(temp)
    select.select_by_visible_text("Vodafone(207)")

    # trans-promo Gateway
    time.sleep(0.5)
    temp = context.driver.find_element(By.ID, 'transpromo_gw')
    select = Select(temp)
    select.select_by_visible_text("Vodafone(207)")

    # govt. Gateway
    time.sleep(0.5)
    temp = context.driver.find_element(By.ID, 'govt_gw')
    select = Select(temp)
    select.select_by_visible_text("Vodafone(207)")

    # Simroute Gateway
    time.sleep(0.5)
    temp = context.driver.find_element(By.ID, 'simroute_gw')
    select = Select(temp)
    select.select_by_visible_text("Vodafone(207)")


@then('click on update')
def click_on_update(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'update_tuc')
    context.driver.execute_script("arguments[0].click();", button)
