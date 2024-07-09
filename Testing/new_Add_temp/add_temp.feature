Feature: Login in code

  Scenario:  Analytics Tab Login
    Given launch chrome browser
    When open Onextel Homepage "http://115.117.115.60:8000/"
    Then Enter Username "Testing5" and password "Onextel@123"
    And Click on login button

#    And open dashboard
    And click DLT
    And go to entity ID tab, click on add entitity ID
    And go to sender ID tab, click on add sender ID(uncheck default)
    And go to template tab, click on add template
    And english, fill all the fields, then click on add
#    And hindi, fill all the fields, then click on add

    And Close driver window
