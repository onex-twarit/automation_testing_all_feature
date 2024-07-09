Feature: Login in code

  Scenario: Login TUC
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "ICICIAdmin" and password "Onextel@123"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button

    And go to New SMS
    And click on Dynamic SMS
    And click on download sample file button
    And verify the labels for CSV and XLSX/XLS sample dynamic
    And click on CSV sample dynamic
    And click on save file in dynamic
    And click on XLSX/XLS sample dynamic
    And click on save file in dynamic
    And close the sample file pop-up dynamic

    And go to New SMS
    And click on Multiple Dynamic SMS
    And click on download sample file button
    And verify the labels for CSV and XLSX/XLS sample multiple
    And click on CSV sample multiple
    And click on save file in multiple dynamic
    And click on XLSX/XLS sample multiple
    And click on save file in multiple dynamic
    And close the sample file pop-up multiple

    And go to New SMS
    And click on Campaign SMS
    And click on download sample file button
    And verify the labels for CSV and XLSX/XLS sample campaign
    And click on CSV sample campaign
    And click on save file in campaign
    And click on XLSX/XLS sample campaign
    And click on save file in campaign
    And close the sample file pop-up campaign

    And go to DLT
    And go to Bulk Upload tab
    And click on download sample file button
    And verify the labels for CSV and XLSX/XLS sample bulk
    And click on CSV sample bulk
    And click on save file in bulk upload
    And click on XLSX/XLS sample bulk
    And click on save file in bulk upload
    And close the sample file pop-up bulk

    And go to Phonebook
    And go to Contacts tab
    And click on add contacts button
    And click on upload bulk contact button
    And click on download sample file button
    And verify the labels for CSV and XLSX/XLS sample contacts
    And click on CSV sample contacts
    And click on save file in contacts
    And click on XLSX/XLS sample contacts
    And click on save file in contacts
    And close the sample file pop-up contacts

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
