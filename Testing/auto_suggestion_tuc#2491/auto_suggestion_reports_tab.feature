Feature: Auto Suggestions(TUC)

  Scenario: Auto Suggestions in Reports tab

    Given Launch the browser
    Then open login page
    And Enter user name and password
    And open dashboard page, go to user management
    And go to reports, then summary tab, search for any tuc, select and search
    And go to campaign summary tab, search for any tuc, select and search
    And go to search tab, search for tuc and mobile number, select and search
    And go to sender ID summary tab, search for any tuc, select and search
    And go to latency report tab, search for any tuc, select and search
    And go to clicker data tab, search for tuc and mobile, select and search
    And go to clicker details tab, search for tuc, select and search
    And go to scheduled campaigns tab, search for tuc, select and search
    And close



