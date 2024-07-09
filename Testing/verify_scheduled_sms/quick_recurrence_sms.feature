Feature: Login in code

  Scenario: Login TUC
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "ICICIAdmin" and password "Onextel@123"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button

    And go to New SMS
    And go to Quick English SMS
    And add campaign for recurrence SMS
    And select sender ID
    And add recipients and select group
    And insert template

    And check recurrence
    And click on schedule, then on schedule now button
    And click on New SMS

    And go to Quick English SMS
    And go to View Schedule tab
    And verify the recurrence sms

    And go to reports
    And then on scheduled campaigns tab, select TUC
    And click on search
    And verify the quick recurrence SMS
    And go to reports
    And go to MIS tab, click on total counts
    And click on search
    And find the quick recurrence campaign name and verify


    And Close driver window








