Feature: Auto Suggestions(TUC)

  Scenario: Auto Suggestions in TUC tab

    Given Launch the browser
    Then open login page
    And Enter user name and password
    And open dashboard page, go to user management
    And go to TUC tab, search for any tuc, select and search
    And close

