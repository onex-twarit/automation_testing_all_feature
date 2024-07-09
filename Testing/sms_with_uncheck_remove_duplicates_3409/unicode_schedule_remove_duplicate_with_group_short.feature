Feature: Login in code

Feature: Login in code

  Scenario: Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "ICICIAdmin" and password "Onextel@123"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button

    And open dashboard
    And go to NEW SMS
    And go to unicode sms
    And select campaign and sender ID
    And add group
    And uncheck remove duplicate box
    And insert template hindi short
    And check allow multipart
    And check allow unicode

    And check schedule sms
    And click on schedule

    And check duplicates on confirmation window
    And check valid numbers on confirmation window for short template group

    And then schedule now
    And click on New SMS

    And verify deducted credits for short template

    And Close driver window
