Feature: Login in code

  Scenario: Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "ICICIAdmin" and password "Onextel@123"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button

    And open dashboard
    And go to NEW SMS
    And go to multiple dynamic sms
    And upload multiple dynamic xls file with temp id
    And select campaign and sender ID
    And select recipient column
    And select template content column
    And select template ID column
    And check scrub DND

    And click on send
    And check valid numbers on confirmation window
    And check DND numbers on confirmation window
    And total required SMS credits
    And then send now

    And click on New SMS
    And verify deducted credits

    And Close driver window
