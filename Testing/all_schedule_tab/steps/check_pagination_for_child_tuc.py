from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then('click on search (with records)')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)


@then('check pagination for child tuc')
def step_impl(context):
    # change limit to 5
    time.sleep(0.5)
    set_limit = Select(context.driver.find_element(By.ID, 'limit'))
    set_limit.select_by_visible_text("5")

    time.sleep(1)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="tuc_name_header"]').text

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'next_page')
    context.driver.execute_script('arguments[0].click();', button)

    time.sleep(1)
    text2 = context.driver.find_element(By.XPATH, '//*[@id="tuc_name_header"]').text
    if text == text2:
        assert False, 'Pagination is not working Fine'
    else:
        assert True, 'Pagination is working fine'
