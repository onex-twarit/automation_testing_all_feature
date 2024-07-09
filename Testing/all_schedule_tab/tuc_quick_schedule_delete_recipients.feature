Feature: Login in code

  Scenario:  Analytics Tab Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "ICICIAdmin" and password "Onextel@123"
    And Click on login button

    And open dashboard
    And click on new sms
    And click on quick english sms
    And select campaign name for ICICIAdmin
    And select sender ID
    And add recipients
    And insert template
    And check schedule sms box, all schedule
    And click on schedule, then on schedule now button, all schedule
    And click on New SMS

    And click on All Schedule
    And click on view all schedule
    And click on search
    And match the time of recent scheduled sms and delete

    And Close driver window