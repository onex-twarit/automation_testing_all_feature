Feature: Login in code

  Scenario: Login SA
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "onexsa" and password "Onextel@12"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button

    And go to config
    And go to Blacklist Number tab
    And go to Upload Blacklist Number tab
    And click on download sample file button
    And verify the labels for CSV and XLSX/XLS sample
    And click on CSV sample
    And click on save file
    And click on XLSX/XLS sample
    And click on save file
    And close the sample file pop-up

    And go to Whitelist Number tab
    And go to Upload Whitelist Number tab
    And click on download sample file button
    And verify the labels for CSV and XLSX/XLS sample
    And click on CSV sample
    And click on save file
    And click on XLSX/XLS sample
    And click on save file
    And close the sample file pop-up

    And Close driver window
