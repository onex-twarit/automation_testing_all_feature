from behave import *
import time
from selenium.webdriver.common.by import By


@then('open dashboard page')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "//*[@id='dashboard_title']").text
    if text == "Dashboard":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on Report, go to MIS tab')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="menu_report"]/p').click()  # click on report
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="pills-mis-data-tab"]').click()  # go to MIS tab

    time.sleep(1)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


@then('click on total counts')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '//*[@id="customers"]/tbody/tr[33]/th[26]/a')
    context.driver.execute_script("arguments[0].click();", button)  # click on total counts


@then('click on Web')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'web_tab').click()  # click on web


@then('enter unicode in sender ID field')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'web_senderid').send_keys("समाचार")  # # sender ID


@then('click on search')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)  # click on search


@then('verify error label \'No report data avaialable\'')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.ID, 'mis_web_table_panel').text
    if text == "No report data avaialable":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('clear sender ID field')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'web_senderid').clear()  # clear sender ID


@then('enter unicode in Campaign Name field')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'web_camp').send_keys("समाचार")  # campaign name


@then('clear Campaign Name field')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'web_camp').clear()  # clear Campaign name


@then('enter unicode in Template ID field')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'templateid').send_keys("समाचार")  # template ID


@then('clear Template ID field')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'templateid').clear()  # clear Template ID


@then('enter unicode in sender ID and Campaign Name field')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'web_senderid').send_keys("समाचार")  # sender ID

    time.sleep(0.5)
    context.driver.find_element(By.ID, 'web_camp').send_keys("समाचार")  # campaign name


@then('enter unicode in Campaign Name and Template ID field')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'web_camp').send_keys("समाचार")  # campaign name

    time.sleep(0.5)
    context.driver.find_element(By.ID, 'templateid').send_keys("समाचार")  # template ID


@then('enter unicode in Template ID and Sender ID field')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'web_senderid').send_keys("समाचार")  # sender ID

    time.sleep(0.5)
    context.driver.find_element(By.ID, 'templateid').send_keys("समाचार")  # template ID


@then('enter unicode in all the fields sender ID, campaign name, template ID')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'web_senderid').send_keys("समाचार")  # sender ID

    time.sleep(0.5)
    context.driver.find_element(By.ID, 'web_camp').send_keys("समाचार")  # campaign name

    time.sleep(0.5)
    context.driver.find_element(By.ID, 'templateid').send_keys("समाचार")  # template ID
