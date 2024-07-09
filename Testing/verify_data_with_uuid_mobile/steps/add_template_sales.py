from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then('click DLT')
def click_DLT(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_manage')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to entity ID tab, click on add entity ID')
def add_entity_id(context):
    # click on entity ID tab
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'entityid_tab')
    context.driver.execute_script("arguments[0].click();", button)

    # click on add entity di button
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'create_entityid')
    context.driver.execute_script("arguments[0].click();", button)

    # enter entity id on new pop-up
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'entity_id').send_keys(123)

    # enter entity name on new pop-up
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'entity_name').send_keys("one")

    # add entity id button
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'add_entityid')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to sender ID tab, click on add sender ID(uncheck default)')
def add_sender_id(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'senderid_tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'create_senderid')
    context.driver.execute_script("arguments[0].click();", button)

    # enter sender ID
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'sender_name').send_keys(123456)

    # select name from dropdown
    select_name = context.driver.find_element(By.ID, 'sender_entity_id')
    select = Select(select_name)
    select.select_by_visible_text("one(123)")

    # uncheck box of set as default
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div[2]/div[4]/div/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)

    # click on add button to add S ID
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'add_sender_id')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to template tab, click on add template')
def add_template(context):
    # click on template tab
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'template_tab')
    context.driver.execute_script("arguments[0].click();", button)

    # click on add template
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'create_template')
    context.driver.execute_script("arguments[0].click();", button)


@then('english, fill all the fields, then click on add')
def add_template_data(context):
    # enter template name
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'template_name').send_keys("English Short")

    # enter template ID
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'template_id').send_keys(123456)

    # select template type
    time.sleep(0.5)
    text = context.driver.find_element(By.ID, "template_type_id")
    select = Select(text)
    select.select_by_visible_text("Service Implicit")

    # select template entity id
    time.sleep(0.5)
    text = context.driver.find_element(By.ID, "template_entity_id")
    select = Select(text)
    select.select_by_visible_text("one(123)")

    # select template sender id
    time.sleep(0.5)
    text = context.driver.find_element(By.ID, "template_sender_id")
    select = Select(text)
    select.select_by_visible_text("123456")

    # give the content to template
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="template_content"]').send_keys("select from dropdown English short")

    # click on add button to add template
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'add_template')
    context.driver.execute_script("arguments[0].click();", button)
