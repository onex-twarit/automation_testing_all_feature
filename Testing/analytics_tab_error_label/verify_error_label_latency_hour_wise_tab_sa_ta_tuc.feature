Feature: Login in code

  Scenario: Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "onexsa" and password "Onextel@12"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button

    And go to Analytics
    And go to Latency Hour-Wise Report tab
    And search on TUCs field with numeric input, latency hour
    And click on search, latency hour
    And verify the error label, latency hour
    And search on TUCs field with alpha-numeric input, latency hour
    And click on search, latency hour
    And verify the error label, latency hour
    And search on TUCs field with special-character input, latency hour
    And click on search, latency hour
    And verify the error label, latency hour

    And log out from sa
    And Enter Username "Onexadmin" and password "Onextel@123"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button

    And go to Analytics
    And go to Latency Hour-Wise Report tab
    And search on TUCs field with numeric input, latency hour
    And click on search, latency hour
    And verify the error label, latency hour
    And search on TUCs field with alpha-numeric input, latency hour
    And click on search, latency hour
    And verify the error label, latency hour
    And search on TUCs field with special-character input, latency hour
    And click on search, latency hour
    And verify the error label, latency hour

    And log out from ta
    And Enter Username "ICICIAdmin" and password "Onextel@12"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button

    And go to Analytics
    And go to Latency Hour-Wise Report tab
    And search on TUCs field with numeric input, latency hour
    And click on search, latency hour
    And verify the error label, latency hour
    And search on TUCs field with alpha-numeric input, latency hour
    And click on search, latency hour
    And verify the error label, latency hour
    And search on TUCs field with special-character input, latency hour
    And click on search, latency hour
    And verify the error label, latency hour

    And Close driver window
