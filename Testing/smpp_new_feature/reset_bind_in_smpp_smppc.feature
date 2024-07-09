Feature: Login in code

  Scenario: Login
    Given launch chrome browser
    When open Onextel Homepage "http://localhost:8000/"
    Then Enter Username "Onexadmin" and password "Onextel@123"
    And Check Terms And Conditions Check Box is preselected
    And Click on login button

    And go to SMPP
    And go to SMPP tab
    And click on search SMPP
    And verify the reset bind button beside search
    And verify the reset bind button present under action in SMPP
    And click on the reset bind button
    And verify the labels or headers on the pop-up
    And click on cancel button
    And click on the reset bind button
    And click on close to close the pop-up
    And click on the reset bind button
    And click on proceed button

    And go to HUB
    And go to SMPPC tab
    And click on search SMPPC
    And verify the reset bind button beside search
    And verify the reset bind button present under action in SMPPC
    And click on the reset bind button
    And verify the labels or headers on the pop-up
    And click on cancel button
    And click on the reset bind button
    And click on close to close the pop-up
    And click on the reset bind button
    And click on proceed button

    And Close driver window
