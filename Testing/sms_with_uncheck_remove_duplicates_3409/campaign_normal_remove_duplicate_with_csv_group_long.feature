Feature: Login in code

  Scenario: Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "ICICIAdmin" and password "Onextel@123"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button

    And open dashboard
    And go to NEW SMS
    And go to campaign sms
    And upload campaign csv file
    And select campaign and sender ID
    And add group campaign
    And uncheck remove duplicate box
    And insert template english long
    And check allow multipart

    And click on send
    And check duplicates on confirmation window
    And check valid numbers on confirmation window for group long template campaign

    And then send now
    And click on New SMS

    And verify deducted credits for long template

    And Close driver window
