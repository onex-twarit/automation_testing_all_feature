Feature: Show button in Notification(TUC)

  Scenario: TUC > Notification

    Given Launch the browser
    Then open login page
    And Enter user name and password tuc
    And open dashboard page tuc
    And go to notification
    And click on show notification button
    And check the notifications in the panel
    And close the browser
