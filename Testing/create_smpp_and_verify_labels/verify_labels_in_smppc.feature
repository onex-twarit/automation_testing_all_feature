Feature: Login in code

  Scenario: Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "Onexadmin" and password "Onextel@12"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button

    And go to HUB
    And go to SMPPC tab
    And click on search SMPPC
    And verify the headers and labels

    And Close driver window
