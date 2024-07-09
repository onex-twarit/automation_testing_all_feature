from behave import *
import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then('go to New SMS')
def left_menu_new_sms(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'new_sms')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to quick english SMS')
def go_to_quick_english_sms(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'quick_eng_sms_title')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    avail_balance = context.driver.find_element(By.XPATH, '//*[@id="available_credits"]').text
    context.available_bal = int(str(avail_balance).replace(",", ""))
    print(avail_balance)


@then('add campaign with \'bulk_GW_camp_one\'')
def add_campaign(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'add_campaign_button')
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(0.5)
    context.driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/input').send_keys(
        'bulk_GW_camp_one')  # description
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'add_campaign')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    camp_name = Select(context.driver.find_element(By.ID, 'campaign_name')).first_selected_option.text
    start = camp_name.find('(') + 1
    end = camp_name.find(')')

    time.sleep(0.5)
    context.camp_id = camp_name[start:end]
    print(context.camp_id)


@then('select Sender ID \'ONEXTL\'')
def select_sender_id(context):
    time.sleep(0.5)
    select_name = context.driver.find_element(By.ID, 'sender_id')
    select = Select(select_name)
    select.select_by_visible_text('ONEXTL')


@then('add group test(22)')
def add_group(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'groupDropdown').send_keys('test (22)')  # adding group


@then('insert template English Short')
def insert_template_english_short(context):
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


@then('click on send')
def click_send_sms(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'send')
    context.driver.execute_script("arguments[0].click();", button)


@then('store the total credit counts')
def store_total_credits(context):
    time.sleep(2)
    context.total_credits = context.driver.find_element(By.XPATH,
                                                        "//label[contains(text(),'Total Required SMS')]/following-sibling::div/p").text
    print("total credits ", context.total_credits)


@then('on SMS confirmation window click on send now')
def click_send_now(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'confirm_send_sms')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on new sms')
def click_on_new_sms(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'confirm_send_sms')
    context.driver.execute_script("arguments[0].click();", button)


@then('verify the deducted credits')
def verify_deducted_credits(context):
    time.sleep(2)
    new_avail_bal = context.driver.find_element(By.XPATH, '//*[@id="available_credits"]').text
    context.new_avail_balance = int(str(new_avail_bal).replace(",", ""))
    print("before deduction ", context.total_credits, "after deduction ", context.new_avail_balance)
    assert context.available_bal == 22 + context.new_avail_balance  # verifying the credits


@then('go to Reports TUC')
def go_to_reports_tuc(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'menu_report')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to MIS tab, click on total counts')
def MIS_total_counts(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'pills-mis-data-tab')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(1)
    button = context.driver.find_element(By.XPATH, '//*[@id="customers"]/tbody/tr[32]/th[26]/a')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on search')
def click_on_search(context):
    time.sleep(2)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)


@then('find campaign bulk_GW_camp_one and click on view details')
def click_on_view_details(context):
    time.sleep(1)
    context.driver.execute_script("window.scrollTo(0, 0);")

    time.sleep(1)
    button = context.driver.find_element(By.XPATH, f'//*[@id="view_details_{context.camp_id}"]')
    context.driver.execute_script("arguments[0].click();", button)


@then('match the total deducted credits with submitted credits')
def match_the_credits(context):
    time.sleep(2)
    submitted_credits = context.driver.find_element(By.ID, 'submit_card_text').text
    print("submitted_credits ", submitted_credits)
    if submitted_credits == context.total_credits:
        assert True, "Test Passed"
    else:
        assert False, "=> Failed, submitted credits mismatched"

    # get one UUID
    time.sleep(2)
    context.uuid = context.driver.find_element(By.XPATH, '//*[@id="customers"]/tbody/tr[2]/td[3]').text
    print("uuid ", context.uuid)


@then('log out TUC')
def log_out_tuc(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'dropdown-caret')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(2)
    button = context.driver.find_element(By.ID, 'log-out')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to report SA')
def go_to_reports_sa(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_master_report')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to search tab')
def go_to_search_tab(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/ul/li[3]/a')
    context.driver.execute_script("arguments[0].click();", button)


@then('enter uuid for GW 207 and click on search')
def enter_uuid_and_search(context):
    time.sleep(1)
    enter_uuid = context.driver.find_element(By.XPATH,
                                             '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[1]/div/div[2]/input').send_keys(
        context.uuid)

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'search')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Gateway ID
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/table/tbody/tr[50]/td[2]').text
    if text == '207':
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed, Gateway ID mismatched"

    # Porter ID
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/table/tbody/tr[51]/td[2]').text
    if text == '1033':
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed, Porter ID mismatched"
