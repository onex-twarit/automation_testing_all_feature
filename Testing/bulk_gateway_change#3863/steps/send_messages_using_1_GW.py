from behave import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@then('add campaign with \'bulk_GW_camp_two\'')
def add_campaign(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'add_campaign_button')
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(0.5)
    context.driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/input').send_keys(
        'bulk_GW_camp_two')  # description
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


@then('find campaign bulk_GW_camp_two and click on view details')
def click_on_view_details(context):
    time.sleep(1)
    context.driver.execute_script("window.scrollTo(0, 0);")

    time.sleep(1)
    button = context.driver.find_element(By.XPATH, f'//*[@id="view_details_{context.camp_id}"]')
    context.driver.execute_script("arguments[0].click();", button)


@then('enter uuid for GW 208 and click on search')
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
    if text == '208':
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed, Gateway ID mismatched"

    # Porter ID
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]/table/tbody/tr[51]/td[2]').text
    if text == '1034':
        assert True, "Test Passed"
    else:
        assert False, "============>> Failed, Porter ID mismatched"
