Feature: Onextel tenant login

  Scenario: Dashboard for tenant

    Given Launch browser for the tenant
    Then open login page for the tenant
    And Enter user name and password for the tenant
    And dashboard page for tenant
    And go to otp details tab
    And click on save changes and verify error labels
    And close the browser

