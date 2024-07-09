from selenium.webdriver.common.by import By
from pages.Login import Login
from behave import *
import time


@when('click on show tenant')
def step_impl(context):
    button = context.driver.find_element(By.ID, "show_tenant")
    context.driver.execute_script("arguments[0].click();", button)


@when('click on onexadmin credits button and delete 100000 credits and ta')
def step_impl(context):
    # delete credits
    time.sleep(1)
    button = context.driver.find_element(By.XPATH,
                                         "//td[contains(text(),'onexadmin')]/following-sibling::td//a[@title='Manage Credit']")
    context.driver.execute_script("arguments[0].click();", button)

    # enter credits 100000
    time.sleep(1)
    context.driver.find_element(By.ID, "credits_amount").send_keys("100000")

    time.sleep(1)
    button = context.driver.find_element(By.XPATH, "//label[text()='Deduct-Credits']")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    button = context.driver.find_element(By.ID, "update_credits")
    context.driver.execute_script("arguments[0].click();", button)

    # delete the tenant
    time.sleep(1)
    button = context.driver.find_element(By.XPATH,
                                         "//td[contains(text(),'onexadmin')]/following-sibling::td//a[@title='Delete']")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    button = context.driver.find_element(By.ID, "delete_save")
    context.driver.execute_script("arguments[0].click();", button)


@when('go to users tab ta and click on search')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "user_view")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(1)
    button = context.driver.find_element(By.ID, "user_search")
    context.driver.execute_script("arguments[0].click();", button)


@when('delete user tenant1admin12')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.XPATH,
                                         "//td[contains(text(),'tenant1admin12')]/following-sibling::td//a[@title='Delete']")
    context.driver.execute_script("arguments[0].click();", button)

    # delete user
    time.sleep(1)
    button = context.driver.find_element(By.ID, "delete_save")
    context.driver.execute_script("arguments[0].click();", button)


@when(u'go to User Management page')
def step_impl(context):
    time.sleep(1)
    Login(context.driver).click_button(Login.user_management_left_menu)


@when('click on newtuc credits button and delete 5000 credits and tuc')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "tuc_view")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(1)
    button = context.driver.find_element(By.ID, "user_search")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(1)
    button = context.driver.find_element(By.XPATH,
                                         "//td[contains(text(),'newTuc')]/following-sibling::td//a[@title='Manage Credit']")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(1)
    context.driver.find_element(By.ID, "credits_amount").send_keys("5000")

    time.sleep(1)
    button = context.driver.find_element(By.XPATH, "//label[text()='Deduct-Credits']")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    button = context.driver.find_element(By.ID, "update_credits")
    context.driver.execute_script("arguments[0].click();", button)

    # delete the tuc
    time.sleep(1)
    button = context.driver.find_element(By.XPATH,
                                         "//td[contains(text(),'newTuc')]/following-sibling::td//a[@title='Delete']")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    button = context.driver.find_element(By.ID, "delete_save")
    context.driver.execute_script("arguments[0].click();", button)


@when('go to users tab tuc and click on search')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.ID, "user_view")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(1)
    button = context.driver.find_element(By.ID, "user_search")
    context.driver.execute_script("arguments[0].click();", button)


@when('delete user newTucUser')
def step_impl(context):
    time.sleep(1)
    button = context.driver.find_element(By.XPATH,
                                         "//td[contains(text(),'newTucUser')]/following-sibling::td//a[@title='Delete']")
    context.driver.execute_script("arguments[0].click();", button)

    # delete user
    time.sleep(1)
    button = context.driver.find_element(By.ID, "delete_save")
    context.driver.execute_script("arguments[0].click();", button)
