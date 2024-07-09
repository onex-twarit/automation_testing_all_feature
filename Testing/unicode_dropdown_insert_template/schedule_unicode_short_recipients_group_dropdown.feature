Feature: unicode recipients

  Scenario: unicode recipients
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "ICICIAdmin" and password "Onextel@123"
    And Click on login button
    And open dashboard page
    And click on click on new sms, click on unicode sms
    And select campaign RCF(2348)
    And select sender ID
    And add recipients
    And add group
    And insert hindi short template, select filter as dropdown
    And check allow multi part sms box
    And check allow unicode box
    And check schedule sms box
    And click on send, then send now
    And click on New SMS
    And Close driver window
