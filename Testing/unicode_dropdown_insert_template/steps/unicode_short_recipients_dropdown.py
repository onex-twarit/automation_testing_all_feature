from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then('click on click on new sms, click on unicode sms')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'new_sms').click()  # go to NEW SMS

    time.sleep(2)
    button = context.driver.find_element(By.ID, 'uicode_sms_title')
    context.driver.execute_script("arguments[0].click();", button)  # go to unicode SMS


@then('insert hindi short template, select filter as dropdown')
def step_impl(context):
    time.sleep(1)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(1)
    context.driver.find_element(By.ID, 'insert_template').click()  # go to insert template

    time.sleep(1)
    context.driver.implicitly_wait(30)
    action = (ActionChains(context.driver))
    type = context.driver.find_element(By.ID, 'template_type_id')  # select template type

    action.move_to_element(type).click().perform()

    time.sleep(0.5)
    action.key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).click().perform()

    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, "template_filter_id"))
    select.select_by_visible_text('Dropdown')

    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, 'modal_template_id'))
    select.select_by_visible_text('Hindi Short')

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'insert_template_to_msg')
    context.driver.execute_script("arguments[0].click();", button)  # click on select button


@then('check allow multi part sms box')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[5]/div[1]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # check allow multi part


@then('check allow unicode box')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[5]/div[2]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # check allow multi part

