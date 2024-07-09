Feature: Login in code

  Scenario:  Analytics Tab Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "SBIUser" and password "Onextel@123"
    And Click on login button

    And open dashboard
    And click on new sms

    And click on campaign sms
    And upload campaign file

    And select campaign name
    And select sender ID
    And insert template

    And check schedule sms, then on split schedule box
    And click on schedule, then on yes, schedule now button

    And click on New SMS

    And log out TUC
    And Enter Username "Onexadmin" and password "Onextel@123"
    And Click on login button
    And open dashboard
    And click on user management
    And go to TUC tab
    And click on search
    And disable the TUC and check it should not going to be disabled
    And verify the error label in the new pop-up window
    And click on OK on warning pop-up

    And Close driver window
