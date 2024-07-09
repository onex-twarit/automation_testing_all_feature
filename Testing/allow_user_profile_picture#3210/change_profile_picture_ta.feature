Feature: Login in code

  Scenario: Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "onexsa" and password "Onextel@123"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button

    And go to User Management
    And go to Tenants tab, click on show Tenants
    And click on edit of Onexadmin
    And check allow user profile picture
    And click on update

    And log out sa
    Then Enter Username "Onexadmin" and password "Onextel@123"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button
    And go to profile section
    And go to My Account
    And upload logo
    And upload icon
    And upload login page logo






    And Close driver window
