import json
import time
import step
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import allure

service = Service(executable_path='/home/twarit/Downloads/chromedriver-linux64/chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def before_all(context):
    with open('Test_Data.json') as f:
        context.test_data = json.load(f)
    try:
        context.driver = webdriver.Chrome(ChromeDriverManager().install())
        context.driver.maximize_window()
        context.driver.implicitly_wait(5)
    except:
        time.sleep(0.5)
        context.driver = driver
        context.driver.maximize_window()


#
# def after_step(context, step):
#     screenshot = context.driver.get_screenshot_as_png()
#     allure.attach(screenshot, step.name, attachment_type=AttachmentType.PNG)


def before_step(context, step):
    print()
