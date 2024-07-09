Feature: Onextel

  Scenario: disable the TUC
#Login to Tenant – User Management – Search by TUC name – disable tuc – close.

    Given Launch the browser
    Then open login page
    And Enter user name and password
    And open dashboard page
    And go to User Management, search tuc by name
    And disable the tuc and check in inactive
    And close
