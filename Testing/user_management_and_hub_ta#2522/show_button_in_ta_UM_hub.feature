Feature: All TUC button

  Scenario: All TUC button in User Management(TA)

    Given Launch the browser
    Then open login page
    And Enter user name and password
    And open dashboard page, go to User Management
    And go to All TUC tab
    And click on 'show all tuc' button
    And go to hub, then go to gateway tab click on show button
    And go to SMPPC tab, click on show button
    And close