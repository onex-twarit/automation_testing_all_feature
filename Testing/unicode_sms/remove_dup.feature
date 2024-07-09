Feature: Onextel
  Scenario: Unicode SMS(remove duplicates)

# Login to tuc – new sms – unicode sms – recipients – remove duplicate
# – send – verify numbers – verify credits – close.

    Given Launch the browser
    Then open login page
    And Enter user name and password
    And open dashboard page
    And go to NEW SMS then to quick unicode sms
    And add recipients, remove duplicates, send it
    And verify number and verify credits
    And close