Feature: Error labels in SA

  Scenario: SA > SMPP
    Given Launch the browser
    Then open login page
    And Enter user name and password for SA
    And open dashboard page
    And go to SMPP
    And go to SMPP tab, click on search button
    And error label 'No Record found' will come
    And close