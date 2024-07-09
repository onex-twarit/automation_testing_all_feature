Feature: Auto Suggestions(TUC)

  Scenario: Auto Suggestions in User tab

    Given Launch the browser
    Then open login page
    And Enter user name and password
    And open dashboard page, go to user management
    And go to User tab, search for any user, select and search
    And close


