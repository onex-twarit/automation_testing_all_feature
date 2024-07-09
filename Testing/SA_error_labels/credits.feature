Feature: Error labels in SA

  Scenario: SA > credits
    Given Launch the browser
    Then open login page
    And Enter user name and password for SA
    And open dashboard page
    And go to Credits
    And go to All allocation tab, click on search button
    And error label 'No Credit Allocation Data Available' should come
    And close

