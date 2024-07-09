Feature: Onextel tuc login

  Scenario: Schedule SMS

    Given Launch the browser
    Then open login page
    And Enter user name and password
    And open dashboard page
    And go to NEW SMS then to quick english sms
    And add recipients
    And present fields to be filled
    And check on schedule sms, split into campaigns and click on send
    And new window for confirmation
    And again on new window click on proceed
    And check if message is sent
    And close the browser
