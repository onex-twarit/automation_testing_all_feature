Feature: Error labels in SA

  Scenario: SA > Mapping Report
    Given Launch the browser
    Then open login page
    And Enter user name and password for SA
    And open dashboard page
    And go to Mapping Report, go to userwise discounting tab
    And click on search button, error label 'no data exists' should come
    And go to detailed discounting tab, click on search
    And error label 'no data exists' should come
    And close