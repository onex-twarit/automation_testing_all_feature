Feature: Login in code

  Scenario:  Analytics Tab Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "ICICIAdmin" and password "Onextel@123"
    And Click on login button
    And open dashboard

    And click User Management, go to TUC
#    And click on add tuc button
#    And fill the fields for ChildOne tuc
#    And click on create tuc button

    And go to User
#    And click on add user button
#    And fill the fields for ChildOne user
#    And click on create user button

    And log out from parent tuc
    And Enter Username "ChildOne" and password "password"
    And Click on login button
    And reset password and click on submit

    And child tuc, click on new SMS, quick sms


    And Close driver window
