Feature: Onextel tuc login

  Scenario: Schedule SMS

    Given Launch the browser tuc
    Then open login page tuc
    And Enter user name and password tuc
    And open dashboard page tuc
    And go to NEW SMS then to quick english sms tuc
    And add two recipients
    And present fields to be filled with duplicate number
    And click on send
    And then verify for duplicate num and credits
    And then click on send now button
    And then again click on new sms button
    And close

#Login to tuc – new sms – quick sms – recipients – remove duplicate – send – verify numbers – verify credits – close.
