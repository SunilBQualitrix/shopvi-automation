@ViShopAppValidations
Feature: Vi Shop Testing - This feature tests the functionality of the Vi Shop application.

# ======== NOTE: Login steps are now pre-configured on the device ========
# @ViShopRegression @ViShopTest
# Scenario Outline: VS001: Login to Vi Shop Application
#     Given  I install vishop <application>
#     Given I launch vishop Application
#     Given I open the app and navigate to the mobile number input screen
#     When  I close the mobile number dialog box
#     When  I input a valid 10-digit mobile number <mobile_number>
#     When  I click on the send OTP CTA button
#     When  I input a valid 4-digit OTP <otp>
#     When  I log into the app using login with OTP CTA button
#     
#     Examples:
#         | mobile_number | otp  |    | application |
#         | 7507233095    | 1234 |    | vishop      |

@ViShopRegression @ViShopTest
Scenario Outline: VS002: Account Page Validations
    When I click on VI Shop from Bottom Navigation and should navigate to the shop Dashboard
    When I verify the account button is displayed
    When I click on the account button and navigate to the account page
    Then I verify all elements are displayed on the account page
    When I navigate to the FAQ page
    Then I verify all elements are displayed on the FAQ page
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
Scenario Outline: VS003: Vi Shop Navigation and Validations
    When I am on shop dashboard and verify Quick Purchase Section
    When I am on shop dashboard and verify all items are displayed on shop dashboard
    When I navigate to the deals tab
    Then I verify all items are displayed on the deals tab
    When I navigate to the categories tab
    Then I verify all items are displayed on the categories tab
    When I navigate to the Travel Sub-category under Categories tab
    Then I verify all items that are displayed under Travel Sub-category
    When I navigate to the CABS inside Travel Sub-category under Categories tab
    Then I verify all items that are displayed under CABS inside Travel Sub-category
    When I navigate to the Hotels inside Travel Sub-category under Categories tab
    Then I verify all items that are displayed under Hotels inside Travel Sub-category
    When I navigate to the Flights inside Travel Sub-category under Categories tab
    Then I verify all items that are displayed under Flights inside Travel Sub-category
    When I navigate to the Experinces inside Travel Sub-category under Categories tab
    Then I verify all items that are displayed under Experinces inside Travel Sub-category
    When I navigate to Movies Subcategory under Categories tab
    Then I verify all items that are displayed under Movies Subcategory
    When I navigate to Movies subcategory under Movies
    Then I verify all items that are displayed under Movies subcategory
    When I navigate to OTT Subcategory under Movies
    Then I verify all items that are displayed under OTT Subcategory
    When I navigate to Shopping Subcategory
    Then I verify all items that are displayed under Shopping Subcategory
    When I navigate to Amazon Egift card subcategory under Shopping
    Then I verify all items that are displayed under Amazon Egift card subcategory
    When I navigate to Amazon Shopping voucher subcategory under Shopping
    Then I verify all items that are displayed under Amazon Shopping voucher subcategory
    When I navigate to Fashion and accessories subcategory under Shopping
    Then I verify all items that are displayed under Fashion and accessories subcategory
    When I navigate to Flipkart subcategory under Shopping
    Then I verify all items that are displayed under Flipkart subcategory
    When I navigate to the my orders tab
    Then I verify all items are displayed on the my orders tab

    Examples:
        | shop_dashboard |
        | true           |

@ViShopRegression
Scenario Outline: VS004: Add to Cart Journey with Amazon SKU from Search Results
    When I click on search icon
    When I enter the <valid_input> in the search field
    Then I click on Search Results
    When I Verify the Product Title, Price, Discount and OutofStock Tag
    When I Verify the Product details
    When I Verify the buying quantity
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
    Then I verify Convenience Fee Details
    Then I Navigate back to HomePage

    Examples:
        | valid_input | | credit_card_number |
        | amazon      | | 4893772405842838   |


@ViShopRegression
Scenario Outline: VS005: Buy Now Journey with Nykaa SKU from Search Results
    When I click on search icon
    When I enter the <valid_input> in the search field
    Then I click on Search Results
    When I Verify the Product Title, Price, Discount and OutofStock Tag
    When I Verify the Product details
    When I Verify the buying quantity
    When I Verify Buy Now CTA button
    Then I Click on the Buy Now CTA button
    When I Verify Proceed to Pay CTA button is displayed on the Buy Now popup
    Then I Click the Buy Now Proceed to Pay CTA button which is displayed on the Buy Now popup
    Then I Verify the Product details added in the cart
    Then I verify Order Summary Details
    Then I verify cart page title and pagination details
    When I click on the Proceed to Buy CTA button
    Then I verify the delivery address page
    When I click on the Proceed to Payment CTA button
    Then I verify the payment page
    Then I enter the <credit_card_number> in the credit card field
    Then I verify Convenience Fee Details
    Then I Navigate back to HomePage

    Examples:
        | valid_input | | credit_card_number |
        | Nykaa      |  | 4893772405842838   |