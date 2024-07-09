from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from behave import *
import time
from selenium.webdriver.common.by import By


@then('open dashboard page, go to NEW SMS, then quick unicode SMS')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "//*[@id='dashboard_title']").text
    if text == "Dashboard":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"

    time.sleep(2)
    avail_balance = context.driver.find_element(By.XPATH, '//*[@id="available_credits"]').text
    context.available_bal = int(str(avail_balance).replace(",", ""))

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="new_sms"]').click()  # go to NEW SMS

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'uicode_sms_title')
    context.driver.execute_script("arguments[0].click();", button)  # go to quick unicode SMS


@then('on new window for unicode campaign, fill the present fields, click on Add')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/input').send_keys(
        "unicode campaign")  # campaign name
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'campaign_desc').send_keys("Desc")  # description
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'add_campaign').click()  # click on add button


@then('add number in recipients, then select unicode template, click on select')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="recipient_numbers"]').send_keys(9950500435)

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="insert_template"]').click()  # go to insert template

    time.sleep(1)
    action = (ActionChains(context.driver))
    type = context.driver.find_element(By.ID, 'template_type_id')  # select template type
    action.move_to_element(type).click().perform()

    time.sleep(1)
    action.key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).click().perform()

    time.sleep(0.5)
    context.driver.find_element(By.ID, 'modal_template_id').send_keys('Hindi Short')

    time.sleep(1)
    context.driver.find_element(By.XPATH, "//li[@class='ui-menu-item']/div[text()='Hindi Short']").click()

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'insert_template_to_msg')
    context.driver.execute_script("arguments[0].click();", button)  # click on select button


@then('check on allow multi part and allow unicode')
def step_impl(context):

    time.sleep(2)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(2)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[5]/div[1]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # check allow multipart sms

    time.sleep(2)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[5]/div[2]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # check allow unicode


@then('verify the credits on the same window for unicode sms')
def step_impl(context):
    time.sleep(2)
    total_ded = context.driver.find_element(By.XPATH,
                                            '//*[@id="available_credits"]').text
    context.total_deductions = int(str(total_ded).replace(",", ""))

    assert context.available_bal == context.total_deductions + 2
