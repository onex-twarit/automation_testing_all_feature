from behave import *
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@given('Launch Chrome browser')
def step_impl(context):
    opt = Options()
    opt.add_argument("--headless")
    context.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=opt)
    context.driver.maximize_window()

    # context.driver = webdriver.Chrome(executable_path='/home/twarit/Downloads/chrome-linux64/chrome')
    # context.driver = webdriver.Chrome(executable_path=r'/home/twarit/Downloads/chrome-linux64/chrome', options=Options())
    # context.driver = webdriver.Chrome()


@when('open loginnnn.py page')
def step_impl(context):
    time.sleep(2)
    context.driver.get('http://localhost:8000/index')


@when('Enter username and password')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("onexsa")
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("onexsa")


@when('Click on Sign in button')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="login_button"]').click()


@when('Welcome to dashboard page')
def step_impl(context):
    time.sleep(2)
    text = context.driver.find_element(By.XPATH, "//*[@id='dashboard_title']").text
    if text == "Dashboard":
        assert True, "Test Passed"


@when('go to user management')
def step_impl(context):
    time.sleep(4)
    context.driver.find_element(By.XPATH, '//*[@id="menu_users"]/p').click()


@when('add tenant')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="create_tenant"]').click()


@when('Enter tenant fields')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="name"]').send_keys("newtenant")  # tenant name
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="mask_phone"]').send_keys("yes")  # mask data
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="description"]').send_keys("desc")  # desc
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="childtuc"]').send_keys(10)  # child tuc


@when('create tenant')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="save_tenant"]').click()


@when('tenant created')
def step_impl(context):
    time.sleep(4)
    context.driver.get('http://localhost:8000/users')


@when('go to tenant user')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="user_view"]').click()


@when('create tenant user')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="create_user"]').click()


@when('enter tenant user fields')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("Onexadmin")  # username
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("password")  # password
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="fname"]').send_keys("first")  # f_name
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="lname"]').send_keys("last")  # l_name
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("email@gmail.com")  # email
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="mob_no"]').send_keys(9876543210)  # m_num
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="comp_name"]').send_keys("onextel")  # company_name
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="web"]').send_keys("web@web.com")  # web
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="role_type"]').send_keys("Tenant Admin")  # role_type
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="tenant"]').send_keys("newtenant(19)")  # tenants


@when('tenant user created')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="save_user"]').click()


@when('go to profile button')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="profile_title"]').click()


@when('log out')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH, '//*[@id="log-out"]').click()
