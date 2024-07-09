from selenium.webdriver import Keys
from behave import *
import time
from selenium.webdriver.common.by import By


@then('go to reports, then summary tab, search for any tuc, select and search')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/a[5]/p').click()  # go to reports

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="pills-summary-tab"]').click()  # go to summary tab

    time.sleep(0.5)
    select_tuc = context.driver.find_element(By.XPATH, '//*[@id="tuc-report"]')  # search for a tuc

    time.sleep(0.5)
    select_tuc.send_keys("t")
    time.sleep(0.5)
    select_tuc.send_keys(Keys.ARROW_DOWN)  # find from the suggestions
    time.sleep(0.5)
    select_tuc.send_keys(Keys.RETURN)

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '//*[@id="search"]')

    context.driver.execute_script("arguments[0].click();", button)  # click on search

    time.sleep(2)
    text = context.driver.find_element(By.XPATH,
                                       '//*[@id="get_channel_summary_date_label"]').text
    if text == "Date":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('go to campaign summary tab, search for any tuc, select and search')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="pills-campaign-summary-tab"]').click()  # go to campaign summary tab

    time.sleep(0.5)
    select_tuc = context.driver.find_element(By.XPATH, '//*[@id="tuc-report"]')  # search for a tuc

    time.sleep(0.5)
    select_tuc.send_keys("t")
    time.sleep(0.5)
    select_tuc.send_keys(Keys.ARROW_DOWN)  # find from the suggestions
    time.sleep(0.5)
    select_tuc.send_keys(Keys.RETURN)

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '//*[@id="search"]')

    context.driver.execute_script("arguments[0].click();", button)  # click on search

    time.sleep(2)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[4]/table/tbody/tr[1]/th[1]').text
    if text == "TUC ID":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('go to search tab, search for tuc and mobile number, select and search')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="pills-search-tab"]').click()  # go to search tab

    time.sleep(0.5)
    select_tuc = context.driver.find_element(By.XPATH, '//*[@id="tuc-report"]')  # search for a tuc

    time.sleep(0.5)
    select_tuc.send_keys("t")
    time.sleep(0.5)
    select_tuc.send_keys(Keys.ARROW_DOWN)  # find from the suggestions
    time.sleep(0.5)
    select_tuc.send_keys(Keys.RETURN)

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="number"]').send_keys(9950500435)  # enter mobile number
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="sender_id"]').send_keys(1234)  # enter Sender ID

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '//*[@id="search"]')
    time.sleep(0.5)
    context.driver.execute_script("arguments[0].click();", button)  # click on search

    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[3]/table/tbody/tr[1]/th[1]').text
    if text == "TUC ID":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('go to sender ID summary tab, search for any tuc, select and search')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="pills-daily-summary-tab"]').click()  # go to sender ID summary tab

    time.sleep(0.5)
    select_tuc = context.driver.find_element(By.XPATH, '//*[@id="tuc-report"]')  # search for a tuc

    time.sleep(0.5)
    select_tuc.send_keys("t")
    time.sleep(0.5)
    select_tuc.send_keys(Keys.ARROW_DOWN)  # find from the suggestions
    time.sleep(0.5)
    select_tuc.send_keys(Keys.RETURN)

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '//*[@id="search"]')

    time.sleep(0.5)
    context.driver.execute_script("arguments[0].click();", button)  # click on search

    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[4]/table/tbody/tr[1]/th[1]').text
    if text == "TUC ID":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('go to latency report tab, search for any tuc, select and search')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="pills-latency-report-tab"]').click()  # go to latency report tab

    time.sleep(0.5)
    select_tuc = context.driver.find_element(By.XPATH, '//*[@id="tuc-report"]')  # search for a tuc

    time.sleep(0.5)
    select_tuc.send_keys("t")
    time.sleep(0.5)
    select_tuc.send_keys(Keys.ARROW_DOWN)  # find from the suggestions
    time.sleep(0.5)
    select_tuc.send_keys(Keys.RETURN)

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '//*[@id="search"]')
    time.sleep(0.5)
    context.driver.execute_script("arguments[0].click();", button)  # click on search


@then('go to clicker data tab, search for tuc and mobile, select and search')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="pills-clicker-data-tab"]').click()  # go to clicker data tab

    time.sleep(0.5)
    select_tuc = context.driver.find_element(By.XPATH, '//*[@id="tuc-report"]')  # search for a tuc

    time.sleep(0.5)
    select_tuc.send_keys("t")
    time.sleep(0.5)
    select_tuc.send_keys(Keys.ARROW_DOWN)  # find from the suggestions
    time.sleep(0.5)
    select_tuc.send_keys(Keys.RETURN)

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '//*[@id="clicker_data_search_btn"]')

    time.sleep(0.5)
    context.driver.execute_script("arguments[0].click();", button)  # click on search

    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[4]/b').text
    if text == "No Clicker Data Available":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('go to clicker details tab, search for tuc, select and search')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="pills-clicker-data-tab"]').click()  # go to clicker details tab

    time.sleep(0.5)
    select_tuc = context.driver.find_element(By.XPATH, '//*[@id="tuc-report"]')  # search for a tuc

    time.sleep(0.5)
    select_tuc.send_keys("t")
    time.sleep(0.5)
    select_tuc.send_keys(Keys.ARROW_DOWN)  # find from the suggestions
    time.sleep(0.5)
    select_tuc.send_keys(Keys.RETURN)

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '//*[@id="clicker_data_search_btn"]')

    time.sleep(0.5)
    context.driver.execute_script("arguments[0].click();", button)  # click on search

    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[4]/b').text
    if text == "No Clicker Data Available":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('go to scheduled campaigns tab, search for tuc, select and search')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="pills-campaign-tab"]').click()  # go to scheduled campaigns tab

    time.sleep(0.5)
    select_tuc = context.driver.find_element(By.XPATH, '//*[@id="tuc-report"]')  # search for a tuc

    time.sleep(0.5)
    select_tuc.send_keys("t")
    time.sleep(0.5)
    select_tuc.send_keys(Keys.ARROW_DOWN)  # find from the suggestions
    time.sleep(0.5)
    select_tuc.send_keys(Keys.RETURN)

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '//*[@id="search"]')

    time.sleep(0.5)
    context.driver.execute_script("arguments[0].click();", button)  # click on search

    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[2]/table/tbody/tr[1]/th[1]').text
    if text == "TUC ID":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"
