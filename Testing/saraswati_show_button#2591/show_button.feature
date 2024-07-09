Feature: Show button in User Management(TUC)

  Scenario: display data with show button

    Given Launch the browser
    Then open login page
    And Enter user name and password for tuc
    And open dashboard page, go to campaign
    And click on show campaign button, data should be present
    And go to User management, go to TUC tab, click on search
    And go to User tab, click on search, verify the data is visible
    And go to DLT, go to Entity ID tab, click on show button with enable/disable
    And go to Sender ID tab, click on show button with enable/disable
    And go to Template tab, click on search button with enable/disable
    And go to API, click on Show API button check button is disabled and enabled
    And go to Phonebook, go to Groups tab, click on show group button
    And go to Config, go to Blacklist Category, click on show button and check E/D
    And go to Whitelist Category, click on show button and check E/D
    And go to Notification, click on show Notification button
    And close

