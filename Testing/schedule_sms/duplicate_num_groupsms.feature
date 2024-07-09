Feature: Onextel tuc login

  Scenario: Schedule SMS

#Login to tuc – new sms – quick sms – group – remove duplicate –
#send – verify numbers – verify credits – close.

    Given Launch the browser tuc
    Then open login page tuc
    And Enter user name and password tuc
    And open dashboard page tuc
    And go to NEW SMS then to quick english sms tuc
    And add group, remove duplicate and fill the present fields
    And send it, verify number and credits
    And close browser