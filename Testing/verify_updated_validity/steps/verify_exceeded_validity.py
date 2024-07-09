from behave import *
import time
from selenium.webdriver.common.by import By


@then('in tuc, click User Management, go to TUC')
def tuc_click_edit(context):
    # click on user management
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/a[3]/p').click()

    # go to tuc tab
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'tuc_view')
    context.driver.execute_script("arguments[0].click();", button)


@then('in child, click on edit(action)')
def tuc_click_edit(context):
    # click on edit in tuc tab
    time.sleep(2)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/table[2]/tbody/tr[2]/td[7]/a[1]/img')
    context.driver.execute_script("arguments[0].click();", button)


@then('enter the validity greater than present')
def give_validity(context):
    time.sleep(0.5)
    # clear the validity field
    context.driver.find_element(By.ID, 'validity').clear()
    # pass the validity
    context.driver.find_element(By.ID, 'validity').send_keys(50)


@then('verify the error label \'validity exceeds\'')
def verify_error_label(context):
    # verify error labels when validity exceeds
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="validity_error_label"]/div/span/p').text
    if text == "Validity exceeds":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('click on cancel')
def click_cancel(context):
    # click on cancel after the eroor label check
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, '//*[@id="cancel"]')
    context.driver.execute_script("arguments[0].click();", button)  # click edit(action)
