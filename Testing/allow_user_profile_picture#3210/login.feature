Feature: Login in code

  Scenario: Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "onexsa" and password "Onextel@123"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button
    And Close driver window
