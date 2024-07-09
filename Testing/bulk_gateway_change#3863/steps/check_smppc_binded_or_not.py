from behave import *
import time
from selenium.webdriver.common.by import By


@then('click on search smppc')
def click_on_search_smppc(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'search_host')
    context.driver.execute_script("arguments[0].click();", button)


@then('check SMPPC names AIRTEL and RETRY SMPPC are binded and bind if unbinded')
def check_smppc_is_binded_or_not(context):
    # AIRTEL SMPPC
    time.sleep(0.5)
    bg_color = context.driver.find_element(By.XPATH,
                                           '//td[contains(text(), "AIRTEL/AIRTEL/vendor_BSNL/")]').value_of_css_property(
        'background-color')
    if bg_color == 'rgba(209, 231, 221, 1)':
        print("smppc is binded")
        assert True, "Test Passed"
    else:

        time.sleep(0.5)
        button = context.driver.find_element(By.XPATH,
                                             "//tr[td[contains(text(), 'AIRTEL/AIRTEL/vendor_BSNL/')]]//button[contains(@title, 'Unbind')]")
        context.driver.execute_script("arguments[0].click();", button)

        time.sleep(1)
        button = context.driver.find_element(By.ID, 'search_host')
        context.driver.execute_script("arguments[0].click();", button)

        time.sleep(1)
        button = context.driver.find_element(By.XPATH,
                                             "//tr[td[contains(text(), 'AIRTEL/AIRTEL/vendor_BSNL/')]]//button[contains(@title, 'Bind')]")
        context.driver.execute_script("arguments[0].click();", button)
        print("smppc was un-binded, now binded")

    # RETRY SMPPC
    time.sleep(0.5)
    bg_color = context.driver.find_element(By.XPATH,
                                           '//td[contains(text(), "Retry SMPPC/AIRTEL/vendor_BSNL/")]').value_of_css_property(
        'background-color')
    if bg_color == 'rgba(209, 231, 221, 1)':
        print("smppc is binded")
        assert True, "Test Passed"
    else:

        time.sleep(0.5)
        button = context.driver.find_element(By.XPATH,
                                             "//tr[td[contains(text(), 'Retry SMPPC/AIRTEL/vendor_BSNL/')]]//button[contains(@title, 'Unbind')]")
        context.driver.execute_script("arguments[0].click();", button)

        time.sleep(1)
        button = context.driver.find_element(By.ID, 'search_host')
        context.driver.execute_script("arguments[0].click();", button)

        time.sleep(1)
        button = context.driver.find_element(By.XPATH,
                                             "//tr[td[contains(text(), 'Retry SMPPC/AIRTEL/vendor_BSNL/')]]//button[contains(@title, 'Bind')]")
        context.driver.execute_script("arguments[0].click();", button)
        print("smppc was un-binded, now binded")
