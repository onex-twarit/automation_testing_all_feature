Feature: Error labels in SA

  Scenario: SA > Master Credits
    Given Launch the browser
    Then open login page
    And Enter user name and password for SA
    And open dashboard page
    And go to Master Credits
    And go to master credits tab, click on show credits button
    And master credits should be '0'
    And go to super admin history tab, click on search button
    And 'No data available' error label should come
    And close

