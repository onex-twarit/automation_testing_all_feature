Feature: Login in code

  Scenario:  Analytics Tab Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "sales" and password "Onextel@123"
    And Click on login button

    And open dashboard

    And go to reports

    And go to search tab select loanuser TUC
    And select filter as mobile, send invalid data(loanuser)
    And click on search
    And verify invalid data
    And select filter as sender ID with mobile, send invalid data(loanuser)
    And click on search
    And verify invalid data

    And Close driver window