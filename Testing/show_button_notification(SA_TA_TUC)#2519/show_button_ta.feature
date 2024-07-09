Feature: Show button in Notification(TA)

  Scenario: TA > Notification

    Given Launch the browser
    Then open login page
    And Enter user name and password ta
    And open dashboard page ta
    And go to notification
    And click on show notification button
    And check the notifications in the panel
    And close the browser
