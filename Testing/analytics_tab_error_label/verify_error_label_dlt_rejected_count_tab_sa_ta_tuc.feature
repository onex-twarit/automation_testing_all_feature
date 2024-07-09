Feature: Login in code

  Scenario: Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "onexsa" and password "Onextel@12"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button

    And go to Analytics
    And go to DLT Rejected Count tab
    And search on TUCs field with numeric input
    And click on search for dlt rejected counts
    And verify the error label, dlt rejected counts
    And search on TUCs field with alpha-numeric input
    And click on search for dlt rejected counts
    And verify the error label, dlt rejected counts
    And search on TUCs field with special-character input
    And click on search for dlt rejected counts
    And verify the error label, dlt rejected counts

    And log out from sa
    And Enter Username "Onexadmin" and password "Onextel@123"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button

    And go to Analytics
    And go to DLT Rejected Count tab
    And search on TUCs field with numeric input
    And click on search for dlt rejected counts
    And verify the error label, dlt rejected counts
    And search on TUCs field with alpha-numeric input
    And click on search for dlt rejected counts
    And verify the error label, dlt rejected counts
    And search on TUCs field with special-character input
    And click on search for dlt rejected counts
    And verify the error label, dlt rejected counts

    And log out from ta
    And Enter Username "ICICIAdmin" and password "Onextel@12"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button

    And go to Analytics
    And go to DLT Rejected Count tab
    And search on TUCs field with numeric input
    And click on search for dlt rejected counts
    And verify the error label, dlt rejected counts
    And search on TUCs field with alpha-numeric input
    And click on search for dlt rejected counts
    And verify the error label, dlt rejected counts
    And search on TUCs field with special-character input
    And click on search for dlt rejected counts
    And verify the error label, dlt rejected counts

    And Close driver window
