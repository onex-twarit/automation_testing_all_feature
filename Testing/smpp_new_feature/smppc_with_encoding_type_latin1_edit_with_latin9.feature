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
    And fill the details to create SMPPC with LATIN-1 encoding type
    And add the SMPPC
    And click on search SMPPC
    And click on edit SMPPC for LATIN-1 encoding type
    And verify the SMPPC LATIN-1 encoding type
    And click on cancel
    And click on search SMPPC
    And click on edit SMPPC for LATIN-1 encoding type
    And SMPPC encoding type LATIN-1 to LATIN-9
    And click on update SMPPC
    And click on search SMPPC
    And click on edit SMPPC for Latin-1 encoding type
    And verify the updated SMPPC LATIN-9 encoding type

    And Close driver window
