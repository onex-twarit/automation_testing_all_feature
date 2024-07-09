Feature: Onextel

  Scenario: Unicode SMS using group remove duplicates

# Login to tuc – new sms – unicode sms – group – remove duplicate
# – send – verify numbers – verify credits – close.

    Given Launch the browser
    Then open login page
    And Enter user name and password
    And open dashboard page
    And go to NEW SMS then to quick unicode sms
    And add recipients, group, and remove duplicate
    And verify duplicate num, then credits
    And close
