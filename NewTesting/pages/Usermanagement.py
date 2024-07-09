from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class UserManagement:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    userManagementPage_id = {"id": "menu_users"}
    addTenantButtonId = {"id": "create_tenant"}
    tenant_name_txtbox_id = {"id": "name"}
    tenant_desc_textbox_id = {"id": "description"}

    # licences tuc
    tenant_child_tuc_txtbox_id = {"id": "childtuc"}
    tenant_smpps_textbox_id = {"id": "smpps"}
    tenant_api_textbox_id = {"id": "smsapi"}

    create_tenant_btn_id = {"id": "save_tenant"}
    tenant_data_label = {"xpath": "//td[contains(text(),'Test')]"}
    tenant_show_btn_id = {"id": "show_tenant"}
    tenant_usertab_id = {"id": "user_view"}
    tenant_adduser_btn_id = {"id": "create_user"}
    tenant_username_txt_id = {"id": "username"}
    tenant_password_txt_id = {"id": "password"}

    # create user
    tenant_fname_txt_id = {"id": "fname"}
    tenant_lname_txt_id = {"id": "lname"}
    tenant_email_txt_id = {"id": "email"}
    tenant_mobno_txt_id = {"id": "mob_no"}
    tenant_compname_txt_id = {"id": "comp_name"}
    tenant_web_txt_id = {"id": "web"}

    tenant_roletype_txt_id = {"id": "role_type"}
    tenant_tenantname_option_id = {"id": "tenant"}
    tenant_createuser_btn_id = {"id": "save_user"}
    tenant_searchuser_btn = {"id": "user_search"}
    create_tenant_label = {"xpath": "//p[text()='Create Tenant']"}
    create_user_label = {"xpath": "//p[text()='Create User']"}
    search_user_field = {"id": "user_input"}
