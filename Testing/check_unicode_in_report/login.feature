Feature: Login in code
    Scenario: Login Tenant
        Given launch chrome browser
        When open Onextel Homepage "http://localhost:8000/"
        Then Enter Username "Onexadmin" and password "Onextel@123"
        And Click on login button
        And Close driver window
