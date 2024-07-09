from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Credits:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 4)

    update_crdit_label = {"id": "credit_alloc_update_credits_label"}
    add_credit_btn = {"xpath": "//input[@value='addCredit']"}
    credits_page = {"id": "menu_credit_allocation"}
    update_credits_btn = {"id": "update_credits"}
    update_credit_btn = {"id": "updateCredit"}
    credits_txtbox = {"id": "credits_amount"}

    available_credits = {"id": "available_credits"}
    credits_left_menu = {"id": "menu_credit_allocation"}
    add_credits_radio_button = {
        "xpath": "//label[text()='Add-Credits']"}

    userwise_allocation = {"id": "pills-user-alloc"}
