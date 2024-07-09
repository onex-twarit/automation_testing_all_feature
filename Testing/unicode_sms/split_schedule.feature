Feature: Onextel tuc login
  Scenario: Schedule SMS

# Login to tuc – new sms – unicode sms – send sms using recipients –
# split schedule – send – verify numbers – verify credits – close.

    Given Launch the browser
    Then open login page
    And Enter user name and password
    And open dashboard page
    And go to NEW SMS then to quick unicode sms
    And add recipients, fill the present fields, schedule and split
    And verify number and credits
    And close