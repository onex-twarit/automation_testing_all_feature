Feature: Error labels in SA

  Scenario: SA > Routing
    Given Launch the browser
    Then open login page
    And Enter user name and password for SA
    And open dashboard page
    And go to Routing, go to view rule tab
    And click on search, 'record not found' label should come
    And close