Feature: Onextel

  Scenario: check TUC's in all status

    Given Launch the browser
    Then open login page
    And Enter user name and password
    And open dashboard page
    And go to report, check all in tuc status
    And search tuc by name and check
    And close
