Feature: Onextel

  Scenario: Unicode SMS using recipients and schedule for early

# Login to tuc – new sms – unicode sms – recipients –
# schedule within 15 mins and verify labels – close.

    Given Launch the browser
    Then open login page
    And Enter user name and password
    And open dashboard page
    And go to NEW SMS then to quick unicode sms
    And add recipients. schedule within 15 mins and send it
    And verify labels
    And close
