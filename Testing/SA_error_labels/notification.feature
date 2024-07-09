Feature: Error labels in SA

  Scenario: SA > Notification
    Given Launch the browser
    Then open login page
    And Enter user name and password for SA
    And open dashboard page
    And go to Notification, click on show notification button
    And label 'No Record Found' should come
    And close