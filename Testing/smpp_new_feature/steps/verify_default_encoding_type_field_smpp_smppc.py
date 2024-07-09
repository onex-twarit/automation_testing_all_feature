from behave import *
import time
from selenium.webdriver.common.by import By


@then('verify by default the GSM-7 encoding type is selected')
def by_default_encoding_type(context):
    time.sleep(1)
    text = context.driver.find_element(By.ID, 'encoding_type').get_attribute('value')
    if text == "gsm_7":
        assert True, f"{text} is present"
    else:
        assert False, f"{text} is not present"


