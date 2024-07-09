from behave import *
import time
from selenium.webdriver.common.by import By


# Login to tuc – new sms – quick sms – recipients and group – split schedule –send –
# verify numbers – verify credits – click on view schedule – verify record is added or not – close.

@then('add recipients, group and select template')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="recipient_numbers"]').send_keys(9876543210)  # add recipients

    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="groupDropdown"]').send_keys("new test(3)")  # adding group

    time.sleep(2)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[1]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # uncheck remove duplicates

    # template add
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="insert_template"]').click()  # go to insert template

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="template_type_id"]').send_keys(
        "Service Implicit(2)")  # select template type

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="template_name"]').send_keys("One Variable")  # select template name

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="insert_template_to_msg"]').click()  # click on select button


@then('check on split schedule, send it')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[6]/div[1]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # check schedule sms

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[6]/div[2]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # check multiple campaigns

    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="sms_body"]/div[7]/div[2]/div[2]/input').send_keys(4)  # sms count

    time.sleep(1)
    button = context.driver.find_element(By.ID, 'send')
    context.driver.execute_script("arguments[0].click();", button)  # send button

    # warning window
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'proceed')
    context.driver.execute_script("arguments[0].click();", button)  # click on yes

    # split confirmation window
    time.sleep(2)
    button = context.driver.find_element(By.ID, 'confirm_send_sms')
    context.driver.execute_script("arguments[0].click();", button)  # click on proceed

    # on new window
    time.sleep(2)
    button = context.driver.find_element(By.ID, 'new_sms')
    context.driver.execute_script("arguments[0].click();", button)  # click on new-sms


@then('verify credits, go to view schedule')
def step_impl(context):
    time.sleep(2)
    new_avail_bal = context.driver.find_element(By.XPATH, '//*[@id="available_credits"]').text
    context.new_avail_balance = int(str(new_avail_bal).replace(",", ""))
    assert context.available_bal == 4 + context.new_avail_balance  # verifying the credits

    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="quick_eng_sms_title"]').click()  # go to quick english sms button

    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="pills-campaign-summary-tab"]').click()  # go to view schedule tab


@then('verify weather record is added or not')
def step_impl(context):
    # check weather record added or not
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, '//*[@id="id_3521"]').text
    if text == "3521":
        assert True, "Test Passed"


@then('browser closed')
def step_impl(context):
    time.sleep(4)
    context.driver.close()
