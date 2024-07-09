Feature: Login in code

  Scenario: Login TUC
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "ICICIAdmin" and password "Onextel@123"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button

    And go to New SMS
    And go to Quick English SMS
    And add campaign for schedule SMS
    And select sender ID
    And add recipients and select group
    And insert template

    And check schedule sms box
    And click on send, then send now
    And click on New SMS

    And go to Quick English SMS
    And go to View Schedule tab
    And verify the schedule sms

    And go to reports
    And then on scheduled campaigns tab, select TUC
    And click on search
    And verify the quick schedule SMS
    And go to reports
    And go to MIS tab, click on total counts
    And click on search
    And find the quick schedule campaign name and verify


    And Close driver window
