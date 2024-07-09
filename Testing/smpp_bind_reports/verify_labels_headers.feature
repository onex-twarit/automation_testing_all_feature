Feature: Login in code

  Scenario: Login Tenant
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "Onexadmin" and password "Onextel@123"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button

    And go to Bind Reports
    And go to SMPP Bind Report tab
    And verify date field
    And verify system/user id search field
    And verify bind status dropdown
    And verify the limit dropdown
    And verify search button

    And Close driver window

