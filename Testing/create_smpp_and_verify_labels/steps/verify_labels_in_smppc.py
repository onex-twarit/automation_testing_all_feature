from behave import *
import time
from selenium.webdriver.common.by import By


@then('go to HUB')
def go_to_hub(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, "menu_hub")
    context.driver.execute_script("arguments[0].click();", button)


@then('go to SMPPC tab')
def go_to_smppc_tab(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, "smppc_view")
    context.driver.execute_script("arguments[0].click();", button)


@then('click on search SMPPC')
def click_search_smppc(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, "search_host")
    context.driver.execute_script("arguments[0].click();", button)


@then('verify the headers and labels')
def verify_headers_labels(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[3]/table/tbody/tr[1]/th[1]').text
    if text == 'Name/Carrier/Vendor/AccountType/Circle':
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"

    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[3]/table/tbody/tr[1]/th[2]').text
    if text == 'Gateway Id':
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"

    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[3]/table/tbody/tr[1]/th[3]').text
    if text == 'Bind Type':
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"

    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[3]/table/tbody/tr[1]/th[4]').text
    if text == 'TPS':
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"

    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[3]/table/tbody/tr[1]/th[5]').text
    if text == 'Binds':
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"

    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[3]/table/tbody/tr[1]/th[6]').text
    if text == 'Action':
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"

