Feature: Login in TUC

  Scenario:  Delete button added in campaign tab
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "HDFCAdmin" and password "Onextel@123"
    And Click on login button

    And open dashboard
    And go to Campaign tab
    And verify campaign tab is opened
    And verify 'delete selected' and 'delete all' buttons are present

    And Close driver window
