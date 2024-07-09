Feature: Login TUC first time

#    TEST CASE 4
  Scenario: Add credits to TUC
    Given open onextel Homepage "url"
    When Enter Tenant Username "ta_username" and password "ta_password"
    And Click the login button
    And go to Credits page
    And go to Userwise Allocation tab
    And click on Update Credit button
    And on the update credit pop select the newly created TUC "tuc_name" from dropdown
    And click on Add credits button and enter the credits "credits_tuc"
    And click on update button
    And verify the credits are credited to the TUC and debited from TA
    And log out
    And verify the login page is visible

  Scenario: Login TUC and verify the available credits
#    Given open onextel Homepage "url"
    When Enter Username for tuc "tuc_username" and password "tuc_invalid_pass"
    And Click the login button
    And In Tuc either dashboard page or change password page should appear "tuc_invalid_pass","tuc_password"
    And Verify that on the dashboard the TUC has 5000 available credits
    And Close driver window