 Feature: Onextel login

  Scenario: Verify record added or not

    Given Launch browser
    Then open the login page
    And Enter the user name and password
    And Dash board page
    And go to NEW SMS then to the quick english sms tuc
    And send sms using group, fill the detalsand
    And check on split schedule and send it
    And verify number then credits
    And close browser