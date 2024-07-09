Feature: Onextel tuc login

  Scenario: Schedule SMS

    Given Launch browser
    Then open the login page
    And Enter the user name and password
    And open the dashboard page
    And go to NEW SMS then to the quick english sms tuc
    And add two recipients and check on remove duplicate
    And present fields to be filled with check on scrub dnd
    And click on the send
    And then verify for the duplicate num and the credits
    And then click on the send now button
    And then again click on the new sms button
    And close browser