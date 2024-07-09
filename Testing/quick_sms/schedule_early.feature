#Login to tuc – new sms – quick sms – recipients and group –
#schedule within 15 mins and verify labels – close.
Feature: Onextel

  Scenario: Quick SMS schedule within 15 mins

    Given Launch the browser
    Then open login page
    And Enter user name and password for tuc
    And open dashboard page tuc
    And go to new sms then to quick sms
    And add recipients and group, schedule early
    And on new window verify labels
    And close the browser
