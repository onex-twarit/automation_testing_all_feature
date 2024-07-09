Feature: Login in code

  Scenario:  Analytics Tab Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "ICICIAdmin" and password "Onextel@123"
    And Click on login button

    And open dashboard
    And in tuc, click User Management, go to TUC
    And click on search
    And in child, click on edit(action)

    And enter the validity greater than present
    And click on update
    And verify the error label 'validity exceeds'
    And click on cancel

    And Close driver window
