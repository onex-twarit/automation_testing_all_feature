Feature: Onextel TUC user login

  Scenario: Dashboard for TUC user

    Given Launch browser tuc user
    Then open login page for tuc user
    And Enter user name and password for tuc user
    And Click on the Sign in button for tuc user
    And Welcome to dashboard page for tuc user
    And go to DLT and add Entity ID
    And add sender ID
    And add template