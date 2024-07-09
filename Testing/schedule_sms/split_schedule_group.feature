Feature: Onextel login

  Scenario: Verify record added or not

#Login to tuc – new sms – quick sms – group – split schedule – send –
#verify numbers – verify credits – click on view schedule – verify record is added or not – close.

    Given Launch browser
    Then open the login page
    And Enter the user name and password
    And Dash board page
    And go to NEW SMS then to the quick english sms tuc
    And send sms using group, fill the details and
    And check split schedule and send it
    And verify num then credits
    And go to view schedule and verify (record added)
    And close browser


