Feature: Login in code

  Scenario: Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "ICICIAdmin" and password "Onextel@123"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button

    And open dashboard
    And go to NEW SMS
    And go to dynamic sms
    And upload dynamic xls short file
    And select campaign and sender ID
    And select recipient column
    And select variable column
    And uncheck remove duplicate box
    And insert template english short
    And click on send
    And check duplicates on confirmation window
    And check valid numbers on confirmation window for short template dynamic
    And then send now
    And click on New SMS
    And verify deducted credits for short template

    And Close driver window
