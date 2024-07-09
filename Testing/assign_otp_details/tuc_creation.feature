Feature: Onextel TUC login

  Scenario: Dashboard for TUC

    Given Launch browser
    Then open login page for tenant user
    And Enter user name and password
    And Click on the Sign in button
#    And enter new password and confirm password
#    And Click on submit button
    And open user management
    And add TUC
    And fill TUC fields
#    And create TUC user
    And fill TUC user fields
    And go to the profile button
    And TUC user log out

