Feature: Onextel

  Scenario: Unicode SMS using group

#Login to tuc – new sms – unicode sms – send sms using group
#– split schedule – send – verify numbers – verify credits – close.

    Given Launch the browser
    Then open login page
    And Enter user name and password
    And open dashboard page
    And go to NEW SMS then to quick unicode sms
    And using group, split schedule, send it,
    And verify num and credit
    And close

