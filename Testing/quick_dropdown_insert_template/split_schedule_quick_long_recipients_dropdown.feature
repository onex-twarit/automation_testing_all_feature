Feature: quick recipients

  Scenario: quick recipients
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "ICICIAdmin" and password "Onextel@123"
    And Click on login button
    And open dashboard page
    And click on click on new sms, click on quick sms
    And select campaign RCF(2348)
    And select sender ID
    And add recipients
    And insert long template, select filter as dropdown
    And check allow multi part sms box
    And check split schedule box
    And click on schedule, then on yes, schedule now button
    And click on New SMS
    And Close driver window