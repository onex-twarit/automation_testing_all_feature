from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.Login import Login


class MasterCredits:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    page_label = {"xpath": "//p[text()='Master Credits']"}
    master_credits_page = {"id": "menu_master_balance"}
    update_credits_label = {"id": "balance_title"}
    credits_txtbox = {"id": "amount"}
    add_btn = {"id": "add"}
    main_credits_text = {"id": "available_credits"}
    update_credits_btn = {"id": "update_balance"}

    def convert_comma_seperate_number(self, element):
        comma_separated_number = Login(self.driver).get_element(element).text
        return int(comma_separated_number.replace(",", ""))

    def comma_creds(creds):
        return int(creds.replace(",", ""))
