Feature: Login in code

  Scenario: Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "Onexadmin" and password "Onextel@123"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button

    And go to HUB
    And go to Gateway tab
    And verify Gateway, SMPPC, Routing, Default Gateway headers are present
    And verify the labels for the dropdowns(carrier, circle, gateways ID)
    And verify the button show, reset add gateway are present

    And Close driver window
