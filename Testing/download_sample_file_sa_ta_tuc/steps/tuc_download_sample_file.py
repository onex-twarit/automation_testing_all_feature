from behave import *
import time
from selenium.webdriver.common.by import By


@then('go to New SMS')
def step_impl(context):
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'new_sms').click()  # go to NEW SMS


@then('click on Dynamic SMS')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'dynamic_sms_title')
    context.driver.execute_script("arguments[0].click();", button)  # go to campaign SMS


@then('verify the labels for CSV and XLSX/XLS sample dynamic')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/label').text
    if text == "CSV Sample":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/label').text
    if text == "XLSX/XLS Sample":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then('click on CSV sample dynamic')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/input')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on save file in dynamic')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'dynamic_save_file')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on XLSX/XLS sample dynamic')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/input')
    context.driver.execute_script("arguments[0].click();", button)


@then(u'close the sample file pop-up dynamic')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'dynamic_close_button')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on Multiple Dynamic SMS')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'multi_dyn_sms_title')
    context.driver.execute_script("arguments[0].click();", button)  # go to multiple dynamic SMS


@then('verify the labels for CSV and XLSX/XLS sample multiple')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/label').text
    if text == "CSV Sample":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/label').text
    if text == "XLSX/XLS Sample":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then('click on CSV sample multiple')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/input')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on save file in multiple dynamic')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'multi_dynamic_save_file')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on XLSX/XLS sample multiple')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/input')
    context.driver.execute_script("arguments[0].click();", button)


@then('close the sample file pop-up multiple')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'download_close_btn')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on Campaign SMS')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'camp_sms_title')
    context.driver.execute_script("arguments[0].click();", button)  # go to campaign SMS


@then('verify the labels for CSV and XLSX/XLS sample campaign')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/label').text
    if text == "CSV Sample":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/label').text
    if text == "XLSX/XLS Sample":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then('click on CSV sample campaign')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/input')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on save file in campaign')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'sample_file_save_file_btn')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on XLSX/XLS sample campaign')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/input')
    context.driver.execute_script("arguments[0].click();", button)


@then('close the sample file pop-up campaign')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'sample_file_close_btn')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to DLT')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_manage')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Bulk Upload tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'bulktemplate_tab')
    context.driver.execute_script("arguments[0].click();", button)


@then('verify the labels for CSV and XLSX/XLS sample bulk')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/label').text
    if text == "CSV Sample":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[2]/label').text
    if text == "XLSX/XLS Sample":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then('click on CSV sample bulk')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/input')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on save file in bulk upload')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'manage_download_save_file')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on XLSX/XLS sample bulk')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[2]/input')
    context.driver.execute_script("arguments[0].click();", button)


@then('close the sample file pop-up bulk')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'manage_download_sample_close_btn')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Phonebook')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'menu_phonebook')
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Contacts tab')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'contacts')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on add contacts button')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'add-contacts')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on upload bulk contact button')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/input[2]')
    context.driver.execute_script("arguments[0].click();", button)


@then('verify the labels for CSV and XLSX/XLS sample contacts')
def step_impl(context):
    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[1]/label').text
    if text == "CSV Sample":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"

    time.sleep(1)
    text = context.driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/label').text
    if text == "XLSX/XLS Sample":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


@then('click on CSV sample contacts')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[1]/input')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on save file in contacts')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'download_sample_save_file_text')
    context.driver.execute_script("arguments[0].click();", button)


@then('click on XLSX/XLS sample contacts')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/input')
    context.driver.execute_script("arguments[0].click();", button)


@then('close the sample file pop-up contacts')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'download_sample_close_contacts')
    context.driver.execute_script("arguments[0].click();", button)
