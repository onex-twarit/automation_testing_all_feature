from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    link_login_error_message = {"xpath": "//a[contains(@href,'login/identify')]"}
    sign_in_label = {"xpath": "//p[text()='Sign In']"}
    change_password_label = {"xpath": "//p[text()='Change Password']"}
    dashboard_page_label = {"id": "dashboard_title"}
    hub_page_label = {"xpath": "//p[text()='HUB']"}
    new_password_txtbox = {"id": "new_password"}
    cnfm_password_txtbox = {"id": "confirm_password"}
    submit_btn = {"id": "reset_button"}
    user_management_pagelabel = {"xpath": "//p[text()='User Management']"}
    invalid_password_xpath = {"xpath": "//span[text()='Invalid UserName or Password']"}
    newpass_errormsg_id = {"id": "newpass_errormsg"}
    profile = {"id": "profile"}
    logout = {"xpath": "//li/a[@id='log-out']"}

    # buttons and fields ta
    input_field_login = {"id": "email"}
    input_field_password = {"id": "password"}
    button_Signin = {"id": "login_button"}

    # # labels
    user_management_left_menu = {"id": "menu_users"}
    create_tuc_page_label = {"xpath": "//h5[text()='Tuc Info']"}
    create_user_page_label = {"xpath": "//h5[text()='User Info']"}

    def enter_txt_field(self, element, txt_value):
        self.wait.until(
            EC.visibility_of_element_located((list(element.keys())[0], list(element.values())[0]))).send_keys(
            txt_value)

    def click_btn_js(self, element):
        Btn = self.wait.until(EC.visibility_of_element_located((list(element.keys())[0], list(element.values())[0])))
        self.driver.execute_script("arguments[0].click();", Btn)

    def click_button(self, element):
        self.wait.until(EC.visibility_of_element_located((list(element.keys())[0], list(element.values())[0]))).click()

    def select_from_dropdown(self, locator, visible_text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        select = Select(element)
        select.select_by_visible_text(visible_text)

    def clear_element(self, element):
        self.wait.until(EC.visibility_of_element_located((list(element.keys())[0], list(element.values())[0]))).clear()

    def verify_labels(self, element, label):
        self.final_txt = self.wait.until(
            EC.presence_of_element_located((list(element.keys())[0], list(element.values())[0]))).text
        if self.final_txt == label:
            assert True, f"final_txt{self.final_txt}"
        else:
            assert False, f"exception occurred ---> {self.final_txt}"

    def get_element(self, element):
        return self.wait.until(EC.presence_of_element_located((list(element.keys())[0], list(element.values())[0])))

    def element_enabled(self, element):
        ele = self.wait.until(
            EC.visibility_of_element_located((list(element.keys())[0], list(element.values())[0]))).is_enabled()
        if ele:
            assert True, f"element {ele} is present"
        else:
            assert False, f"element {ele} is absent"
