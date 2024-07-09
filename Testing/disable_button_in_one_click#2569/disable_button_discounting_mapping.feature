Feature: Disable show button in Discounting Mapping

  Scenario: SA > Settings

    Given Launch the browser
    Then open login page
    And Enter user name and password
    And open dashboard page
    And go to settings
    And go to discounting mapping tab
    And click on show button (discounting)
#    And it should be disabled in one click (discounting)
    And close

