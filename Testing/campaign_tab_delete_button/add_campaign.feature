Feature: Login in TUC

  Scenario:  Delete button added in campaign tab
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "HDFCAdmin" and password "Onextel@123"
    And Click on login button

    And open dashboard
    And go to Campaign tab
    And click on 'Add Campaign' button

    And enter quick campaign name
    And enter description
    And click on add button

    And click on 'Add Campaign' button
    And enter new quick campaign name
    And enter description
    And click on add button

    And click on 'Add Campaign' button
    And enter unicode campaign name
    And enter description
    And click on add button

    And click on 'Add Campaign' button
    And enter new unicode campaign name
    And enter description
    And click on add button

    And click on 'Add Campaign' button
    And enter dynamic campaign name
    And enter description
    And click on add button

    And click on 'Add Campaign' button
    And enter multiple dynamic campaign name
    And enter description
    And click on add button

    And click on 'Add Campaign' button
    And enter campaign name
    And enter description
    And click on add button

    And click on 'Show Campaign' button

    And Close driver window
