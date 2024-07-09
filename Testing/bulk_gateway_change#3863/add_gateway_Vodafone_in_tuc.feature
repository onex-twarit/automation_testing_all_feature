Feature: Login in code

  Scenario: Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "Onexadmin" and password "Onextel@123"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button

    And go to User Management
    And go to TUC tab
    And click on search TUC
    And click on ICICIAdmin TUC edit
    And change all the gateways type to Vodafone
    And click on update

    And Close driver window