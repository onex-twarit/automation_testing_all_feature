Feature: Onextel tuc login

  Scenario: Schedule Early SMS

    Given Launching browser
    Then login page
    And user name and password
    And dashboard page
    And go to NEW SMS after it go to quick english sms tuc
    And add recipients and select template
    And check on schedule sms (within 15 min)
    And click send
    And verify for the error label on new window
    And click on OK button
    And browser closed