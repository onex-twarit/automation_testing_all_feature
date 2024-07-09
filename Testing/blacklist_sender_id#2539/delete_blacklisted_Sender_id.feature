Feature: Delete Blacklist Sender ID

  Scenario: Delete Blacklist Sender ID

    Given Launch the browser
    Then open login page
    And Enter user name and password for sa
    And open dashboard page, go to config
    And go to Blacklist sender ID tab
    And click on show button, delete the added sender ID
    And close