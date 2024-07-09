from behave import *
import time
from selenium.webdriver.common.by import By


@then('click on download XLSX')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "download_xls")
    context.driver.execute_script("arguments[0].click();", button)
