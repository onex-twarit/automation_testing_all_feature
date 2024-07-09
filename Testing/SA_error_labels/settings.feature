Feature: Error labels in SA

  Scenario: SA > Setting
    Given Launch the browser
    Then open login page
    And Enter user name and password for SA
    And open dashboard page
    And go to Settings, go to discounting mapping tab
    And click on show users button, error label 'no data exists' should come
    And go to retry mapping tab, click on show retry gateways button
    And error label 'no gateway data available' should come
    And click on show retry users button, label 'No data available' should come
    And go to backup gateway tab, label 'not able to get data' should come
    And close