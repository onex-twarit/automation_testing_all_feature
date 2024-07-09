from behave import *
import time
from selenium.webdriver.common.by import By
from datetime import date


@then('go to Bind Reports')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, "menu_bind_reports")
    context.driver.execute_script("arguments[0].click();", button)


@then('go to SMPP Bind Report tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, "smpps_bind_report_tab")
    context.driver.execute_script("arguments[0].click();", button)


@then('verify date field')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.ID, "from_label").text
    if text == "Date":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"

    date_today = date.today()
    date_str = date_today.strftime("%Y-%m-%d")

    time.sleep(1)
    text = context.driver.find_element(By.ID, "date").get_attribute('value')

    if text == date_str:
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('verify system/user id search field')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="tab_content"]/div[1]/div/div/div[2]/input').get_attribute(
        'placeholder')
    if text == "Search System Id / User Id":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('verify bind status dropdown')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.ID, "bind_type").get_attribute('value')
    if text == "All":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('verify the limit dropdown')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.ID, "limit").get_attribute('value')
    if text == "100":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('verify search button')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.ID, "smpps_bind_report_search").text
    if text == "Search":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"
