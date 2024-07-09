Feature: Show button in Notification(SA)

  Scenario: SA > Notification

    Given Launch the browser
    Then open login page
    And Enter user name and password
    And open dashboard page SA
    And go to notification
    And click on show notification button
    And check the notifications in the panel
    And close the browser
