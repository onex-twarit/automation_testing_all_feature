Feature: Onextel tuc login
  Scenario: Schedule Early SMS

# Login to tuc – new sms – quick sms – group –
# schedule within 15 mins and verify labels – close.

    Given Launch browser
    Then open login page
    And user name and password
    And dashboard page
    And go to NEW SMS after it go to quick english sms tuc
    And select group
    And check on schedule sms within 15 min
    And click send
    And verify for the error label on new window
    And click on OK button
    And browser closed