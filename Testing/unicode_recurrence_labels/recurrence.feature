Feature: Onextel tuc login

  Scenario: Recurrence

    Given Launch the browser
    Then open login page
    And Enter user name and password
    And open dashboard page
    And go to NEW SMS then to quick unicode
    And present fields to be filled
    And check on recurrence, verify the labels and click on send
    And on new window click on proceed
    And check if message is sent
    And close the browser
