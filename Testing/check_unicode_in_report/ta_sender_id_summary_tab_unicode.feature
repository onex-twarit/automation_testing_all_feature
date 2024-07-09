Feature: Login in code

  Scenario: Login Tenant
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "Onexadmin" and password "Onextel@123"
    And Click on login button

    And open dashboard page
    And click on Report, go to Sender ID summary tab
    And enter TUC ICICIAdmin

    And enter unicode in sender ID field for sender id summary tab
    And click on search
    And verify error label 'No report data avaialable' for sender id summary tab

    And Close driver window