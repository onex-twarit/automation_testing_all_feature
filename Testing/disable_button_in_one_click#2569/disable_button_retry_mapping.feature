Feature: Disable show button in Retry Mapping

  Scenario: SA > Settings

    Given Launch the browser
    Then open login page
    And Enter user name and password
    And open dashboard page
    And go to settings
    And go to retry mapping tab
    And click on show retry gateways button (retry)
    And show retry gateways button should be disabled in one click (retry)
    And click on show button (retry)
    And it should be disabled in one click (retry)
    And close

