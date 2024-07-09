Feature: Show button in SA

  Scenario: Show button in Carrier, Vendor, Circle, Type

    Given Launch the browser
    Then open login page
    And Enter user name and password
    And open dashboard page, go to options
    And go to carrier tab,check enable and disable show button, click on show carrier
    And go to vendor tab,check enable and disable show button, click on show vendor
    And go to circle tab,check enable and disable show button, click on show circle
    And go to type tab,check enable and disable show button, click on show type
    And close