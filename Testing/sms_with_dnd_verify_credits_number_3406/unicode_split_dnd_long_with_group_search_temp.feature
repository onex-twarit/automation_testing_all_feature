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
    And insert template hindi long with search type
    And check allow multipart
    And check allow unicode
    And check scrub DND

    And check split sms

    And click on schedule
    And then on click on Yes
    And check DND numbers on split confirmation window
    And total required SMS credits on split confirmation window

    And then schedule now
    And click on New SMS
    And verify deducted credits split

    And Close driver window
