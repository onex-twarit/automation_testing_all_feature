Feature: Onextel

  Scenario: Unicode SMS using recipients and check if record added or not

#Login to tuc – new sms – unicode sms – send sms using recipients – split schedule – send –
#verify numbers – verify credits – click on view schedule – verify record is added or not – close.

    Given Launch the browser
    Then open login page
    And Enter user name and password
    And open dashboard page
    And go to NEW SMS then to quick unicode sms
    And add recipients, split schedule, send it, verify num and credit
    And on view schedule check added record
    And close
