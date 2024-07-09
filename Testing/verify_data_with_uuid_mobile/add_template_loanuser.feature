Feature: Login in code

  Scenario:  Analytics Tab Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "loanuser" and password "Onextel@123"
    And Click on login button

    And open dashboard
    And click DLT
    And go to entity ID tab, click on add entity ID
    And go to sender ID tab, click on add sender ID(uncheck default)
    And go to template tab, click on add template
    And english, fill all the fields, then click on add

    And Close driver window
