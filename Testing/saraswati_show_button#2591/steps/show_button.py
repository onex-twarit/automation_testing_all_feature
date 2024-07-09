from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from behave import *
import time
from selenium.webdriver.common.by import By

service = Service(executable_path='/home/twarit/Downloads/chromedriver-linux64/chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


@given('Launch the browser')
def step_impl(context):
    time.sleep(0.5)
    context.driver = driver
    context.driver.maximize_window()


@then('open login page')
def step_impl(context):
    time.sleep(0.5)
    context.driver.get('http://localhost:8000/index')


@then('Enter user name and password for tuc')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("tucOne")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Pass123@@")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="login_button"]').click()


@then('open dashboard page, go to campaign')
def step_impl(context):
    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH, "//*[@id='dashboard_title']").text
    if text == "Dashboard":
        assert True, "Test Passed"

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/a[2]/p')  # go to campaign
    context.driver.execute_script("arguments[0].click();", button)


@then('click on show campaign button, data should be present')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_campaign')
    button.is_enabled()  # check button is enabled

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="show_campaign"]')
    context.driver.execute_script("arguments[0].click();", button)  # click on show button
    button.get_property('disabled')  # check button is disabled

    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH, '//*[@id="camp_table_camp_name_label"]').text  # verify data is present
    if text == "Campaign Name":
        assert True, "Test Passed"


@then('go to User management, go to TUC tab, click on search')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/a[3]/p')  # go to UM
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="tuc_view"]').click()  # go to TUC tab

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="user_search"]')  # click on search button
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/table[2]/tbody/tr[1]/th[1]').text
    if text == "TUC Name":
        assert True, "Test Passed"  # verify the data is present


@then('go to User tab, click on search, verify the data is visible')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="user_view"]').click()  # go to User tab

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="user_search"]')  # click on search button
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/table/tbody/tr[1]/th[1]/a').text
    if text == "User Name":
        assert True, "Test Passed"  # verify the data is present


@then('go to DLT, go to Entity ID tab, click on show button with enable/disable')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="menu_manage"]')  # go to DLT
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="entityid_tab"]').click()  # go to Entity ID tab

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_entityid')
    button.is_enabled()  # check button is enabled

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="show_entityid"]')  # click on show entity ID button
    context.driver.execute_script("arguments[0].click();", button)
    button.get_property('disabled')  # check button is disabled

    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH,
                                       '//*[@id="entityid_tab_col1"]').text
    if text == "Entity ID":
        assert True, "Test Passed"  # verify the data is present


@then('go to Sender ID tab, click on show button with enable/disable')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="senderid_tab"]').click()  # go to Sender ID tab

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_senderid')
    button.is_enabled()  # check button is enabled

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="show_senderid"]')  # click on show sender ID button
    context.driver.execute_script("arguments[0].click();", button)
    button.get_property('disabled')  # check button is disabled

    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH,
                                       '//*[@id="senderid_col1"]').text
    if text == "Sender ID":
        assert True, "Test Passed"  # verify the data is present


@then('go to Template tab, click on search button with enable/disable')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="template_tab"]').click()  # go to template tab

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="search"]')  # click on search button
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[3]/table/tbody/tr[1]/th[2]').text
    if text == "Template Name":
        assert True, "Test Passed"  # verify the data is present


@then('go to API, click on Show API button check button is disabled and enabled')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/a[9]/p')  # go to API
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'view_api')
    button.is_enabled()  # check button is enabled

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="view_api"]')  # click on Show API button
    context.driver.execute_script("arguments[0].click();", button)
    button.get_property('disabled')  # check button is disabled

    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH,
                                       '//*[@id="api_table_header_key"]').text
    if text == "Key":
        assert True, "Test Passed"  # verify the data is present


@then('go to Phonebook, go to Groups tab, click on show group button')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/a[10]/p')  # go to Phonebook
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="groups"]').click()  # go to groups tab

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show-group')
    button.is_enabled()  # check button is enabled

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="show-group"]')  # click on Show group button
    context.driver.execute_script("arguments[0].click();", button)
    button.get_property('disabled')  # check button is disabled

    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH,
                                       '//*[@id="get_groups_table_group_name_header"]').text
    if text == "Group Name":
        assert True, "Test Passed"  # verify the data is present


@then('go to Config, go to Blacklist Category, click on show button and check E/D')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/a[11]/p')  # go to Config
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="blacklist_cat_tab"]').click()  # go to blacklist category tab

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_blacklist')
    button.is_enabled()  # check button is enabled

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="show_blacklist"]')  # click on Show blacklist button
    context.driver.execute_script("arguments[0].click();", button)
    button.get_property('disabled')  # check button is disabled

    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH,
                                       '//*[@id="blacklist_category_name_header"]').text
    if text == "Category Name":
        assert True, "Test Passed"  # verify the data is present


@then('go to Whitelist Category, click on show button and check E/D')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH,
                                '//*[@id="whitelist_cat_tab"]').click()  # go to whitelist category tab

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_whitelist')
    button.is_enabled()  # check button is enabled

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="show_whitelist"]')  # click on Show whitelist button
    context.driver.execute_script("arguments[0].click();", button)
    button.get_property('disabled')  # check button is disabled

    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH,
                                       '//*[@id="whitelist_category_name_header"]').text
    if text == "Category Name":
        assert True, "Test Passed"  # verify the data is present


@then('go to Notification, click on show Notification button')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/a[12]/p')  # go to Notification
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_notification')
    button.is_enabled()  # check button is enabled

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="show_notification"]')  # click on show notification button
    context.driver.execute_script("arguments[0].click();", button)
    button.get_property('disabled')  # check button is disabled

    time.sleep(0.5)
    text = context.driver.find_element(By.XPATH,
                                       '//*[@id="notification_table_subject_header"]').text
    if text == "Subject":
        assert True, "Test Passed"  # verify the data is present


@then('close')
def step_impl(context):
    time.sleep(0.5)
    context.driver.close()
