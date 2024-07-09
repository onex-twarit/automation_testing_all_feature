from behave import *
import time
from selenium.webdriver.common.by import By


@then('click on \'Show Campaign\' button')
def click_add_button(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'show_campaign')
    context.driver.execute_script("arguments[0].click();", button)

    # checking the length of the campaign
    check_length = len(context.driver.find_elements(By.XPATH, '//*[@id="tab_content"]/table/tbody/tr'))
    print(f"length is {check_length}")

    if check_length == 9:
        assert True, "campaign verified"
    else:
        assert False, "----->> Failed campaign verified with length 9"


@then('select the campaigns to delete')
def click_add_button(context):

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/table/tbody/tr[2]/td[1]/label/input')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/table/tbody/tr[4]/td[1]/label/input')
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/table/tbody/tr[6]/td[1]/label/input')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on \'Delete Selected\' button')
def click_add_button(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'delete_selected_campaign')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on delete on warning window')
def click_add_button(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'delete_save')
    context.driver.execute_script("arguments[0].click();", button)


# @then('verify if the campaigns are deleted')
# def verify_deleted_campaigns(context):
#     # check_camp1 = context.driver.find_element(By.XPATH, f'//td[contains(text(),"{context.camp1}")]')
#     # check_camp1 = context.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]')
#     check_camp1 = context.driver.find_element(By.XPATH, '//*[@id="tab_content"]/table/tbody').text
#     print(check_camp1)
#     if context.camp1 not in check_camp1.text:
#         assert True, "campaign verified"
#     else:
#         assert False, "----->> Failed campaign verified"

@then('verify if the campaigns are deleted')
def verify_deleted_campaigns(context):
    time.sleep(0.5)
    check_length_after_delete = len(context.driver.find_elements(By.XPATH, '//*[@id="tab_content"]/table/tbody/tr'))
    print(f"length is {check_length_after_delete}")

    if check_length_after_delete == 6:
        assert True, "campaign verified with length"
    else:
        assert False, "----->> Failed campaign verified with length 6"


@then('click on \'Delete All\' button')
def click_add_button(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'delete_all_campaign')
    context.driver.execute_script("arguments[0].click();", button)
