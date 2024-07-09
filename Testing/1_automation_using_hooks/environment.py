import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='/home/twarit/Downloads/chromedriver-linux64/chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


def before_scenario(context, steps):
    try:
        time.sleep(0.5)
        context.driver = driver
        context.driver.maximize_window()
    except NameError:
        print("Chrome browser did not open")
    else:
        print("Chrome browser open successfully")



def after_scenario(context, steps):
    time.sleep(0.5)
    context.driver.quit()


def after_step(context, steps):
    print()
