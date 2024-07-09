Feature: Login in code

  Scenario: Login Tenant
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "Onexadmin" and password "Onextel@123"
    And Click on login button

    And open dashboard page
    And click on Report, go to Search tab
    And enter TUC ICICIAdmin

    And enter unicode in sender ID field for search tab
    And click on search
    And verify error label 'No report data avaialable' for search tab

    And clear sender ID field for search tab
    And enter unicode in UUID field for search tab
    And click on search
    And verify error label 'No report data avaialable' for search tab

    And enter unicode in sender ID field for search tab
    And click on search
    And verify error label 'No report data avaialable' for search tab

    And Close driver window
