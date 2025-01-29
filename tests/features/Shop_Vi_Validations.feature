@ViShopAppValidations
Feature: Vi Shop Testing - This feature tests the functionality of the Vi Shop application.


@ViShopRegression @ViShopTest
Scenario Outline: VS001: Verify VI Shop App
    Given  I install vishop <application>
    Examples:
        | application |
        | vishop      |


@ViShopRegression @ViShopTest
Scenario Outline: VS002: Verify Signing in Functionality
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
Scenario Outline: VS003: Verify Account Page Navigation and Elements
    When I verify the account button is displayed
    When I click on the account button and navigate to the account page
    Then I verify all elements are displayed on the account page
    When I navigate to the FAQ page
    Then I verify all elements are displayed on the FAQ page
    When I navigate to the Credit Card (CC) page
    Then I verify all elements are displayed on the Credit Card (CC) page
    When I navigate to the Orders page
    Then I verify all elements are displayed on the Orders page
    When I navigate to the Coupons page
    Then I verify all elements are displayed on the Coupons page
    When I navigate to the T and C page
    When I navigate to the Privacy and Policy page
    When I navigate to the About US page
    When I navigate to Saved Payments page
    Then I Verify all elements are displayed on the Saved Payments page
    Examples:
        | account_button |
        | true           |

@ViShopRegression
Scenario Outline: VS004: Verify Navigation across the Tabs
    When I am on shop dashboard and verify all items are displayed on shop dashboard
    When I navigate to the deals tab
    Then I verify all items are displayed on the deals tab
    When I navigate to the explore tab
    Then I verify all items are displayed on the explore tab
    When I navigate to the my orders tab
    Then I verify all items are displayed on the my orders tab
    Examples:
        | shop_dashboard |
        | true           |

@ViShopRegression @ViShopTest
Scenario Outline: VS005: Verify Search Functionality
    When I click on search icon
#    When I enter the <invalid_input> in the search field
#    Then I verify no search results are displayed
    When I enter the <valid_input_flipkart> in the search field
    Then I click on Flipkart Search Results
#    Then I verify expected content are displayed for flipkart
#    When I enter the <valid_input_amazon> in the search field
#    Then I verify expected content are displayed for amazon
    Examples:
        | invalid_input | valid_input_flipkart  | valid_input_amazon |
        | zzz           | flipkart             | amazon             |

@ViShopRegression @ViShopTest
Scenario Outline: VS006: Verify Add to Cart Journey with Flipkart SKU from Search Results
    When I Verify the Product Title, Price, Discount and OutofStock Tag
    When I Verify the Product details
    When I Verify the buying quantity
    When I scroll to the element with text product details
    Then I Verify more details after the swipe
    When I scroll to the element with text ratings and reviews
    Then I Verify the Ratings and Review Section
    When I scroll to the element with text similar products comparison
    Then I Verify more similar products comparison section
    When I scroll to the element with text out of stock
    Then I Verify Different Denominations
    Then I Verify Add to cart and Buy Now CTA button
    Then I Click on Add To Cart CTA Button
    Then I Verify the Product details added in the cart
    Then I verify Order Summary Details
    Then I verify cart page title and pagination details
    When I click on the Proceed to Buy CTA button
    Then I verify the delivery address page
    When I click on the Proceed to Payment CTA button
    Then I verify the payment page
    Then I enter the <credit_card_number> in the credit card field

    Examples:
        | credit_card_number |
        | 4893772405842838   |
