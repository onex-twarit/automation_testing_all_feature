from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then('add campaign \'quick group camp\', fill the present fields, click on Add')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="add_campaign_button"]')
    context.driver.execute_script("arguments[0].click();",
                                  button)  # click on add campaign button on campaign name field

    time.sleep(0.5)
    context.driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/input').send_keys(
        "quick group camp")  # campaign name
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'campaign_desc').send_keys("Desc")  # description
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'add_campaign').click()  # click on add button


@then('then add sender ID, add group, insert template')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="groupDropdown"]').send_keys("group one(3)")  # adding group

    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="insert_template"]').click()  # go to insert template

    time.sleep(1)
    context.driver.implicitly_wait(30)
    action = (ActionChains(context.driver))
    type = context.driver.find_element(By.ID, 'template_type_id')  # select template type

    action.move_to_element(type).click().perform()

    time.sleep(0.5)
    action.key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).click().perform()

    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, "template_filter_id"))
    select.select_by_visible_text("Search")

    time.sleep(0.5)
    context.driver.find_element(By.ID, 'modal_template_id').send_keys('English Short')

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, "//li[@class='ui-menu-item']/div[text()='English Short']").click()

    time.sleep(1)
    button = context.driver.find_element(By.ID, 'insert_template_to_msg')
    context.driver.execute_script("arguments[0].click();", button)  # click on select button


@then('verify with name \'quick group camp\'')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[3]/div/table/tbody/tr[2]/td[4]/div').text
    if text == 'quick group camp':
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('go to scheduled campaign, verify \'quick group camp\' name')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, 'pills-campaign-tab')
    context.driver.execute_script("arguments[0].click();", button)  # go to scheduled campaign tab

    time.sleep(2)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)  # click on search button

    time.sleep(2)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/table/tbody/tr[2]/td[4]/div').text
    if text == "quick group camp":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"
