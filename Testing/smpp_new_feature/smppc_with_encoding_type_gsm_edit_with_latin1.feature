Feature: Login in code

  Scenario: Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "Onexadmin" and password "Onextel@123"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button

    And go to HUB
    And go to SMPPC tab
    And click on Add SMPPC
    And fill the details to create SMPPC with GSM-7 encoding type
    And add the SMPPC
    And click on search SMPPC
    And click on edit SMPPC for GSM-7 encoding type
    And verify the SMPPC GSM-7 encoding type
    And click on cancel
    And click on search SMPPC
    And click on edit SMPPC for GSM-7 encoding type
    And SMPPC encoding type GSM-7 to LATIN-1
    And click on update SMPPC
    And click on search SMPPC
    And click on edit SMPPC for GSM-7 encoding type
    And verify the updated SMPPC LATIN-1 encoding type

    And Close driver window
