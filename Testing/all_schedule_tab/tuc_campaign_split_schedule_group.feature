Feature: Login in code

  Scenario:  Analytics Tab Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "ICICIAdmin" and password "Onextel@123"
    And Click on login button

    And open dashboard
    And click on new sms

    And click on campaign sms

    And select campaign name for ICICIAdmin
    And select sender ID
    And add group for campaign, for tuc
    And insert template

    And check schedule sms, then on split schedule box, all schedule
    And click on schedule, then on yes, schedule now button, all schedule
    And click on New SMS

    And Close driver window
