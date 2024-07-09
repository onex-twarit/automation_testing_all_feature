Feature: Onextel tenant login

  Scenario: Dashboard for tenant

    Given Launch the browser
    Then open login page tenant
    And Enter user name and password tenant
    And dashboard page tenant
    And go to assign details tab
    And click on save changes and reset
    And close the browser tenant

