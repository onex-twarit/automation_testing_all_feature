Feature: Login in TUC

  Scenario:  Delete button added in campaign tab
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "HDFCAdmin" and password "Onextel@123"
    And Click on login button

    And open dashboard

    And go to Campaign tab
    And click on 'Show Campaign' button

    And select the campaigns to delete
    And click on 'Delete Selected' button
    And click on delete on warning window

    And verify if the campaigns are deleted

    And click on 'Delete All' button
    And click on delete on warning window

    And Close driver window
