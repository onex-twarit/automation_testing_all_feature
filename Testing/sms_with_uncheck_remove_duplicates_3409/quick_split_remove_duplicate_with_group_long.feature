Feature: Login in code

  Scenario: Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "ICICIAdmin" and password "Onextel@123"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button

    And open dashboard
    And go to NEW SMS
    And go to quick sms
    And select campaign and sender ID
    And add group
    And uncheck remove duplicate box
    And insert template english long
    And check allow multipart
    And check split sms
    And click on schedule
    And then on click on Yes

    And check duplicates on split confirmation window

    And then schedule now for split
    And click on New SMS

    And verify deducted credits for long template split

    And Close driver window
