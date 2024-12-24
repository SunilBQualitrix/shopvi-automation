@ViShopAppValidations
Feature: Vi Shop Testing - This feature tests the functionality of the Vi Shop application.


@ViShopRegression 
Scenario Outline: SV001: Verify Tinder App Multiple Login Features
    Given  I install vishop <application>
    Examples:
        | application |
        | vishop      |


@ViShopRegression 
Scenario Outline: SV002: Verify Trouble Signing in Functionality
    Given I launch vishop Application
    Given I open the app and navigate to the mobile number input screen
    When  I close the mobile number dialog box
    When  I input a valid 10-digit mobile number <mobile_number>
    When  I click on the send OTP CTA button
    When  I input a valid 4-digit OTP <otp>
    When  I log into the app using login with OTP CTA button
    Then  I click on VI Shop from Bottom Navigation and should navigate to the shop Dashboard
    Examples:
        | mobile_number | otp  |
        | 7507233095    | 1234 |
