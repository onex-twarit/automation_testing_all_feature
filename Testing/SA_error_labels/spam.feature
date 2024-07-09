Feature: Error labels in SA

  Scenario: SA > Spam
    Given Launch the browser
    Then open login page
    And Enter user name and password for SA
    And open dashboard page
    And go to Spam
    And go to spam category tab, click on show category button
    And error label 'No Data Available' should come
    And go to keywords tab, click on search button
    And error label 'Please Select a valid category' should come
    And go to spam unassign tab, click on show categories button
    And label 'No data available' should come
    And close