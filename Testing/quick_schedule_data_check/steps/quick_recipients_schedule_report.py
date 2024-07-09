from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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
    context.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("ICICIAdmin")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("Onextel@123")
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="login_button"]').click()


@then('open dashboard page')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, "//*[@id='dashboard_title']").text
    if text == "Dashboard":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"

    time.sleep(2)
    avail_balance = context.driver.find_element(By.XPATH, '//*[@id="available_credits"]').text
    context.available_bal = int(str(avail_balance).replace(",", ""))


@then('click on click on new sms, click on quick sms')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="new_sms"]').click()  # go to NEW SMS

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="quick_eng_sms_title"]')
    context.driver.execute_script("arguments[0].click();", button)  # go to quick english SMS


@then('add campaign \'quick camp\', fill the present fields, click on Add')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '//*[@id="add_campaign_button"]')
    context.driver.execute_script("arguments[0].click();",
                                  button)  # click on add campaign button on campaign name field

    time.sleep(0.5)
    context.driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/input').send_keys(
        "quick camp")  # campaign name
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'campaign_desc').send_keys("Desc")  # description
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'add_campaign').click()  # click on add button


@then('then add sender ID, add recipients, insert template')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="recipient_numbers"]').send_keys(9950500435)

    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="insert_template"]').click()  # go to insert template

    time.sleep(1)
    context.driver.implicitly_wait(30)
    action = (ActionChains(context.driver))
    type = context.driver.find_element(By.ID, 'template_type_id')  # select template type

    action.move_to_element(type).click().perform()

    time.sleep(0.5)
    action.key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).click().perform()

    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, "template_filter_id"))
    select.select_by_visible_text("Search")

    time.sleep(0.5)
    context.driver.find_element(By.ID, 'modal_template_id').send_keys('English Short')

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, "//li[@class='ui-menu-item']/div[text()='English Short']").click()

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'insert_template_to_msg')
    context.driver.execute_script("arguments[0].click();", button)  # click on select button


@then('check schedule sms for 1 hour')
def step_impl(context):
    time.sleep(1)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[6]/div[1]/label[1]/input')
    context.driver.execute_script("arguments[0].click();", button)  # check schedule box

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="schedule_row_hour"]').send_keys(18)


@then('click on schedule, then on schedule now button')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'send')
    context.driver.execute_script("arguments[0].click();", button)  # click on schedule button

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'confirm_send_sms')
    context.driver.execute_script("arguments[0].click();", button)  # click on schedule now button


@then('click on New SMS')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'new_sms')
    context.driver.execute_script("arguments[0].click();", button)  # click on new sms button


@then('go to Reports, go to MIS tab')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="menu_report"]/p').click()  # go to report tab

    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="pills-tab"]/li[1]').click()  # go to MIS tab

    time.sleep(1)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(2)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div/table/tbody/tr[14]/td[20]/a')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1.5)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)  # click on search button


@then('verify with name \'quick camp\'')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[3]/div/table/tbody/tr[2]/td[4]/div').text
    if text == 'quick camp':
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('go to summary tab check all and web')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, 'pills-summary-tab').click()  # go to summary tab

    time.sleep(2)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)  # click on search button

    time.sleep(2)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[3]/table/tbody/tr[3]/th[3]').text
    if text == "1":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"

    time.sleep(2)
    select = Select(driver.find_element(By.ID, 'source_type_summary'))
    select.select_by_visible_text('WEB')

    time.sleep(2)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)  # click on search button

    time.sleep(2)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[3]/table/tbody/tr[3]/th[3]').text
    if text == "1":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('go to scheduled campaign, verify \'quick camp\' name')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, 'pills-campaign-tab')
    context.driver.execute_script("arguments[0].click();", button)  # go to scheduled campaign tab

    time.sleep(2)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)  # click on search button

    time.sleep(2)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/table/tbody/tr[2]/td[4]/div').text
    if text == "quick camp":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('delete schedule')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/a[1]/img')
    context.driver.execute_script("arguments[0].click();", button)  # go to dashboard

    time.sleep(1)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(1)
    button = context.driver.find_element(By.ID, 'collapsable_schedule')
    context.driver.execute_script("arguments[0].click();", button)  # click scheduled sms dropdown

    time.sleep(1.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[5]/div[2]/div/table/tbody/tr[2]/td[9]/a/img')
    context.driver.execute_script("arguments[0].click();", button)  # click delete

    time.sleep(1)
    button = context.driver.find_element(By.ID, 'quick_sms_confirm_delete_delete')
    context.driver.execute_script("arguments[0].click();", button)  # click delete on warning pop-up


@then('close')
def step_impl(context):
    time.sleep(1)
    context.driver.close()
