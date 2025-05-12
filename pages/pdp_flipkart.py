from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from utils.custom_logger import allureLogs
from pages.actions.android_actions import AndroidActions
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException   # noqa:E501
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

locators_pdpf = {

    "SHOP_BY_CATEGORY": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("shop by category")'),      # noqa:E501

    "PRODUCT_TITLE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("flipkart shopping voucher")'),    # noqa:E501
    "OUT_OF_STOCK": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("out of stock")'),      # noqa:E501
    "PRODUCT_PRICE": (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "₹")]'),     # noqa:E501
    "PRODUCT_DISCOUNT": (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "% off")]'),      # noqa:E501

    # Denominations
    "DENOMINATION_W/OFFER1": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("₹980").instance(1)'),     # noqa:E501
    "DENOMINATION_WO/OFFER1": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("₹1000").instance(1)'),   # noqa:E501
    "DENOMINATION_W/OFFER2": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("₹4900.0")'),      # noqa:E501
    "DENOMINATION_WO/OFFER2": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("₹5000.0")'),     # noqa:E501
    "DENOMINATION_W/OFFER3": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("₹9800.0")'),      # noqa:E501
    "DENOMINATION_WO/OFFER3": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("₹10000.0")'),    # noqa:E501
    "DENOMINATION_W/OFFER4": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("₹490.0")'),   # noqa:E501
    "DENOMINATION_WO/OFFER4": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("₹500.0")'),      # noqa:E501
    "DENOMINATION_W/OFFER5": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("₹2450.0")'),      # noqa:E501
    "DENOMINATION_WO/OFFER5": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("₹2500.0")'),     # noqa:E501

    "BUYING": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("buying:")'),     # noqa:E501
    "FOR_MYSELF": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("for myself")'),      # noqa:E501
    "FOR_MYSELF_RADIO_BUTTON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(4)'),      # noqa:E501
    "AS_A_GIFT": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("as a gift")'),    # noqa:E501
    "AS_A_GIFT_RADIO_BUTTON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(5)'),   # noqa:E501
    "QUANTITY": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("quantity:")'),     # noqa:E501
    "QUANTITY_COUNT": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("1")'),   # noqa:E501
    "INCREASE_QUANTITY": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(7)'),    # noqa:E501
    "DECREASE_QUANTITY": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(6)'),    # noqa:E501

    "ABOUT_PRODUCT": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("about product")'),    # noqa:E501
    "ABOUT_PRODUCT_EXPAND_COLLAPSE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(8)'),    # noqa:E501
    "ABOUT_PRODUCT_DESCRIPTION": (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "Flipkart is your one-stop online shopping destination")]'),     # noqa:E501

    "PRODUCT_DETAILS": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("product details")'),    # noqa:E501
    "PRODUCT_DETAILS_EXPAND_COLLAPSE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(9)'),      # noqa:E501
    "PRODUCT_DETAILS_DESCRIPTION": (AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="p"])[1]/android.widget.TextView'),   # noqa:E501

    "STEPS_TO_REDEEM": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("steps to redeem")'),    # noqa:E501
    "STEPS_TO_REDEEM_EXPAND_COLLAPSE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(10)'),     # noqa:E501
    "STEPS_TO_REDEEM_DESCRIPTION": (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView'),     # noqa:E501

    "TERMS_AND_CONDITIONS": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("terms and conditions")'),      # noqa:E501
    "TERMS_AND_CONDITIONS_EXPAND_COLLAPSE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(11)'),    # noqa:E501
    "TERMS_AND_CONDITIONS_DESCRIPTION": (AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="p"]/android.widget.TextView'),   # noqa:E501


    # Details
    "PRODUCT_DETAILS1": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("occasion:  ")'),   # noqa:E501
    "PRODUCT_DETAILS2": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("shopping")'),      # noqa:E501
    "PRODUCT_DETAILS3": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("denomination: ")'),    # noqa:E501
    "PRODUCT_DETAILS4": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Rs. 1000")'),      # noqa:E501
    "PRODUCT_DETAILS5": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("brand: ")'),   # noqa:E501
    "PRODUCT_DETAILS6": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Flipkart").instance(1)'),      # noqa:E501
    "PRODUCT_DETAILS7": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("type: ")'),    # noqa:E501
    "PRODUCT_DETAILS8": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("giftcard")'),      # noqa:E501
    "PRODUCT_DETAILS9": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("validity: ")'),    # noqa:E501
    "PRODUCT_DETAILS10": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("12 months")'),    # noqa:E501
    "PRODUCT_DETAILS11": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("place of redemption: ")'),    # noqa:E501
    "PRODUCT_DETAILS12": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("flipkart.com")'),     # noqa:E501
    "COLLAPSE_EXPAND_ARROW": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(5)'),    # noqa:E501

    "MORE_FROM_THIS_SELLER": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("more from this seller")'),    # noqa:E501



    "RATINGS_REVIEWS_TITLE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ratings and reviews")'),      # noqa:E501
    "WRITE_A_REVIEW_CTA": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("write a review")'),      # noqa:E501
    "VIEW_ALL_REVIEWS_TEXT": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("View all reviews")'),     # noqa:E501
    "VIEW_ALL_REVIEWS_CTA": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(16)'),    # noqa:E501
    "NO_OF_RATINGS": (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "ratings")]'),   # noqa:E501
    "NO_OF_REVIEWS": (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "reviews")]'),   # noqa:E501
    "AVG_RATING": (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "/5")]'),   # noqa:E501



    "SIMILAR_PRODUCTS_COMPARISON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("similar products comparison")'),    # noqa:E501
    "CUSTOM_COMPARE_CTA": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("custom compare")'),      # noqa:E501
    "CUSTOM_COMPARE_DESC": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("do you want to compare Flipkart subscriptions with other brands?")'),   # noqa:E501
    "CUSTOM_COMPARE_IMAGE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(4)'),     # noqa:E501

    "ADD_TO_CART": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("add to cart")'),        # noqa:E501
    "BUY_NOW": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("buy now")'),  # noqa:E501
    "GO_TO_CART": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("go to cart")'),      # noqa:E501

    # cart page
    "CART_PRODUCT_TITLE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Flipkart Shopping Voucher")'),   # noqa:E501
    "CART_PRODUCT_QUANTITY": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("1").instance(1)'),    # noqa:E501
    "CART_PRODUCT_PRICE": (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "₹")]'),    # noqa:E501
    "CART_PRODUCT_PRICE_SAVED": (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "saved")]'),      # noqa:E501
    "CART_BUYING_FOR": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("buying for: ")'),   # noqa:E501
    "CART_BUYING_FOR_MYSELF": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("myself")'),      # noqa:E501
    "CART_EDIT_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(6)'),   # noqa:E501
    "CART_REMOVE_FROM_CART": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(3)'),    # noqa:E501
    "CART_PRODUCT_IMAGE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(2)'),   # noqa:E501
    "CART_PAGE_PROCEED_CTA": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("proceed to buy")'),   # noqa:E501
    "CART_TOTAL_TEXT": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Total")'),      # noqa:E501
    "CART_TOTAL_PRICE": (AppiumBy.XPATH, '(//android.widget.TextView[contains(@text, ".")])[2]'),     # noqa:E501
    "CART_TAXES_TEXT": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("inclusive of all taxes")'),     # noqa:E501

    "CART_APPLY_COUPON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("apply coupon")'),     # noqa:E501
    "CART_APPLY_COUPON_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(7)'),   # noqa:E501
    "CART_APPLY_COUPON_ARROW_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(8)'),     # noqa:E501

    # ORder Summary
    "ORDER_SUMMARY_TITLE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("order summary")'),      # noqa:E501
    "OREDER_SUMMARY_DISCOUNT": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("discount")'),   # noqa:E501
    "VIEW_PRICE_BREAK_UP": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("view price breakup")'),     # noqa:E501
    "VIEW_PRICE_BREAK_UP_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(9)'),     # noqa:E501
    "RECOMMENDED_FOR_YOU": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("recommended for you")'),    # noqa:E501
    "RECOMMENDED_FOR_YOU_SEE_ALL_TEXT": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("see all")'),   # noqa:E501
    "RECOMMENDED_FOR_YOU_SEE_ALL_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(10)'),    # noqa:E501

    "CART_PAGE_TITLE": (AppiumBy.XPATH, '(//android.widget.TextView[@text="cart"])[1]'),      # noqa:E501
    "PAGINATION_1": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("1").instance(0)'),   # noqa:E501
    "PAGINATION_1_CART": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("cart").instance(1)'),   # noqa:E501
    "PAGINATION_1_DASH": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("- - - -").instance(0)'),   # noqa:E501
    "PAGINATION_2": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("2")'),      # noqa:E501
    "PAGINATION_2_DETAILS": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("details")'),   # noqa:E501
    "PAGINATION_2_DASH": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("- - - -").instance(1)'),      # noqa:E501
    "PAGINATION_3": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("3")'),     # noqa:E501
    "PAGINATION_3_CONFIRMATION": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("confirmation")'),     # noqa:E501
    "SAVED_AMOUNT_BANNER": (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "Yay!")]'),    # noqa:E501


    "ADDRESS_FOR_COMMUNICATION1": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("purchase details will be sent to")'),    # noqa:E501
    "BILLING_ADDRESS": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("billing address")'),    # noqa:E501
    "ORDER_DETAILS_CURRENT_ORDER": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("order details for current order")'),    # noqa:E501
    "DEFAULT_TAG": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("default")'),    # noqa:E501
    "COMMUNICATION_PHONE_NUMBER": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("phone number:")'),   # noqa:E501
    "COMMUNICATION_EMAIL": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("email ID:")'),      # noqa:E501
    "COMMUNICATION_EMAIL_ID": (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "@gmail")]'),   # noqa:E501
    "COMMUNICATION_SHIPPING_ADDRESS": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("shipping address:")'),   # noqa:E501
    "BILLING_ADDRESS_ADDRESS": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("billing address:")'),   # noqa:E501
    "ORDER_DETAILS": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("order details for current order")'),      # noqa:E501

    "PROCEED_TO_PAYMENT_CTA_BUTTON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Proceed to payment")'),   # noqa:E501

    "AMOUNT_PAYABLE_TEXT": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("amount payable")'),     # noqa:E501
    "CREDIT_DEBIT_CARD_PAYMENT_OPTION": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("pay via credit / debit cards")'),   # noqa:E501
    "CREDIT_DEBIT_CARD_NUMBER_ARROW": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(5)'),   # noqa:E501
    "INPUT_CREDIT_DEBIT_CARD_NUMBER": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("card number")'),     # noqa:E501
    "INPUT_CREDIT_DEBIT_CARD_NUMBER_FIELD": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("TextInput_EditText_card number")'),     # noqa:E501

    "SHOW_BREAKUP": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("show breakup0")'),    # noqa:E501
    "SUB_TOTAL": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("subtotal")'),    # noqa:E501
    "CONVENIENCE_FEE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("convenience fee ")'),    # noqa:E501
    "HIDE_BREAKUP": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("hide breakup0")'),    # noqa:E501
    "YES_EXIT": (AppiumBy.XPATH, "//android.widget.TextView[@text='yes, exit']"),    # noqa:E501


}


class ProductDetailsPageFlipkart(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = AndroidActions(driver)

    def verify_product_title_price_discount(self):
        allureLogs("Verifying Product Title, Price, and Discount and if Out of Stock applicable")     # noqa:E501
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
                if len(elements) > 1:  # Multiple elements case (e.g., for prices)    # noqa:E501
                    values = [el.text for el in elements]
                    details[detail_name] = values
                    allureLogs(f"✅ Element {detail_name} is DISPLAYED | (Multiple Values: {values})")   # noqa:E501
                else:  # Single element case
                    value = elements[0].text
                    details[detail_name] = value
                    allureLogs(f"✅ Element {detail_name} is DISPLAYED | (Value: {value})")      # noqa:E501
            else:
                details[detail_name] = None
                allureLogs(f"❌ Element {detail_name} is NOT DISPLAYED")
        self.actions.screenshotAttachment("Product Title, Price, Discount and Out of Stock Tag Verification")     # noqa:E501
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
                if len(elements) > 1:  # Multiple elements case (e.g., for prices)    # noqa:E501
                    values = [el.text for el in elements]
                    details[detail_name] = values
                    allureLogs(f"✅ Element {detail_name} is DISPLAYED | (Multiple Values: {values})")   # noqa:E501
                else:  # Single element case
                    value = elements[0].text
                    details[detail_name] = value
                    allureLogs(f"✅ Element {detail_name} is DISPLAYED | (Value: {value})")      # noqa:E501
            else:
                details[detail_name] = None
                allureLogs(f"❌ Element {detail_name} is NOT DISPLAYED")
        self.actions.screenshotAttachment("Product Details Verification")
        return details

    def verify_buying_quantity(self):
        allureLogs("Verifying Buying Options and Quantity")
        locators = {
            "Buying Option": locators_pdpf["BUYING"],
            "Buying For Myself Option": locators_pdpf["FOR_MYSELF"],
            "Buying for Myself Radio Button": locators_pdpf["FOR_MYSELF_RADIO_BUTTON"],   # noqa:E501
            "Buying As A Gift": locators_pdpf["AS_A_GIFT"],
            "Buying As A Gift Radio Button": locators_pdpf["AS_A_GIFT_RADIO_BUTTON"],   # noqa:E501
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
                if len(elements) > 1:  # Multiple elements case (e.g., for prices)  # noqa:E501
                    values = [el.text for el in elements]
                    details[detail_name] = values
                    allureLogs(f"✅ Element {detail_name} is DISPLAYED | (Multiple Values: {values})")  # noqa:E501
                else:  # Single element case
                    value = elements[0].text
                    details[detail_name] = value
                    allureLogs(f"✅ Element {detail_name} is DISPLAYED | (Value: {value})")    # noqa:E501
            else:
                details[detail_name] = None
                allureLogs(f"❌ Element {detail_name} is NOT DISPLAYED")
        self.actions.screenshotAttachment("Buying Option and Quantity Verification")    # noqa:E501
        return details

    def verify_more_details(self):
        allureLogs("Verifying more details")
        locators = {
            "About Product": locators_pdpf["ABOUT_PRODUCT"],
            "About Product Expand and Collapse Icon": locators_pdpf["ABOUT_PRODUCT_EXPAND_COLLAPSE"],   # noqa:E501
            "Product Details": locators_pdpf["PRODUCT_DETAILS"],
            "Product Details Expand and Collapse Icon": locators_pdpf["PRODUCT_DETAILS_EXPAND_COLLAPSE"],   # noqa:E501
            "Steps to Redeem": locators_pdpf["STEPS_TO_REDEEM"],
            "Steps to Redeem Expand and Collapse Icon": locators_pdpf["STEPS_TO_REDEEM_EXPAND_COLLAPSE"],   # noqa:E501
            "T&C": locators_pdpf["TERMS_AND_CONDITIONS"],
            "T&C Expand and Collapse Icon": locators_pdpf["TERMS_AND_CONDITIONS_EXPAND_COLLAPSE"],  # noqa:E501
            "More from this Seller Tray": locators_pdpf["MORE_FROM_THIS_SELLER"],   # noqa:E501
        }
        details = {}
        for detail_name, locator in locators.items():
            allureLogs(f"Checking element: {detail_name}")
            elements = self.driver.find_elements(*locator)
            if elements:
                if len(elements) > 1:  # Multiple elements case (e.g., for prices)  # noqa:E501
                    values = [el.text for el in elements]
                    details[detail_name] = values
                    allureLogs(f"✅ Element {detail_name} is DISPLAYED | (Multiple Values: {values})")     # noqa:E501
                else:  # Single element case
                    value = elements[0].text
                    details[detail_name] = value
                    allureLogs(f"✅ Element {detail_name} is DISPLAYED | (Value: {value})")    # noqa:E501
            else:
                details[detail_name] = None
                allureLogs(f"❌ Element {detail_name} is NOT DISPLAYED")
        self.actions.screenshotAttachment("About Product, Product Verification, Steps to Redeem, T&C, More from this sellar Tray Verification Completed")   # noqa:E501
        return details

    def verify_ratings_and_reviews(self):
        allureLogs("Verifying more details")
        locators = {
            "Ratings and Reviews Title": locators_pdpf["RATINGS_REVIEWS_TITLE"],    # noqa:E501
            "Write a Review": locators_pdpf["WRITE_A_REVIEW_CTA"],
            "View all Reviews Text": locators_pdpf["VIEW_ALL_REVIEWS_TEXT"],
            "View all Reviews CTA Button": locators_pdpf["VIEW_ALL_REVIEWS_CTA"],   # noqa:E501
            "No.of Ratings": locators_pdpf["NO_OF_RATINGS"],
            "No.of Reviews": locators_pdpf["NO_OF_REVIEWS"],
            "Average Rating": locators_pdpf["AVG_RATING"],
            "T&C Expand and Collapse Icon": locators_pdpf["TERMS_AND_CONDITIONS_EXPAND_COLLAPSE"],  # noqa:E501
        }
        details = {}
        for detail_name, locator in locators.items():
            allureLogs(f"Checking element: {detail_name}")
            elements = self.driver.find_elements(*locator)
            if elements:
                if len(elements) > 1:  # Multiple elements case (e.g., for prices)  # noqa:E501
                    values = [el.text for el in elements]
                    details[detail_name] = values
                    allureLogs(f"✅ Element {detail_name} is DISPLAYED | (Multiple Values: {values})")     # noqa:E501
                else:  # Single element case
                    value = elements[0].text
                    details[detail_name] = value
                    allureLogs(f"✅ Element {detail_name} is DISPLAYED | (Value: {value})")    # noqa:E501
            else:
                details[detail_name] = None
                allureLogs(f"❌ Element {detail_name} is NOT DISPLAYED")
        self.actions.screenshotAttachment("Ratings and Reviews section Verification completed")     # noqa:E501
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
                if len(elements) > 1:  # Multiple elements case (e.g., for prices)  # noqa:E501
                    values = [el.text for el in elements]
                    details[detail_name] = values
                    allureLogs(f"✅ Element {detail_name} is DISPLAYED | (Multiple Values: {values})")     # noqa:E501
                else:  # Single element case
                    value = elements[0].text
                    details[detail_name] = value
                    allureLogs(f"✅ Element {detail_name} is DISPLAYED | (Value: {value})")    # noqa:E501
            else:
                details[detail_name] = None
                allureLogs(f"❌ Element {detail_name} is NOT DISPLAYED")
        self.actions.screenshotAttachment("Add to Cart CTA & Buy Now CTA Verification Completed")   # noqa:E501
        return details

    def verify_similar_products_comparision(self):
        allureLogs("Verifying more details")
        locators = {
            "Similar Products Comparision Title": locators_pdpf["SIMILAR_PRODUCTS_COMPARISON"],     # noqa:E501
            "Custom Compare CTA Button": locators_pdpf["CUSTOM_COMPARE_CTA"],
            "Custom Compare CTA Description": locators_pdpf["CUSTOM_COMPARE_DESC"],     # noqa:E501
            "Custom Compare CTA Image": locators_pdpf["CUSTOM_COMPARE_IMAGE"],
        }
        details = {}
        for detail_name, locator in locators.items():
            allureLogs(f"Checking element: {detail_name}")
            elements = self.driver.find_elements(*locator)
            if elements:
                if len(elements) > 1:  # Multiple elements case (e.g., for prices)  # noqa:E501
                    values = [el.text for el in elements]
                    details[detail_name] = values
                    allureLogs(f"✅ Element {detail_name} is DISPLAYED | (Multiple Values: {values})")     # noqa:E501
                else:  # Single element case
                    value = elements[0].text
                    details[detail_name] = value
                    allureLogs(f"✅ Element {detail_name} is DISPLAYED | (Value: {value})")    # noqa:E501
            else:
                details[detail_name] = None
                allureLogs(f"❌ Element {detail_name} is NOT DISPLAYED")
        self.actions.screenshotAttachment("Similar Products Verification Completed")    # noqa:E501
        return details

    '''def verify_change_denomination(self):
        denomination_amount = self.actions.wait_for_elements(*locators_pdpf['PRODUCT_PRICE'])   # noqa:E501
        if denomination_amount:
            allureLogs("Denominations are displayed")
            denomination_amount[4].click()
            allureLogs("Clicked on second Denomination")
            self.actions.screenshotAttachment("clicked on second Denomination")
        else:
            allureLogs("Denominations are not displayed")
            self.actions.screenshotAttachment("Denominations are not displayed")'''   # noqa:E501

    def verify_change_denomination(self):
        """
        Verifies if the product is out of stock and changes to a different denomination if available.   # noqa:E501
        If 'out of stock' is not found, it scrolls to the text 'product details'.   # noqa:E501
        """
        try:
            # Scroll to the text "out of stock"
            out_of_stock_element = self.actions.scroll_into_view("out of stock")      # noqa:E501

            if out_of_stock_element:
                allureLogs("'Out of stock' text is found after scrolling")
                # Find all denominations
                denomination_amount = self.actions.wait_for_elements(*locators_pdpf['PRODUCT_PRICE'])   # noqa:E501
                if denomination_amount and len(denomination_amount) > 4:  # Ensure at least 5 denominations are present # noqa:E501
                    allureLogs("Denominations are displayed")
                    denomination_amount[4].click()  # Click on the 5th denomination (index 4)   # noqa:E501
                    allureLogs("Clicked on the second Denomination")
                    self.actions.screenshotAttachment("Clicked on second Denomination")     # noqa:E501
                else:
                    allureLogs("Denominations are not sufficient to perform the action")    # noqa:E501
                    self.actions.screenshotAttachment("Not enough denominations available")     # noqa:E501
            else:
                allureLogs("'Out of stock' text not found")
                # Scroll to the text "product details" if "out of stock" is not found   # noqa:E501
                product_details_element = self.actions.scroll_into_view("buying")   # noqa:E501
                if product_details_element:
                    allureLogs("Scrolled to 'buying'")
                else:
                    allureLogs("'Buying' text not found after scrolling")

        except Exception as e:
            allureLogs(f"❌ An error occurred: {str(e)}")
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
        Verifies cart page product details, handles stale elements with retries,    # noqa:E501
        and logs status of each element.
        """
        allureLogs("Verifying CART page product details")

        locators = {
            "CART Page Product Title": locators_pdpf["CART_PRODUCT_TITLE"],
            "CART Page Product Quantity": locators_pdpf["CART_PRODUCT_QUANTITY"],   # noqa:E501
            "CART Page Product Price": locators_pdpf["CART_PRODUCT_PRICE"],
            "CART Page Product Price Saved": locators_pdpf["CUSTOM_COMPARE_IMAGE"],     # noqa:E501
            "CART Page Product Buying For": locators_pdpf["CART_BUYING_FOR"],
            "CART Page Product Buying For Myself": locators_pdpf["CART_BUYING_FOR_MYSELF"],     # noqa:E501
            "CART Page Product Edit Icon": locators_pdpf["CART_EDIT_ICON"],
            "CART Page Product Remove from Cart": locators_pdpf["CART_REMOVE_FROM_CART"],   # noqa:E501
            "CART Page Product Image": locators_pdpf["CART_PRODUCT_IMAGE"],
            "CART Page Proceed CTA": locators_pdpf["CART_PAGE_PROCEED_CTA"],
            "CART Page Total Text": locators_pdpf["CART_TOTAL_TEXT"],
            "CART Page Total Price": locators_pdpf["CART_TOTAL_PRICE"],
            "CART Page Proceed to Checkout": locators_pdpf["CART_PAGE_PROCEED_CTA"],    # noqa:E501
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
                        if len(elements) > 1:  # Multiple elements case (e.g., for prices)  # noqa:E501
                            values = [el.text for el in elements]
                            details[detail_name] = values
                            allureLogs(f"✅ Element {detail_name} is DISPLAYED | (Multiple Values: {values})")     # noqa:E501
                        else:  # Single element case
                            value = elements[0].text
                            details[detail_name] = value
                            allureLogs(f"✅ Element {detail_name} is DISPLAYED | (Value: {value})")    # noqa:E501
                    else:
                        details[detail_name] = None
                        allureLogs(f"❌ Element {detail_name} is NOT DISPLAYED")

                    break  # If successful, exit the retry loop

                except StaleElementReferenceException:
                    retries += 1
                    allureLogs(f"✅ StaleElementReferenceException: Retrying {retries}/{max_retries}")     # noqa:E501

                except TimeoutException:
                    allureLogs(f"❌ TimeoutException: Element {detail_name} NOT found in time.")   # noqa:E501
                    break  # Stop retrying if element is not found at all

        self.actions.screenshotAttachment("CART Page Product Details Verification Completed")   # noqa:E501
        return details

    def verify_cart_page_order_summary(self):
        allureLogs("Verifying more details")
        locators = {
            "CART Page Order Summary Title": locators_pdpf["ORDER_SUMMARY_TITLE"],  # noqa:E501
            "CART Page Discount Availed": locators_pdpf["OREDER_SUMMARY_DISCOUNT"],     # noqa:E501
            "View Price Break Up": locators_pdpf["VIEW_PRICE_BREAK_UP"],
            "View Price Break Up Icon": locators_pdpf["VIEW_PRICE_BREAK_UP_ICON"],  # noqa:E501
            "Recommended For You Tray": locators_pdpf["RECOMMENDED_FOR_YOU"],
            "Recommended For You Tray See ALL Text": locators_pdpf["RECOMMENDED_FOR_YOU_SEE_ALL_TEXT"],     # noqa:E501
            "Recommended For You Tray See All Icon": locators_pdpf["RECOMMENDED_FOR_YOU_SEE_ALL_ICON"],     # noqa:E501
        }
        details = {}
        for detail_name, locator in locators.items():
            allureLogs(f"Checking element: {detail_name}")
            elements = self.driver.find_elements(*locator)
            if elements:
                if len(elements) > 1:  # Multiple elements case (e.g., for prices)  # noqa:E501
                    values = [el.text for el in elements]
                    details[detail_name] = values
                    allureLogs(f"✅ Element {detail_name} is DISPLAYED | (Multiple Values: {values})")     # noqa:E501
                else:  # Single element case
                    value = elements[0].text
                    details[detail_name] = value
                    allureLogs(f"✅ Element {detail_name} is DISPLAYED | (Value: {value})")    # noqa:E501
            else:
                details[detail_name] = None
                allureLogs(f"❌ Element {detail_name} is NOT DISPLAYED")
        self.actions.screenshotAttachment("CART Page Order Summary Verification Completed")  # noqa:E501
        return details

    def verify_cart_page_pagination(self):
        allureLogs("Verifying more details")
        locators = {
            "CART Page Title": locators_pdpf["CART_PAGE_TITLE"],
            "Pagination Placement 1": locators_pdpf["PAGINATION_1"],
            "Pagination Cart": locators_pdpf["PAGINATION_1_CART"],
            "Pagination Details": locators_pdpf["PAGINATION_2_DETAILS"],
            "Pagination Confirmation": locators_pdpf["PAGINATION_3_CONFIRMATION"],  # noqa:E501
            "Pagination Placement 2": locators_pdpf["PAGINATION_2"],
            "Pagination Placement 3": locators_pdpf["PAGINATION_3"],
        }
        details = {}
        for detail_name, locator in locators.items():
            allureLogs(f"Checking element: {detail_name}")
            elements = self.driver.find_elements(*locator)
            if elements:
                if len(elements) > 1:  # Multiple elements case (e.g., for prices)  # noqa:E501
                    values = [el.text for el in elements]
                    details[detail_name] = values
                    allureLogs(f"✅ Element {detail_name} is DISPLAYED | (Multiple Values: {values})")     # noqa:E501
                else:  # Single element case
                    value = elements[0].text
                    details[detail_name] = value
                    allureLogs(f"✅ Element {detail_name} is DISPLAYED | (Value: {value})")    # noqa:E501
            else:
                details[detail_name] = None
                allureLogs(f"❌ Element {detail_name} is NOT DISPLAYED")
        self.actions.screenshotAttachment("CART Page Title and Pagination Verification Completed")  # noqa:E501
        return details

    def verify_click_proceed_to_buy_cta(self):
        self.actions.click_button(*locators_pdpf["CART_PAGE_PROCEED_CTA"])
        allureLogs("Clicked on Proceed to Buy CTA")
        self.actions.screenshotAttachment("Clicked on Proceed to Buy CTA")

    def verify_payment_page(self):
        allureLogs("Verifying if user is on Payment Page")
        self.actions.is_element_displayed(*locators_pdpf["ADDRESS_FOR_COMMUNICATION1"])     # noqa:E501
        allureLogs("Verifying more details")
        locators = {
            "PURCHASE Details Will be sent to": locators_pdpf["ADDRESS_FOR_COMMUNICATION1"],    # noqa:E501
            "Billing Address": locators_pdpf["BILLING_ADDRESS"],
            "Order Details for Current Order": locators_pdpf["ORDER_DETAILS_CURRENT_ORDER"],       # noqa:E501
            "Default Tag": locators_pdpf["DEFAULT_TAG"],
            "Communication Phone Number": locators_pdpf["COMMUNICATION_PHONE_NUMBER"],  # noqa:E501
            "Communication Email Option": locators_pdpf["COMMUNICATION_EMAIL"],
            "Communication Email ID": locators_pdpf["COMMUNICATION_EMAIL_ID"],
            "Billing Adress Option": locators_pdpf["BILLING_ADDRESS_ADDRESS"],
            "Order Details": locators_pdpf["ORDER_DETAILS"],
            "Proceed to Payment CTA Button": locators_pdpf["PROCEED_TO_PAYMENT_CTA_BUTTON"],    # noqa:E501
        }
        details = {}
        for detail_name, locator in locators.items():
            allureLogs(f"Checking element: {detail_name}")
            elements = self.driver.find_elements(*locator)
            if elements:
                if len(elements) > 1:  # Multiple elements case (e.g., for prices)  # noqa:E501
                    values = [el.text for el in elements]
                    details[detail_name] = values
                    allureLogs(f"✅ Element {detail_name} is DISPLAYED | (Multiple Values: {values})")     # noqa:E501
                else:  # Single element case
                    value = elements[0].text
                    details[detail_name] = value
                    allureLogs(f"✅ Element {detail_name} is DISPLAYED | (Value: {value})")    # noqa:E501
            else:
                details[detail_name] = None
                allureLogs(f"❌ Element {detail_name} is NOT DISPLAYED")
        self.actions.screenshotAttachment("CART Page Title and Pagination Verification Completed")  # noqa:E501
        return details

    def verify_proceed_to_payment_cta(self):
        self.actions.click_button(*locators_pdpf["PROCEED_TO_PAYMENT_CTA_BUTTON"])  # noqa:E501
        allureLogs("Clicked on Proceed to Buy CTA")
        self.actions.screenshotAttachment("Clicked on Proceed to Buy CTA")

    def verify_credit_debit_card_payment_section(self):
        """
        Verifies the presence of 'Amount Payable' text, and if found, checks other payment-related elements.    # noqa:E501
        Logs their displayed status and captures screenshots for debugging.
        """
        allureLogs("Verifying Credit/Debit Card Payment Section")

        # Define locators
        locators = {
            "Amount Payable Text": locators_pdpf["AMOUNT_PAYABLE_TEXT"],
            "Credit/Debit Card Payment Option": locators_pdpf["CREDIT_DEBIT_CARD_PAYMENT_OPTION"],  # noqa:E501
            "Credit/Debit Card Option Arrow": locators_pdpf["CREDIT_DEBIT_CARD_NUMBER_ARROW"],  # noqa:E501
            "Input Credit/Debit Card Number": locators_pdpf["INPUT_CREDIT_DEBIT_CARD_NUMBER"],  # noqa:E501
        }

        # Check if 'Amount Payable' is displayed
        amount_payable_element = self.driver.find_elements(*locators["Amount Payable Text"])    # noqa:E501
        if not amount_payable_element:
            allureLogs("Amount Payable Text is NOT DISPLAYED. Skipping further verification.")  # noqa:E501
            self.actions.screenshotAttachment("Amount_Payable_Not_Displayed")
            return False

        allureLogs("Amount Payable Text is DISPLAYED. Verifying remaining elements.")   # noqa:E501
        details = {}

        # Iterate through the remaining locators and check their presence
        for detail_name, locator in locators.items():
            elements = self.driver.find_elements(*locator)

            if elements:
                if len(elements) > 1:  # Multiple elements found
                    values = [el.text for el in elements if el.text.strip()]
                    details[detail_name] = values if values else "Element present but no text"  # noqa:E501
                    allureLogs(f"✅ Element '{detail_name}' is DISPLAYED | (Multiple Values: {values})")   # noqa:E501
                else:  # Single element found
                    value = elements[0].text if elements[0].text.strip() else "Element present but no text"     # noqa:E501
                    details[detail_name] = value
                    allureLogs(f"✅ Element '{detail_name}' is DISPLAYED | (Value: {value})")  # noqa:E501
            else:
                details[detail_name] = None
                allureLogs(f"❌ Element '{detail_name}' is NOT DISPLAYED")

        # Capture final screenshot for verification
        self.actions.screenshotAttachment("Credit_Debit_Card_Payment_Section_Verification_Completed")   # noqa:E501
        return details

    def verify_input_cc_number(self, card_number):
        self.actions.click_button(*locators_pdpf["CREDIT_DEBIT_CARD_NUMBER_ARROW"])     # noqa:E501
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
                allureLogs(f"StaleElementReferenceException: Retrying {retries}/{max_retries}")     # noqa:E501

            except TimeoutException:
                allureLogs("TimeoutException: Credit card input field not found.")  # noqa:E501
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
            allureLogs(f"✅ Entered CC Number after clicking: {card_number}")

        except Exception as e:
            allureLogs(f"❌ Failed to enter CC number even after clicking: {str(e)}")  # noqa:E501

    def verify_convenience_fee(self):
        self.actions.click_button(*locators_pdpf["SHOW_BREAKUP"])
        allureLogs("Clicked on Show Breakup")
        self.actions.screenshotAttachment("Clicked on Show Breakup")
        self.actions.is_element_displayed(*locators_pdpf["SUB_TOTAL"])
        allureLogs("Sub Total TEXT is displayed")
        locators = {
            "Sub Total": locators_pdpf["SUB_TOTAL"],    # noqa:E501
            "Convenience Fee": locators_pdpf["CONVENIENCE_FEE"],
            "Amount": locators_pdpf["PRODUCT_PRICE"],       # noqa:E501
            "Hide Breakup Button": locators_pdpf["HIDE_BREAKUP"],
            "Amount Payable Text": locators_pdpf["AMOUNT_PAYABLE_TEXT"],
        }
        details = {}
        for detail_name, locator in locators.items():
            allureLogs(f"Checking element: {detail_name}")
            elements = self.driver.find_elements(*locator)
            if elements:
                if len(elements) > 1:  # Multiple elements case (e.g., for prices)  # noqa:E501
                    values = [el.text for el in elements]
                    details[detail_name] = values
                    allureLogs(f"✅ Element: {detail_name} is DISPLAYED | (Multiple Values: {values})")     # noqa:E501
                else:  # Single element case
                    value = elements[0].text
                    details[detail_name] = value
                    allureLogs(f"✅ Element: {detail_name} is DISPLAYED | (Value: {value})")    # noqa:E501
            else:
                details[detail_name] = None
                allureLogs(f"❌ Element: {detail_name} is NOT DISPLAYED")
        self.actions.screenshotAttachment("CART Page Title and Pagination Verification Completed")  # noqa:E501
        return details

    def verify_navigation_to_home_page(self):
        allureLogs("Starting Navigation Back to Home Page")

        locators = {
            "Exit Confirmation Dialog": locators_pdpf["YES_EXIT"],
            "Proceed to Payment Button": locators_pdpf["PROCEED_TO_PAYMENT_CTA_BUTTON"],    # noqa:E501
            "Cart Page Proceed Button": locators_pdpf["CART_PAGE_PROCEED_CTA"],
            "Add to Cart Button": locators_pdpf["ADD_TO_CART"],
            "Shop by Category Section": locators_pdpf["SHOP_BY_CATEGORY"]
        }

        navigation_steps = [
            ("Navigating back to Purchase Details Page", "Exit Confirmation Dialog"),   # noqa:E501
            ("Navigating back to Cart Page", "Proceed to Payment Button"),
            ("Navigating back to Product Details Page", "Cart Page Proceed Button"),    # noqa:E501
            ("Navigating back to Shop Dashboard", "Add to Cart Button"),
            ("Final step: Shop Dashboard should be visible", "Shop by Category Section")    # noqa:E501
        ]

        # First Back Navigation with YES_EXIT Confirmation
        self.driver.back()
        allureLogs("First back action triggered")

        if self.actions.is_element_displayed(*locators["Exit Confirmation Dialog"]):    # noqa:E501
            allureLogs("Exit Confirmation Dialog is displayed, clicking YES_EXIT")  # noqa:E501
            self.actions.click_button(*locators["Exit Confirmation Dialog"])
            self.actions.screenshotAttachment("Exit Confirmation Clicked")
        else:
            allureLogs("Exit Confirmation Dialog NOT displayed")

        # Continue with the rest of the back navigation steps
        for step_description, element_name in navigation_steps[1:]:  # Skipping first as it was handled separately  # noqa:E501
            self.driver.back()
            allureLogs(step_description)

            if self.actions.is_element_displayed(*locators[element_name]):
                allureLogs(f"✅ {element_name} is DISPLAYED")
            else:
                allureLogs(f"❌ {element_name} is NOT DISPLAYED")

            self.actions.screenshotAttachment(step_description)

        self.driver.back()
        allureLogs("Navigation to Home Page Completed ✅")
