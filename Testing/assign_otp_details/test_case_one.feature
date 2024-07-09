Feature: Onextel tenant login

  Scenario: Dashboard for tenant

    Given Launch browser for tenant
    Then open login page for tenant
    And Enter user name and password for tenant
    And dashboard page tenant
    And go to assign otp details tab
    And verify the present fields
    And close browser for tenant

