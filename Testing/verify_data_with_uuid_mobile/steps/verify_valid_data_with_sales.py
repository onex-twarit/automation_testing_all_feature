from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then('click on click on new sms, click on quick sms')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'new_sms').click()  # go to NEW SMS

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'quick_eng_sms_title')
    context.driver.execute_script("arguments[0].click();", button)  # go to quick english SMS


@then('select campaign for sales')
def step_impl(context):
    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, "campaign_name"))
    select.select_by_visible_text('campaign sales(2575)')


@then('select sender ID')
def step_impl(context):
    time.sleep(0.5)
    temp = context.driver.find_element(By.ID, 'sender_id')  # select sender ID
    select = Select(temp)
    select.select_by_visible_text("123456")


@then('add recipients for sales')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'recipient_numbers').send_keys("6262923190")


@then('insert short template, select filter as dropdown')
def step_impl(context):
    time.sleep(0.5)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(0.5)
    context.driver.find_element(By.ID, 'insert_template').click()  # go to insert template

    time.sleep(0.5)
    context.driver.implicitly_wait(30)
    action = (ActionChains(context.driver))
    type = context.driver.find_element(By.ID, 'template_type_id')  # select template type

    action.move_to_element(type).click().perform()

    time.sleep(0.5)
    action.key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).click().perform()

    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, "template_filter_id"))
    select.select_by_visible_text('Dropdown')

    time.sleep(0.5)
    select = Select(context.driver.find_element(By.ID, 'modal_template_id'))
    select.select_by_visible_text('English Short')

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'insert_template_to_msg')
    context.driver.execute_script("arguments[0].click();", button)  # click on select button


@then('click on send, then send now')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'send')
    context.driver.execute_script("arguments[0].click();", button)  # click on send button

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'confirm_send_sms')
    context.driver.execute_script("arguments[0].click();", button)  # click on send now button


@then('click on New SMS')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'new_sms')
    context.driver.execute_script("arguments[0].click();", button)  # click on new sms button


@then('go to reports')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'menu_report')
    context.driver.execute_script("arguments[0].click();", button)  # click on reports from left menu


@then('click on MIS tab')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'pills-mis-data-tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on total counts and click on search')
def step_impl(context):
    time.sleep(2)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # scroll down

    time.sleep(2)
    button = context.driver.find_element(By.XPATH, '//*[@id="total_msg_count"]/a')
    context.driver.execute_script("arguments[0].click();", button)  # click on total counts

    time.sleep(2)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)  # click on search


@then('click on view details with TUC name \'sales\'')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH, "//td[contains(text(),'sales')]/following-sibling::td[26]/a")
    context.driver.execute_script("arguments[0].click();", button)


@then('store mobile number, uuid, sender ID')
def step_impl(context):
    time.sleep(1)
    context.uuid = context.driver.find_element(By.XPATH,
                                               "//td[contains(text(),'sales')]/following-sibling::td[1]").text

    time.sleep(1)
    context.sender_id = context.driver.find_element(By.XPATH,
                                                    "//td[contains(text(),'sales')]/following-sibling::td[2]").text

    time.sleep(1)
    context.mobile_num = context.driver.find_element(By.XPATH,
                                                     "//td[contains(text(),'sales')]/following-sibling::td[3]").text


@then('go to search tab select sales TUC')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "pills-search-tab")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    context.driver.find_element(By.ID, "tuc-report").send_keys("sales(2025)")


@then('select filter as mobile')
def step_impl(context):
    time.sleep(1)
    select = Select(context.driver.find_element(By.ID, "select_filter"))
    select.select_by_visible_text('Mobile')

    time.sleep(1)
    context.driver.find_element(By.ID, "number").send_keys(f"{context.mobile_num}")


@then('click on search')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "search")
    context.driver.execute_script("arguments[0].click();", button)


@then('verify the data')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH, '//*[@id="search-table"]/tbody/tr[1]/th[1]').text
    if text == "TUC ID":
        assert True, "Test Passed"
    else:
        assert False, "----->> Failed"


@then('select filter as UUID')
def step_impl(context):
    time.sleep(1)
    select = Select(context.driver.find_element(By.ID, "select_filter"))
    select.select_by_visible_text('UUID')

    time.sleep(1)
    context.driver.find_element(By.ID, "uuid").send_keys(f"{context.uuid}")


@then('select filter as sender ID with mobile')
def step_impl(context):
    time.sleep(1)
    select = Select(context.driver.find_element(By.ID, "select_filter"))
    select.select_by_visible_text('Sender ID with Mobile')

    time.sleep(1)
    context.driver.find_element(By.ID, "number").send_keys(f"{context.mobile_num}")
    time.sleep(1)
    context.driver.find_element(By.ID, "sender_id").send_keys(f"{context.sender_id}")
