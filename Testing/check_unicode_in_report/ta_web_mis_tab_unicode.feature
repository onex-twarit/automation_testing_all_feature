Feature: Login in code

  Scenario: Login Tenant
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "Onexadmin" and password "Onextel@123"
    And Click on login button
    And open dashboard page
    And click on Report, go to MIS tab
    And click on total counts
    And click on Web

    And enter unicode in sender ID field
    And click on search
    And verify error label 'No report data avaialable'

    And clear sender ID field
    And enter unicode in Campaign Name field
    And click on search
    And verify error label 'No report data avaialable'

    And clear Campaign Name field
    And enter unicode in Template ID field
    And click on search
    And verify error label 'No report data avaialable'

    And clear Template ID field
    And enter unicode in sender ID field
    And enter unicode in Campaign Name field
    And click on search
    And verify error label 'No report data avaialable'

    And clear sender ID field
    And enter unicode in Template ID field
    And click on search
    And verify error label 'No report data avaialable'

    And clear Campaign Name field
    And enter unicode in sender ID field
    And click on search
    And verify error label 'No report data avaialable'

    And enter unicode in Campaign Name field
    And click on search
    And verify error label 'No report data avaialable'

    And Close driver window
