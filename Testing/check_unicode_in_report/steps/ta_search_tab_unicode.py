from behave import *
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then('click on Report, go to Search tab')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="menu_report"]/p').click()  # click on report
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="pills-search-tab"]').click()  # go to search tab


@then('enter TUC ICICIAdmin')
def step_impl(context):
    time.sleep(1)
    # tuc = context.driver.find_element(By.ID, 'tuc-report').send_keys("ICICIAdmin(2005)")  # enter TUC
    tuc = context.driver.find_element(By.ID, 'tuc-report') # enter TUC
    tuc.send_keys("ICICIAdmin(2005)")
    time.sleep(0.5)
    tuc.send_keys(Keys.ARROW_DOWN)
    time.sleep(0.5)
    tuc.send_keys(Keys.RETURN)
    # select=Select(tuc)
    # select.select_by_visible_text("ICICIAdmin(2005)")
    # tuc.send_keys(Keys.RETURN)


@then('enter unicode in sender ID field for search tab')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'sender_id').send_keys("समाचार")  # sender ID


@then('verify error label \'No report data avaialable\' for search tab')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[3]/p').text
    if text == "No report data avaialable":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('clear sender ID field for search tab')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'sender_id').clear()  # clear sender ID


@then('enter unicode in UUID field for search tab')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'uuid').send_keys("समाचार")  # campaign name
