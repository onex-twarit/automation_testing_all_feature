Feature: Disable show button in Error Mapping

  Scenario: SA > Settings

    Given Launch the browser
    Then open login page
    And Enter user name and password
    And open dashboard page
    And go to settings
    And go to error mapping tab
    And click on show gateways button (error)
    And show gateways button should be disabled in one click (error)
    And click on show button (error)
    And it should be disabled in one click (error)
    And close

