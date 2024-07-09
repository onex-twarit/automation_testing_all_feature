from telnetlib import EC

from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


@given('Launch browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@then('open loginnnn.py page for tenant user')
def step_impl(context):
    time.sleep(2)
    context.driver.get('http://localhost:8000/index')


@then('Enter user name and password')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("Onexadmin")
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("password")


@then('Click on the Sign in button')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="login_button"]').click()


@then('enter new password and confirm password')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="new_password"]').send_keys("Onextel@123")
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="confirm_password"]').send_keys("Onextel@123")


@then('Click on submit button')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="reset_button"]').click()


@then('open user management')
def step_impl(context):
    time.sleep(4)
    context.driver.find_element(By.XPATH, '//*[@id="menu_users"]/p').click()


@then('add TUC')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="create_tuc"]').click()


@then('fill TUC fields')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="name"]').send_keys("newtuc")                 # name
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="otp_acc_type"]').send_keys("On Delivery")    # otp_charges_type
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="trans_acc_type"]').send_keys("On Delivery")  # trans_charges_type
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="promo_acc_type"]').send_keys("On Delivery")  # promo_charges_type
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="gov_acc_type"]').send_keys("On Delivery")    # govt_charges_type
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="sim_acc_type"]').send_keys("On Delivery")    # sim_route_type
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="default_acc_type"]').send_keys(
        "On Delivery")  # default_charges_type
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="billing_type"]').send_keys("PREPAID")        # billing_type
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="validity"]').send_keys(30)                   # validity
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="mask_phone"]').send_keys("yes")              # mask_data
    time.sleep(0.5)
    button = context.driver.find_element(By.XPATH,
                                         "/html/body/div[1]/div[2]/div[3]/div[2]/div/div/div[2]/div/div[1]/div[25]/div[1]/label/input")
    context.driver.execute_script("arguments[0].click();", button)                               # gateway uncheck box

    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="childtuc"]').send_keys(5)                    # child_tuc
    time.sleep(1)
    button = context.driver.find_element(By.ID, 'save_tuc')
    context.driver.execute_script("arguments[0].click();", button)


@then('fill TUC user fields')
def step_impl(context):
    time.sleep(2)
    button = context.driver.find_element(By.XPATH,
                                         "//*[@id='user_view']")
    context.driver.execute_script("arguments[0].click();", button)
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="create_user"]').click()                 # click for add tuc user
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("ICICIAdmin")    # username
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("password")      # password
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="fname"]').send_keys("first")            # f_name
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="lname"]').send_keys("last")             # l_name
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("email@gmail.com")  # email
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="mob_no"]').send_keys(9876543210)        # m_num
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="comp_name"]').send_keys("onextel")      # company_name
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="web"]').send_keys("web@web.com")        # web
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="role_type"]').send_keys("TUC Admin")    # role_type
    time.sleep(0.5)
    context.driver.find_element(By.ID, 'tuc').send_keys("newtuc(2002)")                     # tenants
    time.sleep(0.5)
    context.driver.find_element(By.XPATH, '//*[@id="save_user"]').click()                   # button for adding tuc fields


@then('go to the profile button')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="profile_title"]').click()


@then('TUC user log out')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="log-out"]').click()
