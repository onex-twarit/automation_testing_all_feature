Feature: Login in code

  Scenario: Login Tenant
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "Onexadmin" and password "Onextel@123"
    And Click on login button

    And open dashboard page
    And click on Report, go to MIS tab
    And click on total counts
    And click on SMPP

    And enter unicode in sender ID field for smpp
    And click on search
    And verify error label 'No report data avaialable' for smpp

    And clear sender ID field for smpp
    And enter unicode in SMPP ID field for smpp
    And click on search
    And verify error label 'No report data avaialable' for smpp

    And clear SMPP ID field for smpp
    And enter unicode in Template ID field for smpp
    And click on search
    And verify error label 'No report data avaialable' for smpp

    And clear Template ID field for smpp
    And enter unicode in sender ID field for smpp
    And enter unicode in SMPP ID field for smpp
    And click on search
    And verify error label 'No report data avaialable' for smpp

    And clear sender ID field for smpp
    And enter unicode in Template ID field for smpp
    And click on search
    And verify error label 'No report data avaialable' for smpp

    And clear SMPP ID field for smpp
    And enter unicode in sender ID field for smpp
    And click on search
    And verify error label 'No report data avaialable' for smpp

    And enter unicode in SMPP ID field for smpp
    And click on search
    And verify error label 'No report data avaialable' for smpp

    And Close driver window
