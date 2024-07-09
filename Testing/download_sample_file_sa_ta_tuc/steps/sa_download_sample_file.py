from behave import *
import time
from selenium.webdriver.common.by import By


@then('go to config')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_config')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Blacklist Number tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'blacklist_num_tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Upload Blacklist Number tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'update_blacklist')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on download sample file button')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'sample_file_download')
    context.driver.execute_script("arguments[0].click();", button)


@then('verify the labels for CSV and XLSX/XLS sample')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="csv_file_div"]/label').text
    if text == "CSV Sample":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="cls_file_div"]/label').text
    if text == "XLSX/XLS Sample":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then('click on CSV sample')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/input')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on save file')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'config_download_save_file')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on XLSX/XLS sample')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/input')
    context.driver.execute_script("arguments[0].click();", button)


@then('close the sample file pop-up')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'download_sample_close_btn')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Whitelist Number tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'whitelist_num_tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Upload Whitelist Number tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'update_whitelist')
    context.driver.execute_script("arguments[0].click();", button)
