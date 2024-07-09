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
    And fill the details to create SMPP with GSM-7 encoding type
    And add the SMPP
    And click on search SMPP
    And click on edit SMPP for GSM-7 encoding type
    And verify the GSM-7 encoding type
    And click on cancel
    And click on search SMPP
    And click on edit SMPP for GSM-7 encoding type
    And encoding type GSM-7 to LATIN-1
    And click on update SMPP
    And click on search SMPP
    And click on edit SMPP for GSM-7 encoding type
    And verify the updated LATIN-1 encoding type

    And Close driver window
