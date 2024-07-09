import export
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from pages.Login import Login


class Tuc:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    user_search = {"id": "user_search"}
    tuc_search = {"id": "user_search"}

    # GW
    onex_gateway = {"name": "onex_gateway"}
    # create_tuc_fields
    tuc_username = {"id": "username"}
    first_name = {"id": "fname"}
    last_name = {"id": "lname"}
    email = {"id": "email"}
    mobile_number = {"id": "mob_no"}
    company_name = {"id": "comp_name"}
    web = {"id": "web"}

    # TUC INFO
    OTP_charges_type = {"id": "otp_acc_type"}
    trans_charges_type = {"id": "trans_acc_type"}
    promo_charges_type = {"id": "promo_acc_type"}
    govt_charges_type = {"id": "gov_acc_type"}
    sim_route_charges_type = {"id": "sim_acc_type"}
    default_charges_type = {"id": "default_acc_type"}
    billing_type = {"id": "billing_type"}

    # TUC
    tuc_tab = {"id": "tuc_view"}
    create_tuc_button = {"id": "save_tuc"}
    user_tab = {"id": "user_view"}
    add_user_tab = {"id": "add_user_tab"}
    add_tuc_button = {"id": "create_tuc"}
    tenant_adduser_btn_id = {"id": "create_user"}
    tenant_createuser_btn_id = {"id": "save_user"}
    dlt_left_menu = {"id": "menu_manage"}
    log_out_dropdown = {"id": "dropdown-caret"}
    log_out = {"id": "log-out"}

    # licences tuc
    tenant_child_tuc_txtbox_id = {"id": "childtuc"}
    tenant_smpps_textbox_id = {"id": "smpps"}
    tenant_api_textbox_id = {"id": "smsapi"}
