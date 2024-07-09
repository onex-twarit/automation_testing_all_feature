Feature: Login in code

#    TEST CASE 3
  Scenario: Login TA first time
    Given open onextel Homepage "url"
    When Enter Tenant Username "ta_username" and password "ta_password"
    And Click the login button
    And In TA either dashboard page or change password page should appear "ta_pass","ta_new_password"

  Scenario: Create Tenant User Client
    Given go to User Management page
    When go to TUC tab
    And click on the Add TUC button
    And Verify the create TUC web page form is loaded
    And Enter the data for creation of TUC "tuc_name", "validity"
    And give licences, "child_tuc_", "s_mpps", "sms_api_"
    And click on create TUC button
    And verify the new TUC is created (using search button, new tuc should be visible)
#
  Scenario: Create TUC user
    Given go to User tab
    When click on the Add User tab
    And click on the Add User button
    And Verify the create user web page form is loaded
    And Enter the data for TUC user "tuc_username", "password", "first_name", "last_name", "email", "mob_num", "comp_name", "web"
    And select role type as TUC admin, then select name of newly created TUC "tuc_name"
    And click on create user button
    And verify the new user is created (using search button, new user should be visible)
    And log out

  Scenario: Login to new created TUC
    Given open onextel Homepage "url"
    When Enter Username for tuc "tuc_username" and password "tuc_invalid_pass"
    And Click the login button
    And In Tuc either dashboard page or change password page should appear "tuc_invalid_pass","tuc_password"
    And Verify that on the dashboard the tenant admin has a left-side menu option DLT


