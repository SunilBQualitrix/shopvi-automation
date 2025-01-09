@ViShopAppValidations
Feature: Vi Shop Testing - This feature tests the functionality of the Vi Shop application.


@ViShopRegression 
Scenario Outline: SV001: Verify VI Shop App
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


@ViShopRegression 
Scenario Outline: SV003: Verify Search Functionality
    Given I launch vishop Application
    When  I open the shop tab and verify search icon is displayed in shop page
    Then  I open the deals tab and verify search icon is not displayed in deals page
    Then  I open the explore tab and verify search icon is displayed in explore page
    Then  I open the my orders tab and verify search icon is displayed in my orders page
    When  I click on search icon
    When  I enter the <invalid_input> in the search field
    Then  I verify no search results are displayed
    When  I enter the <valid_input_flipkart> in the search field
    Then  I verify expected content are displayed for flipkart
    When  I enter the <valid_input_amazon> in the search field
    Then  I verify expected content are displayed for amazon
    Examples:
        | invalid_input | valid_input_flipkart  | valid_input_amazon |
        | zzz           | flipkart              | amazon             |