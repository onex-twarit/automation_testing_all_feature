from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


# Login to Tenant – go to report – check all in tuc status - Search by TUC name – check – close.

@then('go to report, check all in tuc status')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="menu_report"]/p').click()  # go to report tab

    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="pills-tab"]/li[1]').click()  # go to MIS tab

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[1]/div[1]/div[1]/div/input[1]')
    context.driver.execute_script("arguments[0].click();", button)  # check all in tuc status


@then('search tuc by name and check')
def step_impl(context):

    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="tuc-report"]').send_keys("newtuc(2000)")  # search tuc by name
    # find = context.driver.find_element(By.XPATH, '//*[@id="tuc-report"]').send_keys("newtuc(2000)")  # search tuc by name
    #
    # if find:
    #     time.sleep(2)
    #     text = context.driver.find_element(By.XPATH, '//*[@id="pills-campaign"]/div[2]/table/tbody/tr[2]/td[1]').text
    #     if text == "newtuc(2000)":
    #         assert True, "Test Passed"

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)  # click on search button

    time.sleep(2)
    text = context.driver.find_element(By.XPATH, '//*[@id="customers"]/tbody/tr[33]/th[26]/a').text
    if text == 134:
        assert True, "Test Passed"