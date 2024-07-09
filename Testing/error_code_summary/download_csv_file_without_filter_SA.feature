Feature: Login in code

  Scenario: Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "onexsa" and password "Onextel@123"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button

    And go to Analytics
    And go to Error Code Summary tab
    And click on search
    And click on download button
    And click on download CSV
    And verify the label on the pop up 'Your Download Request Received!'
    And click on OK

    And go to Report
    And go to Download Data tab SA
    And click on download

    And Close driver window