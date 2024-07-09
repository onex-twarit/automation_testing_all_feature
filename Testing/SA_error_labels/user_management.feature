Feature: Error labels in SA

  Scenario: SA > User Management

    Given Launch the browser
    Then open login page
    And Enter user name and password for SA
    And open dashboard page
    And go to User Management
    And go to user tab, click on search button
    And error label 'No Record found' should come
    And search tab, click on search button
    And error label 'Please enter Sender ID' should come
    And close

