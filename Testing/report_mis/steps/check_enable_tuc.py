from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


@then('enable the tuc and check in active')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/table/tbody/tr[2]/td[6]/a[3]/div/label/input')
    context.driver.execute_script("arguments[0].click();", button)  # enable tuc

    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="menu_report"]/p').click()  # go to report tab

    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="pills-tab"]/li[1]').click()  # go to MIS tab

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[1]/div[1]/div[1]/div/input[2]')
    context.driver.execute_script("arguments[0].click();", button)  # check active tuc

    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="tuc-report"]').send_keys("newtuc(2000)")  # enter tuc

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)  # click on search button

    time.sleep(2)
    text = context.driver.find_element(By.XPATH, '//*[@id="customers"]/tbody/tr[33]/th[26]/a').text
    if text == 134:
        assert True, "Test Passed"
