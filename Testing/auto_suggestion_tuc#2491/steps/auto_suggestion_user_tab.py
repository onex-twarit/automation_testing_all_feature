from selenium.webdriver import Keys
from behave import *
import time
from selenium.webdriver.common.by import By


@then('go to User tab, search for any user, select and search')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="user_view"]').click()  # go to user tab

    time.sleep(0.5)
    select_tuc = context.driver.find_element(By.XPATH, '//*[@id="user_input"]')  # search for a user

    time.sleep(0.5)
    select_tuc.send_keys("t")
    time.sleep(0.5)
    select_tuc.send_keys(Keys.ARROW_DOWN)  # find from the suggestions
    time.sleep(0.5)
    select_tuc.send_keys(Keys.RETURN)

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '//*[@id="user_search"]')

    context.driver.execute_script("arguments[0].click();", button)  # click on search

    time.sleep(2)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div/table/tbody/tr[1]/th[1]/a').text
    if text == "User Name":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"

