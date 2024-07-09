Feature: Blacklist Sender ID

  Scenario: Blacklist Sender ID from SA and TA

    Given Launch the browser
    Then open login page
    And Enter user name and password for sa
    And open dashboard page, go to config
    And go to Blacklist sender ID tab
    And click on add sender ID blacklist button
    And enter sender ID and description then click on add button
    And logout sa and Enter user name and password for tuc
    And open dashboard page, click on New SMS button
    And go to quick english SMS tab
    And check in Sender ID field, it should not come
    And close