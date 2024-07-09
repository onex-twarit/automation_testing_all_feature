from behave import *
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@then('click on search')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, "fetch_error_code_search_button")
    context.driver.execute_script("arguments[0].click();", button)


@then('verify the data is present')
def step_impl(context):
    time.sleep(0.5)
    text = context.driver.find_element(By.ID, "get_error_code_summary_Date").text
    if text == "Date":
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"


# @then('verify the data is present')
# def step_impl(context):
#     time.sleep(0.5)
#     text = context.driver.find_element(By.ID, "get_error_code_summary_Date").text
#     if text == "Date":
#         assert True, "Test Passed"
#     else:
#         text = context.driver.find_element(By.ID, "search_label").text
#         if text == 'No report data available':
#             assert True, "Test Passed"
#         else:
#             assert False, "============>> Failed"


# valid tuc and search
@then('enter correct TUC name')
def step_impl(context):
    time.sleep(0.5)
    select_tuc = context.driver.find_element(By.XPATH,
                                             '//*[@id="pills-clicker-data"]/div[1]/div[1]/div[1]/input')  # search for a tuc

    time.sleep(0.5)
    select_tuc.send_keys("ICICI")

    time.sleep(0.5)
    select_tuc.send_keys(Keys.ARROW_DOWN)  # find from the suggestions

    time.sleep(0.5)
    select_tuc.send_keys(Keys.RETURN)


@then('enter incorrect TUC name with alpha-numeric input')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="pills-clicker-data"]/div[1]/div[1]/div[1]/input').send_keys(
        'abc123')


@then('enter incorrect TUC name with special-character input')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="pills-clicker-data"]/div[1]/div[1]/div[1]/input').send_keys(
        "@#$%^&&*()ABC123")


@then('verify the error label for incorrect tuc')
def step_impl(context):
    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH, '//*[@id="pills-clicker-data"]/span').text
    if text == 'Please enter a valid tuc':
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed"


# error code 765
@then('enter the error code \'765\'')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'clicker_data_mobile_text').send_keys("765")
    # new = context.driver.find_element(By.ID, 'clicker_data_mobile_text').text
    # print(new)


@then('verify if the data is present for code \'765\'')
def step_impl(context):
    time.sleep(0.5)
    text = context.driver.find_element(By.ID, "search_label").text
    if text == 'No report data available':
        assert True, "Test Passed"
    else:
        text = context.driver.find_element(By.XPATH, '//*[@id="latency-report-table"]/tbody/tr[3]/td[5]').text
        if text == '765':
            assert True, "Test Passed"
        else:
            assert False, "============>> Failed"


# error code 654
@then('enter the error code \'654\'')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'clicker_data_mobile_text').send_keys("654")


@then('verify if the data is present for code \'654\'')
def step_impl(context):
    time.sleep(0.5)
    text = context.driver.find_element(By.ID, "search_label").text
    if text == 'No report data available':
        assert True, "Test Passed"
    else:
        text = context.driver.find_element(By.XPATH, '//*[@id="latency-report-table"]/tbody/tr[3]/td[5]').text
        if text == '654':
            assert True, "Test Passed"
        else:
            assert False, "============>> Failed"
