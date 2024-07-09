from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then('click phonebook')
def click_phonebook(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="menu_phonebook"]/p')
    context.driver.execute_script("arguments[0].click();", button)


@then('click groups tab')
def click_groups_tab(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'groups')
    context.driver.execute_script("arguments[0].click();", button)


@then('click add group button')
def click_add_group(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'add-group')
    context.driver.execute_script("arguments[0].click();", button)


@then('add group name and description')
def add_group_and_desc(context):
    time.sleep(1)
    context.driver.find_element(By.ID, 'group-name').send_keys("scrub dnd group")

    time.sleep(1)
    context.driver.find_element(By.ID, 'group-desc').send_keys("desc")


@then('click on add button')
def add_button_for_group(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'add')
    context.driver.execute_script("arguments[0].click();", button)


@then('click contacts tab')
def click_contacts_tab(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'contacts')
    context.driver.execute_script("arguments[0].click();", button)


@then('click add contacts button')
def click_add_contacts(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'add-contacts')
    context.driver.execute_script("arguments[0].click();", button)


@then('choose upload bulk contact')
def upload_bulk_contacts(context):
    time.sleep(1)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/label[2]')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    context.driver.switch_to.frame("up_onex_file")
    fileupload = context.driver.find_element(By.ID, 'file1')
    fileupload.send_keys('/home/twarit/Desktop/dnd_nums.csv')


@then('select group for the uploaded file')
def select_group_for_file(context):
    time.sleep(1)
    select_group = context.driver.find_element(By.ID, 'select-group-bulk')
    select = Select(select_group)
    select.select_by_visible_text("scrub dnd group(508)")
