Feature: Login in TUC

  Scenario:  Delete button added in campaign tab
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "HDFCAdmin" and password "Onextel@123"
    And Click on login button
    And Close driver window
