Feature: Onextel

  Scenario: Enable the TUC

    Given Launch the browser
    Then open login page
    And Enter user name and password
    And open dashboard page
    And go to User Management, search tuc by name
    And enable the tuc and check in active
    And close
