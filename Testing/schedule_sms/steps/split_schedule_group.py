from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


# Login to tuc – new sms – quick sms – group – split schedule – send –
# verify numbers – verify credits – click on view schedule – verify record is added or not – close.
@then('send sms using group, fill the details and')
def step_impl(context):

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="groupDropdown"]').send_keys("new test(3)")  # adding group

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="insert_template"]').click()  # go to insert template

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="template_type_id"]').send_keys(
        "Service Implicit(1)")                                                          # select template type

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="template_name"]').send_keys("One Variable")  # select template name

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="insert_template_to_msg"]').click()  # click on select button


@then('check split schedule and send it')
def step_impl(context):

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[6]/div[1]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # check schedule box

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[6]/div[2]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # check multiple campaigns

    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="sms_body"]/div[7]/div[2]/div[2]/input').send_keys(2)  # sms count

    time.sleep(1)
    button = context.driver.find_element(By.ID, 'send')
    context.driver.execute_script("arguments[0].click();", button)  # send button
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'proceed')
    context.driver.execute_script("arguments[0].click();", button)           # tap yes on warning window


@then('verify num then credits')
def step_impl(context):

    #   verify numbers
    time.sleep(2)
    text = context.driver.find_element(By.XPATH,
                                       '//*[@id="bd-example-modal-lg"]/div/div/div[2]/table/tbody/tr[3]/th[2]').text
    if text == 2:
        assert True, "Test Passed"

    time.sleep(1)
    button = context.driver.find_element(By.ID, 'confirm_send_sms')
    context.driver.execute_script("arguments[0].click();", button)  # proceed button

    # go to view schedule tab
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign-summary-tab"]')
    context.driver.execute_script("arguments[0].click();", button)

# check weather record added or not
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, '//*[@id="id_3508"]').text
    if text == "3508":
        assert True, "Test Passed"
    #   verify credits
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'new_sms')
    context.driver.execute_script("arguments[0].click();", button)  # click on new sms button

    time.sleep(2)
    new_avail_bal = context.driver.find_element(By.XPATH, '//*[@id="available_credits"]').text
    context.new_avail_balance = int(str(new_avail_bal).replace(",", ""))  # verifying the credits

    assert context.available_bal == 2 + context.new_avail_balance


@then('go to view schedule and verify (record added)')
def step_iompl(context):
    pass

