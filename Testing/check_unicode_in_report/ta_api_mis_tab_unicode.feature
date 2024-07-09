Feature: Login in code

  Scenario: Login Tenant
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "Onexadmin" and password "Onextel@123"
    And Click on login button

    And open dashboard page
    And click on Report, go to MIS tab
    And click on total counts
    And click on API

    And enter unicode in sender ID field for api
    And click on search
    And verify error label 'No report data avaialable' for api

    And clear sender ID field for api
    And enter unicode in API Key field for api
    And click on search
    And verify error label 'No report data avaialable' for api

    And clear API Key field for api
    And enter unicode in Campaign Name field for api
    And click on search
    And verify error label 'No report data avaialable' for api

    And clear Campaign Name field for api
    And enter unicode in Template ID field for api
    And click on search
    And verify error label 'No report data avaialable' for api

    And clear Template ID field for api
    And enter unicode in sender ID field for api
    And enter unicode in API Key field for api
    And enter unicode in Campaign Name field for api
    And click on search
    And verify error label 'No report data avaialable' for api

    And clear sender ID field for api
    And enter unicode in Template ID field for api
    And click on search
    And verify error label 'No report data avaialable' for api

    And clear API Key field for api
    And enter unicode in sender ID field for api
    And click on search
    And verify error label 'No report data avaialable' for api

    And clear Campaign Name field for api
    And enter unicode in API Key field for api
    And click on search
    And verify error label 'No report data avaialable' for api

    And clear Template ID field for api
    And click on search
    And verify error label 'No report data avaialable' for api

    And clear sender ID field for api
    And enter unicode in Campaign Name field for api
    And click on search
    And verify error label 'No report data avaialable' for api

    And clear API Key field for api
    And enter unicode in Template ID field for api
    And click on search
    And verify error label 'No report data avaialable' for api

    And clear Campaign Name field for api
    And enter unicode in sender ID field for api
    And click on search
    And verify error label 'No report data avaialable' for api

    And Close driver window
