Feature: Login in code

  Scenario: Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "ICICIAdmin" and password "Onextel@123"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button

    And go to Analytics
    And go to Error Code Summary tab
    And click on search
    And verify the data is present

    And go to Error Code Summary tab
    And enter correct TUC name
    And click on search
    And verify the data is present

    And go to Error Code Summary tab
    And enter incorrect TUC name with alpha-numeric input
    And click on search
    And verify the error label for incorrect tuc

    And go to Error Code Summary tab
    And enter incorrect TUC name with special-character input
    And click on search
    And verify the error label for incorrect tuc

    And go to Error Code Summary tab
    And enter the error code '765'
    And click on search
    And verify if the data is present for code '765'

    And go to Error Code Summary tab
    And enter the error code '654'
    And click on search
    And verify if the data is present for code '654'

    And Close driver window
