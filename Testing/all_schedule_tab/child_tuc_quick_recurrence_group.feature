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
    And add group, all schedule
    And insert template
    And check recurrence box, all schedule
    And click on schedule, then on schedule now button
    And click on New SMS

    And Close driver window

