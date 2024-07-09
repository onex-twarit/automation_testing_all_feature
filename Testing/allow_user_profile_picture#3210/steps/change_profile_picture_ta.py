from behave import *
import time
from selenium.webdriver.common.by import By


@then('go to User Management')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, "menu_users")
    context.driver.execute_script("arguments[0].click();", button)


@then('go to Tenants tab, click on show Tenants')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, "tenant_view")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, "show_tenant")
    context.driver.execute_script("arguments[0].click();", button)


@then('click on edit of Onexadmin')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         "(//td[contains(text(),'Onexadmin')]/following-sibling::td//a[@title='Edit'])[1]")
    context.driver.execute_script("arguments[0].click();", button)


@then('check allow user profile picture')
def step_impl(context):
    time.sleep(0.5)
    checkbox_user_profile = context.driver.find_element(By.XPATH,
                                                        "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[10]/div/div/div/label/input").is_selected()
    if not checkbox_user_profile:
        button = context.driver.find_element(By.XPATH,
                                             "/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[10]/div/div/div/label/input")
        context.driver.execute_script("arguments[0].click();", button)


@then('click on update')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, "update_tenant")
    context.driver.execute_script("arguments[0].click();", button)


@then('log out sa')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, "dropdown-caret")
    context.driver.execute_script("arguments[0].click();", button)

    time.sleep(0.5)
    button = context.driver.find_element(By.ID, "log-out")
    context.driver.execute_script("arguments[0].click();", button)


@then('go to profile section')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, "dropdown-caret")
    context.driver.execute_script("arguments[0].click();", button)


@then('go to My Account')
def step_impl(context):
    time.sleep(0.5)
    button = context.driver.find_element(By.ID, 'user-account')
    context.driver.execute_script("arguments[0].click();", button)


@then('upload logo')
def step_impl(context):
    time.sleep(0.5)


    fileupload.send_keys('/home/twarit/Desktop/company_logo.png')


@then('upload icon')
def step_impl(context):
    time.sleep(0.5)

    
    fileupload.send_keys('/home/twarit/Desktop/company_icon.png')


@then('upload login page logo')
def step_impl(context):
    time.sleep(0.5)


    fileupload.send_keys('/home/twarit/Desktop/login_page_logo.svg')
