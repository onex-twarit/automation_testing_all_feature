Feature: Login TUC first time

#    TEST CASE 4
  Scenario: Login TUC first time
    Given open onextel Homepage "url"
    When Enter Username for tuc "tuc_username" and password "tuc_invalid_pass"
    And Click on login button then enter valid password for tuc "tuc_password"
#    And Verify the dashboard page and change the password if change password pop-up appears "<new_password>"
    And Verify that on the dashboard the tenant admin has a left-side menu option “DLT”
    And Verify that on the dashboard the TUC has 5000 available credits
    And Close driver window
