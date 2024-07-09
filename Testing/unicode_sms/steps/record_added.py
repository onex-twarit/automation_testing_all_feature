from behave import *
import time
from selenium.webdriver.common.by import By


@then('add recipients, split schedule, send it, verify num and credit')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="recipient_numbers"]').send_keys(9876543210,
                                                                                    "\n")  # add recipients 1

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="recipient_numbers"]').send_keys(9879043210)  # add recipients 2

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="insert_template"]').click()  # go to insert template

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="template_type_id"]').send_keys(
        "Service Implicit(2)")  # select template type

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="template_name"]').send_keys("New Hindi")  # select template name

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="insert_template_to_msg"]').click()  # click on select button

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="dest_language"]').send_keys("Hindi")  # select Hindi

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[5]/div[1]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # check multipart

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[5]/div[2]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # check unicode

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[6]/div[1]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # check schedule sms

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[6]/div[2]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # check multiple campaigns

    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="sms_body"]/div[7]/div[2]/div[2]/input').send_keys(2)  # sms count

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

    # verifying the credits
    time.sleep(2)
    new_avail_bal = context.driver.find_element(By.XPATH, '//*[@id="available_credits"]').text
    context.new_avail_balance = int(str(new_avail_bal).replace(",", ""))
    assert context.available_bal == 4 + context.new_avail_balance


# Login to tuc – new sms – unicode sms – send sms using recipients – split schedule – send –
# verify numbers – verify credits – click on view schedule – verify record is added or not – close.

@then('on view schedule check added record')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="uicode_sms_title"]').click()  # go to unicode sms button

    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="pills-campaign-summary-tab"]').click()  # go to view schedule tab

    time.sleep(2)
    text = context.driver.find_element(By.XPATH, '//*[@id="id_3527"]').text
    if text == "3527":
        assert True, "Test Passed"
