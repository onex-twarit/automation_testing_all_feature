Feature: Login in code

  Scenario:  Analytics Tab Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "Onexadmin" and password "Onextel@123"
    And Click on login button

    And open dashboard
    And click User Management, go to TUC
    And click on search
    And click on edit(action)

    And enter the validity(70) in tuc
    And click on update
    And click on search
    And verify the updated validity in ta

    And log out from TA
    And Enter Username "ICICIAdmin" and password "Onextel@123"
    And Click on login button

    And open dashboard
    And click on user management, go to TUC tab, tuc

    And click on add tuc button
    And fill the fields for ChildOne tuc(50)
    And click on create button

    And click on add tuc button
    And fill the fields for ChildTwo tuc(30)
    And click on create button


    And Close driver window
