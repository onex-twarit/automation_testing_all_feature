from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from behave import *
import time


@then('verify three options are present in the dropdown encoding type')
def by_default_encoding_type(context):
    time.sleep(1)
    count_options = context.driver.find_element(By.ID, 'encoding_type')
    verify_options = len(Select(count_options).options)
    print(verify_options)
    if verify_options == 3:
        assert True, f"{verify_options} is present"
    else:
        assert False, f"{verify_options} is not present"
