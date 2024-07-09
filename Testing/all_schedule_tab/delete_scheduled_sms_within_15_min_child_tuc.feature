Feature: Login in code

  Scenario:  Analytics Tab Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "ChildOne" and password "Onextel@123"
    And Click on login button

    And open dashboard

    And click on new sms
    And click on quick english sms
    And select campaign name for ChildOne
    And select sender ID
    And add recipients
    And insert template
    And check schedule sms box, all schedule
    And click on schedule, then on schedule now button, all schedule
    And click on New SMS

    And click on All Schedule
    And click on view all schedule
    And click on delete button on the scheduled sms
    And click within 15 min and verify the error label

    And log out from child TUC

    And Enter Username "Onexadmin" and password "Onextel@123"
    And Click on login button

    And open dashboard

    And click on All Schedule
    And click on view all schedule
    And click on search (with records)
    And match the time of the scheduled sms
    And delete the entry from the TA

    And Close driver window
