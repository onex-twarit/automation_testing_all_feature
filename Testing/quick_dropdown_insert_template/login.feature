Feature: Login in code
    Scenario:  Analytics Tab Login
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/"
        Then Enter Username "ICICIAdmin" and password "Onextel@123"
        And Click on login button
        And Close driver window