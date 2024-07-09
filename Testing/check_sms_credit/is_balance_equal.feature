Feature: Onextel tuc login

  Scenario: Recurrence

    Given Launch the browser
    Then open login page
    And Enter user name and password for tuc user
    And open dashboard page for tuc user
    And go to NEW SMS then to quick unicode
    And present fields to be filled and check current credit
    And check on recurrence, set timing and click on send
    And after clicking on proceed substract total credits from current credit and check
    And close the browser
