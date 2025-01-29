import time
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from utils.custom_logger import custom_logger, allureLogs
from pages.actions.android_actions import AndroidActions
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



locators_pdpf = {

    "PRODUCT_TITLE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("flipkart shopping voucher")'),
    "OUT_OF_STOCK": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("out of stock")'),
    "PRODUCT_PRICE": (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "₹")]'),
    "PRODUCT_DISCOUNT": (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "% off")]'),

    #Denominations
    "DENOMINATION_W/OFFER1": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("₹980").instance(1)'),
    "DENOMINATION_WO/OFFER1": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("₹1000").instance(1)'),
    "DENOMINATION_W/OFFER2": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("₹4900.0")'),
    "DENOMINATION_WO/OFFER2": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("₹5000.0")'),
    "DENOMINATION_W/OFFER3": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("₹9800.0")'),
    "DENOMINATION_WO/OFFER3": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("₹10000.0")'),
    "DENOMINATION_W/OFFER4": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("₹490.0")'),
    "DENOMINATION_WO/OFFER4": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("₹500.0")'),
    "DENOMINATION_W/OFFER5": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("₹2450.0")'),
    "DENOMINATION_WO/OFFER5": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("₹2500.0")'),

    "BUYING": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("buying:")'),
    "FOR_MYSELF": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("for myself")'),
    "FOR_MYSELF_RADIO_BUTTON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(4)'),
    "AS_A_GIFT": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("as a gift")'),
    "AS_A_GIFT_RADIO_BUTTON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(5)'),
    "QUANTITY": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("quantity:")'),
    "QUANTITY_COUNT": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("1")'),
    "INCREASE_QUANTITY": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(7)'),
    "DECREASE_QUANTITY": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(6)'),

    "ABOUT_PRODUCT": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("about product")'),
    "ABOUT_PRODUCT_EXPAND_COLLAPSE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(8)'),
    "ABOUT_PRODUCT_DESCRIPTION": (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "Flipkart is your one-stop online shopping destination")]'),

    "PRODUCT_DETAILS": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("product details")'),
    "PRODUCT_DETAILS_EXPAND_COLLAPSE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(9)'),
    "PRODUCT_DETAILS_DESCRIPTION": (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="p"])[1]/android.widget.TextView'),

    "STEPS_TO_REDEEM": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("steps to redeem")'),
    "STEPS_TO_REDEEM_EXPAND_COLLAPSE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(10)'),
    "STEPS_TO_REDEEM_DESCRIPTION": (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView'),

    "TERMS_AND_CONDITIONS": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("terms and conditions")'),
    "TERMS_AND_CONDITIONS_EXPAND_COLLAPSE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(11)'),
    "TERMS_AND_CONDITIONS_DESCRIPTION": (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="p"]/android.widget.TextView'),


    #Details
    "PRODUCT_DETAILS1": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("occasion:  ")'),
    "PRODUCT_DETAILS2": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("shopping")'),
    "PRODUCT_DETAILS3": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("denomination: ")'),
    "PRODUCT_DETAILS4": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Rs. 1000")'),
    "PRODUCT_DETAILS5": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("brand: ")'),
    "PRODUCT_DETAILS6": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Flipkart").instance(1)'),
    "PRODUCT_DETAILS7": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("type: ")'),
    "PRODUCT_DETAILS8": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("giftcard")'),
    "PRODUCT_DETAILS9": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("validity: ")'),
    "PRODUCT_DETAILS10": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("12 months")'),
    "PRODUCT_DETAILS11": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("place of redemption: ")'),
    "PRODUCT_DETAILS12": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("flipkart.com")'),
    "COLLAPSE_EXPAND_ARROW": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(5)'),

    "MORE_FROM_THIS_SELLER": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("more from this seller")'),



    "RATINGS_REVIEWS_TITLE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ratings and reviews")'),
    "WRITE_A_REVIEW_CTA": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("write a review")'),
    "VIEW_ALL_REVIEWS_TEXT": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("View all reviews")'),
    "VIEW_ALL_REVIEWS_CTA": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(16)'),
    "NO_OF_RATINGS": (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "ratings")]'),
    "NO_OF_REVIEWS": (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "reviews")]'),
    "AVG_RATING": (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "/5")]'),



    "SIMILAR_PRODUCTS_COMPARISON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("similar products comparison")'),
    "CUSTOM_COMPARE_CTA": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("custom compare")'),
    "CUSTOM_COMPARE_DESC": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("do you want to compare Flipkart subscriptions with other brands?")'),
    "CUSTOM_COMPARE_IMAGE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(4)'),

    "ADD_TO_CART": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("add to cart")'),
    "BUY_NOW": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("buy now")'),
    "GO_TO_CART": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("go to cart")'),

    # cart page
    "CART_PRODUCT_TITLE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Flipkart Shopping Voucher")'),
    "CART_PRODUCT_QUANTITY": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("1").instance(1)'),
    "CART_PRODUCT_PRICE": (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "₹")]'),
    "CART_PRODUCT_PRICE_SAVED": (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "saved")]'),
    "CART_BUYING_FOR": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("buying for: ")'),
    "CART_BUYING_FOR_MYSELF": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("myself")'),
    "CART_EDIT_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(6)'),
    "CART_REMOVE_FROM_CART": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(3)'),
    "CART_PRODUCT_IMAGE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(2)'),
    "CART_PAGE_PROCEED_CTA": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("proceed to buy")'),
    "CART_TOTAL_TEXT": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Total")'),
    "CART_TOTAL_PRICE": (AppiumBy.XPATH, '(//android.widget.TextView[contains(@text, ".")])[2]'),
    "CART_TAXES_TEXT": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("inclusive of all taxes")'),

    "CART_APPLY_COUPON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("apply coupon")'),
    "CART_APPLY_COUPON_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(7)'),
    "CART_APPLY_COUPON_ARROW_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(8)'),

    #ORder Summary
    "ORDER_SUMMARY_TITLE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("order summary")'),
    "OREDER_SUMMARY_DISCOUNT": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("discount")'),
    "VIEW_PRICE_BREAK_UP": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("view price breakup")'),
    "VIEW_PRICE_BREAK_UP_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(9)'),
    "RECOMMENDED_FOR_YOU": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("recommended for you")'),
    "RECOMMENDED_FOR_YOU_SEE_ALL_TEXT": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("see all")'),
    "RECOMMENDED_FOR_YOU_SEE_ALL_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(10)'),

    "CART_PAGE_TITLE": (AppiumBy.XPATH, '(//android.widget.TextView[@text="cart"])[1]'),
    "PAGINATION_1":(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("1").instance(0)'),
    "PAGINATION_1_CART":(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("cart").instance(1)'),
    "PAGINATION_1_DASH":(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("- - - -").instance(0)'),
    "PAGINATION_2":(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("2")'),
    "PAGINATION_2_DETAILS":(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("details")'),
    "PAGINATION_2_DASH":(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("- - - -").instance(1)'),
    "PAGINATION_3":(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("3")'),
    "PAGINATION_3_CONFIRMATION":(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("confirmation")'),
    "SAVED_AMOUNT_BANNER":(AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "Yay!")]'),


    "ADDRESS_FOR_COMMUNICATION1": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("purchase details will be sent to")'),
    "BILLING_ADDRESS": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("billing address")'),
    "ORDER_DETAILS_CURRENT_ORDER": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("order details for current order")'),
    "DEFAULT_TAG": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("default")'),
    "COMMUNICATION_PHONE_NUMBER": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("phone number:")'),
    "COMMUNICATION_EMAIL": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("email ID:")'),
    "COMMUNICATION_EMAIL_ID": (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "@gmail")]'),
    "COMMUNICATION_SHIPPING_ADDRESS": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("shipping address:")'),
    "BILLING_ADDRESS_ADDRESS": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("billing address:")'),
    "ORDER_DETAILS": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("order details for current order")'),

    "PROCEED_TO_PAYMENT_CTA_BUTTON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Proceed to payment")'),

    "AMOUNT_PAYABLE_TEXT": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("amount payable")'),
    "CREDIT_DEBIT_CARD_PAYMENT_OPTION": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("pay via credit / debit cards")'),
    "CREDIT_DEBIT_CARD_NUMBER_ARROW": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(5)'),
    "INPUT_CREDIT_DEBIT_CARD_NUMBER": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("card number")'),
    "INPUT_CREDIT_DEBIT_CARD_NUMBER_FIELD": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("TextInput_EditText_card number")'),

}

class ProductDetailsPageFlipkart(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = AndroidActions(driver)

    def verify_product_title_price_discount(self):
        allureLogs("Verifying Product Title, Price, and Discount and if Out of Stock applicable")
        locators = {
            "Product Title": locators_pdpf["PRODUCT_TITLE"],
            "Product Price": locators_pdpf["PRODUCT_PRICE"],
            "Product Discount": locators_pdpf["PRODUCT_DISCOUNT"],
            "Out of Stock Tag": locators_pdpf["OUT_OF_STOCK"],
        }
        details = {}
        for detail_name, locator in locators.items():
            allureLogs(f"Checking element: {detail_name}")
            elements = self.driver.find_elements(*locator)
            if elements:
                if len(elements) > 1:  # Multiple elements case (e.g., for prices)
                    values = [el.text for el in elements]
                    details[detail_name] = values
                    allureLogs(f"Element {detail_name} is DISPLAYED | (Multiple Values: {values})")
                else:  # Single element case
                    value = elements[0].text
                    details[detail_name] = value
                    allureLogs(f"Element {detail_name} is DISPLAYED | (Value: {value})")
            else:
                details[detail_name] = None
                allureLogs(f"Element {detail_name} is NOT DISPLAYED")
        self.actions.screenshotAttachment("Product Title, Price, Discount and Out of Stock Tag Verification")
        return details

    def verify_product_details(self):
        allureLogs("Verifying other product details")
        locators = {
            "Occassion Option": locators_pdpf["PRODUCT_DETAILS1"],
            "Shopping Option": locators_pdpf["PRODUCT_DETAILS2"],
            "Denomination Option": locators_pdpf["PRODUCT_DETAILS3"],
            "Denomination Value": locators_pdpf["PRODUCT_DETAILS4"],
            "Brand Option": locators_pdpf["PRODUCT_DETAILS5"],
            "Brand Name": locators_pdpf["PRODUCT_DETAILS6"],
            "Type Option": locators_pdpf["PRODUCT_DETAILS7"],
            "Type Value": locators_pdpf["PRODUCT_DETAILS8"],
            "Validity Option": locators_pdpf["PRODUCT_DETAILS9"],
            "Validity Value": locators_pdpf["PRODUCT_DETAILS10"],
            "Place of Redemption Option": locators_pdpf["PRODUCT_DETAILS11"],
            "Place of Redemption Value": locators_pdpf["PRODUCT_DETAILS12"],
            "Collapse_Expand Arrow": locators_pdpf["COLLAPSE_EXPAND_ARROW"]

        }
        details = {}
        for detail_name, locator in locators.items():
            allureLogs(f"Checking element: {detail_name}")
            elements = self.driver.find_elements(*locator)
            if elements:
                if len(elements) > 1:  # Multiple elements case (e.g., for prices)
                    values = [el.text for el in elements]
                    details[detail_name] = values
                    allureLogs(f"Element {detail_name} is DISPLAYED | (Multiple Values: {values})")
                else:  # Single element case
                    value = elements[0].text
                    details[detail_name] = value
                    allureLogs(f"Element {detail_name} is DISPLAYED | (Value: {value})")
            else:
                details[detail_name] = None
                allureLogs(f"Element {detail_name} is NOT DISPLAYED")
        self.actions.screenshotAttachment("Product Details Verification")
        return details

    def verify_buying_quantity(self):
        allureLogs("Verifying Buying Options and Quantity")
        locators = {
            "Buying Option": locators_pdpf["BUYING"],
            "Buying For Myself Option": locators_pdpf["FOR_MYSELF"],
            "Buying for Myself Radio Button": locators_pdpf["FOR_MYSELF_RADIO_BUTTON"],
            "Buying As A Gift": locators_pdpf["AS_A_GIFT"],
            "Buying As A Gift Radio Button": locators_pdpf["AS_A_GIFT_RADIO_BUTTON"],
            "Quantity Option": locators_pdpf["QUANTITY"],
            "Quantity Count": locators_pdpf["QUANTITY_COUNT"],
            "Increase Quantity": locators_pdpf["INCREASE_QUANTITY"],
            "Decrease Quantity": locators_pdpf["DECREASE_QUANTITY"],

        }
        details = {}
        for detail_name, locator in locators.items():
            allureLogs(f"Checking element: {detail_name}")
            elements = self.driver.find_elements(*locator)
            if elements:
                if len(elements) > 1:  # Multiple elements case (e.g., for prices)
                    values = [el.text for el in elements]
                    details[detail_name] = values
                    allureLogs(f"Element {detail_name} is DISPLAYED | (Multiple Values: {values})")
                else:  # Single element case
                    value = elements[0].text
                    details[detail_name] = value
                    allureLogs(f"Element {detail_name} is DISPLAYED | (Value: {value})")
            else:
                details[detail_name] = None
                allureLogs(f"Element {detail_name} is NOT DISPLAYED")
        self.actions.screenshotAttachment("Buying Option and Quantity Verification")
        return details


    def verify_more_details(self):
        allureLogs("Verifying more details")
        locators = {
            "About Product": locators_pdpf["ABOUT_PRODUCT"],
            "About Product Expand and Collapse Icon": locators_pdpf["ABOUT_PRODUCT_EXPAND_COLLAPSE"],
            "Product Details": locators_pdpf["PRODUCT_DETAILS"],
            "Product Details Expand and Collapse Icon": locators_pdpf["PRODUCT_DETAILS_EXPAND_COLLAPSE"],
            "Steps to Redeem": locators_pdpf["STEPS_TO_REDEEM"],
            "Steps to Redeem Expand and Collapse Icon": locators_pdpf["STEPS_TO_REDEEM_EXPAND_COLLAPSE"],
            "T&C": locators_pdpf["TERMS_AND_CONDITIONS"],
            "T&C Expand and Collapse Icon": locators_pdpf["TERMS_AND_CONDITIONS_EXPAND_COLLAPSE"],
            "More from this Seller Tray": locators_pdpf["MORE_FROM_THIS_SELLER"],
        }
        details = {}
        for detail_name, locator in locators.items():
            allureLogs(f"Checking element: {detail_name}")
            elements = self.driver.find_elements(*locator)
            if elements:
                if len(elements) > 1:  # Multiple elements case (e.g., for prices)
                    values = [el.text for el in elements]
                    details[detail_name] = values
                    allureLogs(f"Element {detail_name} is DISPLAYED | (Multiple Values: {values})")
                else:  # Single element case
                    value = elements[0].text
                    details[detail_name] = value
                    allureLogs(f"Element {detail_name} is DISPLAYED | (Value: {value})")
            else:
                details[detail_name] = None
                allureLogs(f"Element {detail_name} is NOT DISPLAYED")
        self.actions.screenshotAttachment("About Product, Product Verification, Steps to Redeem, T&C, More from this sellar Tray Verification Completed")
        return details


    def verify_ratings_and_reviews(self):
        allureLogs("Verifying more details")
        locators = {
            "Ratings and Reviews Title": locators_pdpf["RATINGS_REVIEWS_TITLE"],
            "Write a Review": locators_pdpf["WRITE_A_REVIEW_CTA"],
            "View all Reviews Text": locators_pdpf["VIEW_ALL_REVIEWS_TEXT"],
            "View all Reviews CTA Button": locators_pdpf["VIEW_ALL_REVIEWS_CTA"],
            "No.of Ratings": locators_pdpf["NO_OF_RATINGS"],
            "No.of Reviews": locators_pdpf["NO_OF_REVIEWS"],
            "Average Rating": locators_pdpf["AVG_RATING"],
            "T&C Expand and Collapse Icon": locators_pdpf["TERMS_AND_CONDITIONS_EXPAND_COLLAPSE"],
        }
        details = {}
        for detail_name, locator in locators.items():
            allureLogs(f"Checking element: {detail_name}")
            elements = self.driver.find_elements(*locator)
            if elements:
                if len(elements) > 1:  # Multiple elements case (e.g., for prices)
                    values = [el.text for el in elements]
                    details[detail_name] = values
                    allureLogs(f"Element {detail_name} is DISPLAYED | (Multiple Values: {values})")
                else:  # Single element case
                    value = elements[0].text
                    details[detail_name] = value
                    allureLogs(f"Element {detail_name} is DISPLAYED | (Value: {value})")
            else:
                details[detail_name] = None
                allureLogs(f"Element {detail_name} is NOT DISPLAYED")
        self.actions.screenshotAttachment("Ratings and Reviews section Verification completed")
        return details

    def verify_addtocart_buynow_cta(self):
        allureLogs("Verifying more details")
        locators = {
            "Add to Cart CTA Button": locators_pdpf["ADD_TO_CART"],
            "Buy Now CTA Button": locators_pdpf["BUY_NOW"],
        }
        details = {}
        for detail_name, locator in locators.items():
            allureLogs(f"Checking element: {detail_name}")
            elements = self.driver.find_elements(*locator)
            if elements:
                if len(elements) > 1:  # Multiple elements case (e.g., for prices)
                    values = [el.text for el in elements]
                    details[detail_name] = values
                    allureLogs(f"Element {detail_name} is DISPLAYED | (Multiple Values: {values})")
                else:  # Single element case
                    value = elements[0].text
                    details[detail_name] = value
                    allureLogs(f"Element {detail_name} is DISPLAYED | (Value: {value})")
            else:
                details[detail_name] = None
                allureLogs(f"Element {detail_name} is NOT DISPLAYED")
        self.actions.screenshotAttachment("Add to Cart CTA & Buy Now CTA Verification Completed")
        return details

    def verify_similar_products_comparision(self):
        allureLogs("Verifying more details")
        locators = {
            "Similar Products Comparision Title": locators_pdpf["SIMILAR_PRODUCTS_COMPARISON"],
            "Custom Compare CTA Button": locators_pdpf["CUSTOM_COMPARE_CTA"],
            "Custom Compare CTA Description": locators_pdpf["CUSTOM_COMPARE_DESC"],
            "Custom Compare CTA Image": locators_pdpf["CUSTOM_COMPARE_IMAGE"],
        }
        details = {}
        for detail_name, locator in locators.items():
            allureLogs(f"Checking element: {detail_name}")
            elements = self.driver.find_elements(*locator)
            if elements:
                if len(elements) > 1:  # Multiple elements case (e.g., for prices)
                    values = [el.text for el in elements]
                    details[detail_name] = values
                    allureLogs(f"Element {detail_name} is DISPLAYED | (Multiple Values: {values})")
                else:  # Single element case
                    value = elements[0].text
                    details[detail_name] = value
                    allureLogs(f"Element {detail_name} is DISPLAYED | (Value: {value})")
            else:
                details[detail_name] = None
                allureLogs(f"Element {detail_name} is NOT DISPLAYED")
        self.actions.screenshotAttachment("Similar Products Verification Completed")
        return details

    '''def verify_change_denomination(self):
        denomination_amount = self.actions.wait_for_elements(*locators_pdpf['PRODUCT_PRICE'])
        if denomination_amount:
            allureLogs("Denominations are displayed")
            denomination_amount[4].click()
            allureLogs("Clicked on second Denomination")
            self.actions.screenshotAttachment("clicked on second Denomination")
        else:
            allureLogs("Denominations are not displayed")
            self.actions.screenshotAttachment("Denominations are not displayed")'''

    def verify_change_denomination(self):
        """
        Verifies if the product is out of stock and changes to a different denomination if available.
        If 'out of stock' is not found, it scrolls to the text 'product details'.
        """
        try:
            # Scroll to the text "out of stock"
            out_of_stock_element = self.actions.scroll_into_view("out of stock")

            if out_of_stock_element:
                allureLogs("'Out of stock' text is found after scrolling")
                # Find all denominations
                denomination_amount = self.actions.wait_for_elements(*locators_pdpf['PRODUCT_PRICE'])
                if denomination_amount and len(denomination_amount) > 4:  # Ensure at least 5 denominations are present
                    allureLogs("Denominations are displayed")
                    denomination_amount[4].click()  # Click on the 5th denomination (index 4)
                    allureLogs("Clicked on the second Denomination")
                    self.actions.screenshotAttachment("Clicked on second Denomination")
                else:
                    allureLogs("Denominations are not sufficient to perform the action")
                    self.actions.screenshotAttachment("Not enough denominations available")
            else:
                allureLogs("'Out of stock' text not found")
                # Scroll to the text "product details" if "out of stock" is not found
                product_details_element = self.actions.scroll_into_view("buying")
                if product_details_element:
                    allureLogs("Scrolled to 'buying'")
                else:
                    allureLogs("'Buying' text not found after scrolling")

        except Exception as e:
            allureLogs(f"An error occurred: {str(e)}")
            self.actions.screenshotAttachment(f"Error: {str(e)}")

    def verify_click_addto_gotocart_cta(self):
        self.actions.click_button(*locators_pdpf["ADD_TO_CART"])
        allureLogs("Clicked on Add to Cart CTA")
        self.actions.screenshotAttachment("Clicked on Add to Cart CTA")
        self.actions.is_element_displayed(*locators_pdpf["GO_TO_CART"])
        allureLogs("Found the Element Go to Cart CTA Button")
        self.actions.screenshotAttachment("Clicked on Go to Cart CTA")
        self.actions.click_button(*locators_pdpf["GO_TO_CART"])


    def verify_cart_page_product_details(self):
        """
        Verifies cart page product details, handles stale elements with retries,
        and logs status of each element.
        """
        allureLogs("Verifying CART page product details")

        locators = {
            "CART Page Product Title": locators_pdpf["CART_PRODUCT_TITLE"],
            "CART Page Product Quantity": locators_pdpf["CART_PRODUCT_QUANTITY"],
            "CART Page Product Price": locators_pdpf["CART_PRODUCT_PRICE"],
            "CART Page Product Price Saved": locators_pdpf["CUSTOM_COMPARE_IMAGE"],
            "CART Page Product Buying For": locators_pdpf["CART_BUYING_FOR"],
            "CART Page Product Buying For Myself": locators_pdpf["CART_BUYING_FOR_MYSELF"],
            "CART Page Product Edit Icon": locators_pdpf["CART_EDIT_ICON"],
            "CART Page Product Remove from Cart": locators_pdpf["CART_REMOVE_FROM_CART"],
            "CART Page Product Image": locators_pdpf["CART_PRODUCT_IMAGE"],
            "CART Page Proceed CTA": locators_pdpf["CART_PAGE_PROCEED_CTA"],
            "CART Page Total Text": locators_pdpf["CART_TOTAL_TEXT"],
            "CART Page Total Price": locators_pdpf["CART_TOTAL_PRICE"],
            "CART Page Proceed to Checkout": locators_pdpf["CART_PAGE_PROCEED_CTA"],
            "CART Page Taxes Text": locators_pdpf["CART_TAXES_TEXT"],
        }

        details = {}
        max_retries = 2  # Number of times to retry locating an element

        for detail_name, locator in locators.items():
            allureLogs(f"Checking element: {detail_name}")
            retries = 0

            while retries < max_retries:
                try:
                    # Wait until the element is present in DOM
                    WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located(locator)
                    )

                    elements = self.driver.find_elements(*locator)

                    if elements:
                        if len(elements) > 1:  # Multiple elements case (e.g., for prices)
                            values = [el.text for el in elements]
                            details[detail_name] = values
                            allureLogs(f"Element {detail_name} is DISPLAYED | (Multiple Values: {values})")
                        else:  # Single element case
                            value = elements[0].text
                            details[detail_name] = value
                            allureLogs(f"Element {detail_name} is DISPLAYED | (Value: {value})")
                    else:
                        details[detail_name] = None
                        allureLogs(f"Element {detail_name} is NOT DISPLAYED")

                    break  # If successful, exit the retry loop

                except StaleElementReferenceException:
                    retries += 1
                    allureLogs(f"StaleElementReferenceException: Retrying {retries}/{max_retries}")

                except TimeoutException:
                    allureLogs(f"TimeoutException: Element {detail_name} NOT found in time.")
                    break  # Stop retrying if element is not found at all

        self.actions.screenshotAttachment("CART Page Product Details Verification Completed")
        return details

    def verify_cart_page_order_summary(self):
        allureLogs("Verifying more details")
        locators = {
            "CART Page Order Summary Title": locators_pdpf["ORDER_SUMMARY_TITLE"],
            "CART Page Discount Availed": locators_pdpf["OREDER_SUMMARY_DISCOUNT"],
            "View Price Break Up": locators_pdpf["VIEW_PRICE_BREAK_UP"],
            "View Price Break Up Icon": locators_pdpf["VIEW_PRICE_BREAK_UP_ICON"],
            "Recommended For You Tray": locators_pdpf["RECOMMENDED_FOR_YOU"],
            "Recommended For You Tray See ALL Text": locators_pdpf["RECOMMENDED_FOR_YOU_SEE_ALL_TEXT"],
            "Recommended For You Tray See All Icon": locators_pdpf["RECOMMENDED_FOR_YOU_SEE_ALL_ICON"],
        }
        details = {}
        for detail_name, locator in locators.items():
            allureLogs(f"Checking element: {detail_name}")
            elements = self.driver.find_elements(*locator)
            if elements:
                if len(elements) > 1:  # Multiple elements case (e.g., for prices)
                    values = [el.text for el in elements]
                    details[detail_name] = values
                    allureLogs(f"Element {detail_name} is DISPLAYED | (Multiple Values: {values})")
                else:  # Single element case
                    value = elements[0].text
                    details[detail_name] = value
                    allureLogs(f"Element {detail_name} is DISPLAYED | (Value: {value})")
            else:
                details[detail_name] = None
                allureLogs(f"Element {detail_name} is NOT DISPLAYED")
        self.actions.screenshotAttachment("CART Page Order Summary Verification Completed")
        return details

    def verify_cart_page_pagination(self):
        allureLogs("Verifying more details")
        locators = {
            "CART Page Title": locators_pdpf["CART_PAGE_TITLE"],
            "Pagination Placement 1": locators_pdpf["PAGINATION_1"],
            "Pagination Cart": locators_pdpf["PAGINATION_1_CART"],
            "Pagination Details": locators_pdpf["PAGINATION_2_DETAILS"],
            "Pagination Confirmation": locators_pdpf["PAGINATION_3_CONFIRMATION"],
            "Pagination Placement 2": locators_pdpf["PAGINATION_2"],
            "Pagination Placement 3": locators_pdpf["PAGINATION_3"],
        }
        details = {}
        for detail_name, locator in locators.items():
            allureLogs(f"Checking element: {detail_name}")
            elements = self.driver.find_elements(*locator)
            if elements:
                if len(elements) > 1:  # Multiple elements case (e.g., for prices)
                    values = [el.text for el in elements]
                    details[detail_name] = values
                    allureLogs(f"Element {detail_name} is DISPLAYED | (Multiple Values: {values})")
                else:  # Single element case
                    value = elements[0].text
                    details[detail_name] = value
                    allureLogs(f"Element {detail_name} is DISPLAYED | (Value: {value})")
            else:
                details[detail_name] = None
                allureLogs(f"Element {detail_name} is NOT DISPLAYED")
        self.actions.screenshotAttachment("CART Page Title and Pagination Verification Completed")
        return details

    def verify_click_proceed_to_buy_cta(self):
        self.actions.click_button(*locators_pdpf["CART_PAGE_PROCEED_CTA"])
        allureLogs("Clicked on Proceed to Buy CTA")
        self.actions.screenshotAttachment("Clicked on Proceed to Buy CTA")

    def verify_payment_page(self):
        allureLogs("Verifying if user is on Payment Page")
        self.actions.is_element_displayed(*locators_pdpf["ADDRESS_FOR_COMMUNICATION1"])
        allureLogs("Verifying more details")
        locators = {
            "PURCHASE Details Will be sent to": locators_pdpf["ADDRESS_FOR_COMMUNICATION1"],
            "Billing Address": locators_pdpf["BILLING_ADDRESS"],
            "Order Details for Current Order": locators_pdpf["ORDER_DETAILS_CURRENT_ORDER"],
            "Default Tag": locators_pdpf["DEFAULT_TAG"],
            "Communication Phone Number": locators_pdpf["COMMUNICATION_PHONE_NUMBER"],
            "Communication Email Option": locators_pdpf["COMMUNICATION_EMAIL"],
            "Communication Email ID": locators_pdpf["COMMUNICATION_EMAIL_ID"],
            "Billing Adress Option": locators_pdpf["BILLING_ADDRESS_ADDRESS"],
            "Order Details": locators_pdpf["ORDER_DETAILS"],
            "Proceed to Payment CTA Button": locators_pdpf["PROCEED_TO_PAYMENT_CTA_BUTTON"],
        }
        details = {}
        for detail_name, locator in locators.items():
            allureLogs(f"Checking element: {detail_name}")
            elements = self.driver.find_elements(*locator)
            if elements:
                if len(elements) > 1:  # Multiple elements case (e.g., for prices)
                    values = [el.text for el in elements]
                    details[detail_name] = values
                    allureLogs(f"Element {detail_name} is DISPLAYED | (Multiple Values: {values})")
                else:  # Single element case
                    value = elements[0].text
                    details[detail_name] = value
                    allureLogs(f"Element {detail_name} is DISPLAYED | (Value: {value})")
            else:
                details[detail_name] = None
                allureLogs(f"Element {detail_name} is NOT DISPLAYED")
        self.actions.screenshotAttachment("CART Page Title and Pagination Verification Completed")
        return details

    def verify_proceed_to_payment_cta(self):
        self.actions.click_button(*locators_pdpf["PROCEED_TO_PAYMENT_CTA_BUTTON"])
        allureLogs("Clicked on Proceed to Buy CTA")
        self.actions.screenshotAttachment("Clicked on Proceed to Buy CTA")

    def verify_credit_debit_card_payment_section(self):
        """
        Verifies the presence of 'Amount Payable' text, and if found, checks other payment-related elements.
        Logs their displayed status and captures screenshots for debugging.
        """
        allureLogs("Verifying Credit/Debit Card Payment Section")

        # Define locators
        locators = {
            "Amount Payable Text": locators_pdpf["AMOUNT_PAYABLE_TEXT"],
            "Credit/Debit Card Payment Option": locators_pdpf["CREDIT_DEBIT_CARD_PAYMENT_OPTION"],
            "Credit/Debit Card Option Arrow": locators_pdpf["CREDIT_DEBIT_CARD_NUMBER_ARROW"],
            "Input Credit/Debit Card Number": locators_pdpf["INPUT_CREDIT_DEBIT_CARD_NUMBER"],
        }

        # Check if 'Amount Payable' is displayed
        amount_payable_element = self.driver.find_elements(*locators["Amount Payable Text"])
        if not amount_payable_element:
            allureLogs("Amount Payable Text is NOT DISPLAYED. Skipping further verification.")
            self.actions.screenshotAttachment("Amount_Payable_Not_Displayed")
            return False

        allureLogs("Amount Payable Text is DISPLAYED. Verifying remaining elements.")
        details = {}

        # Iterate through the remaining locators and check their presence
        for detail_name, locator in locators.items():
            elements = self.driver.find_elements(*locator)

            if elements:
                if len(elements) > 1:  # Multiple elements found
                    values = [el.text for el in elements if el.text.strip()]
                    details[detail_name] = values if values else "Element present but no text"
                    allureLogs(f"Element '{detail_name}' is DISPLAYED | (Multiple Values: {values})")
                else:  # Single element found
                    value = elements[0].text if elements[0].text.strip() else "Element present but no text"
                    details[detail_name] = value
                    allureLogs(f"Element '{detail_name}' is DISPLAYED | (Value: {value})")
            else:
                details[detail_name] = None
                allureLogs(f"Element '{detail_name}' is NOT DISPLAYED")

        # Capture final screenshot for verification
        self.actions.screenshotAttachment("Credit_Debit_Card_Payment_Section_Verification_Completed")
        return details


    def verify_input_cc_number(self, card_number):
        self.actions.click_button(*locators_pdpf["CREDIT_DEBIT_CARD_NUMBER_ARROW"])
        max_retries = 2
        retries = 0
        cc_locator = locators_pdpf["INPUT_CREDIT_DEBIT_CARD_NUMBER_FIELD"]

        while retries < max_retries:
            try:
                # Wait for element to be present and visible
                cc_input = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located(cc_locator)
                )
                cc_input.clear()
                cc_input.send_keys(card_number)
                allureLogs(f"Entered CC Number: {card_number}")
                return  # Success, exit method

            except StaleElementReferenceException:
                retries += 1
                allureLogs(f"StaleElementReferenceException: Retrying {retries}/{max_retries}")

            except TimeoutException:
                allureLogs("TimeoutException: Credit card input field not found.")
                break  # Stop retrying if element is not found

        # If input field is still not accessible, try clicking the field
        try:
            allureLogs("Trying to click the CC input field as fallback...")
            self.click_button(*cc_locator)
            # Retry entering text after clicking
            cc_input = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(cc_locator)
            )
            cc_input.send_keys(card_number)
            allureLogs(f"Entered CC Number after clicking: {card_number}")

        except Exception as e:
            allureLogs(f"Failed to enter CC number even after clicking: {str(e)}")
