from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then('insert template hindi long with dropdown type')
def template_hindi_long_dropdown(context):
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
    select.select_by_visible_text('Hindi Long')

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'insert_template_to_msg')
    context.driver.execute_script("arguments[0].click();", button)  # click on select button

