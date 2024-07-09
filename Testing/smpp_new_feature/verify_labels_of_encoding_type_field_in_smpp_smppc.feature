Feature: Login in code

  Scenario: Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "Onexadmin" and password "Onextel@123"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button

    And go to SMPP
    And go to SMPP tab
    And click on Add SMPP
    And verify the labels of encoding type field

    And go to HUB
    And go to SMPPC tab
    And click on Add SMPPC
    And verify the labels of encoding type field