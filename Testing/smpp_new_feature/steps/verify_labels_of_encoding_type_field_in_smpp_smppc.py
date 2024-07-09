from behave import *
import time
from selenium.webdriver.common.by import By


@then('verify the labels of encoding type field')
def verify_encoding_type_label(context):
    # verify the new added field encoding type
    time.sleep(1)
    text = context.driver.find_element(By.ID, 'encoding_typepanel1').is_displayed()
    if text:
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"
