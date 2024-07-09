Feature: Login in code

  Scenario: Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "ICICIAdmin" and password "Onextel@123"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button

    And go to Analytics
    And go to Error Code Summary tab
    And enter back in 'From Date' and recent in 'To Date'
    And set rows limit to 5
    And click on search
    And check pagination with limit 5

    And set rows limit to 10
    And click on search
    And check pagination with limit 10

    And Close driver window