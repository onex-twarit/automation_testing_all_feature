Feature: Error labels in SA

  Scenario: SA > Routing
    Given Launch the browser
    Then open login page
    And Enter user name and password for SA
    And open dashboard page
    And go to Options, go to carrier tab
    And click on show carrier button, error label 'no data exist' should come
    And go to vendor tab,
    And click on show vendor button, error label 'no data exist' should come
    And go to circle tab,
    And click on show circle button, error label 'no data exist' should come
    And go to type tab,
    And click on show type button, error label 'no data exist' should come
    And close