import time
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from utils.custom_logger import allureLogs
from pages.actions.android_actions import AndroidActions

locators_ap = {
    "BELL_ICON": (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="DS_SHOP_https://vishop.myvi.in/documents/35161/38258 / notification-icon.webp"]'),  # noqa:E501
    "BELL_ICON1": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(1)'),  # noqa:E501
    "Back_arrow": (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="DS_SHOP_https://vishop.myvi.in/documents/35161/38258/back-arrow.webp"]'),  # noqa:E501
    "BACK_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(0)'),  # noqa:E501
    "SEARCH_ICON": (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png"]'),  # noqa:E501
    "SEARCH_ICON1": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(2)'),  # noqa:E501

    "ACCOUNT_BUTTON1": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOPshop-account-icon.webp")'),  # noqa:E501
    "ACCOUNT_BUTTON2": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(0)'),  # noqa:E501

    "PAGE_TITLE": (AppiumBy.XPATH, '//android.widget.TextView[@text="account"]'),  # noqa:E501
    "YOUR_ORDERS": (AppiumBy.XPATH, '//android.widget.TextView[@text="your orders"]'),  # noqa:E501
    "CC": (AppiumBy.XPATH, '//android.widget.TextView[@text="credit cards"]'),  # noqa:E501
    "COUPOUNS": (AppiumBy.XPATH, '//android.widget.TextView[@text="coupons"]'),  # noqa:E501
    "SAVEDPAY": (AppiumBy.XPATH, '//android.widget.TextView[@text="saved payments"]'),  # noqa:E501
    "HELPANDSUPPORT": (AppiumBy.XPATH, '//android.widget.TextView[@text="help & support"]'),  # noqa:E501
    "FAQ": (AppiumBy.XPATH, '//android.widget.TextView[@text="FAQs"]'),
    "TANDC": (AppiumBy.XPATH, '//android.widget.TextView[@text="terms & conditions"]'),  # noqa:E501
    "PRIVACY_POLICY": (AppiumBy.XPATH, '//android.widget.TextView[@text="privacy policy"]'),  # noqa:E501
    "ABOUT_US": (AppiumBy.XPATH, '//android.widget.TextView[@text="about us"]'),  # noqa:E501
    "POWERED_BY": (AppiumBy.XPATH, '//android.widget.TextView[@text="powered by Vodafone Idea Business Service Ltd."]'),  # noqa:E501
    "PROFILE_NUMBER": (AppiumBy.XPATH, '//android.widget.TextView[@text="7507233095"]'),  # noqa:E501
    "EDIT_ICON1": (AppiumBy.XPATH, '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView'),  # noqa:E501
    "SAVINGS_BANNER": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(5)'),  # noqa:E501

    # Locators under orders page
    "ORDERSEARCHBOX": (AppiumBy.XPATH, '//android.widget.EditText[@text="search for orders..."]'),  # noqa:E501
    "ORDERSPAGETITLE": (AppiumBy.XPATH, '//android.widget.TextView[@text="your orders"]'),  # noqa:E501
    "ORDERSEARCHICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(1)'),  # noqa:E501
    "ORDERSPAGEFILTERICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(3)'),  # noqa:E501

    # Locators under credit cards page
    "CCRESUMEAPPLICATION": (AppiumBy.XPATH, '//android.widget.TextView[@text="resume applications"]'),  # noqa:E501
    "CCPAGETITLE": (AppiumBy.XPATH, '//android.widget.TextView[@text="my applications"]'),  # noqa:E501

    # Locators under coupons page
    "COUPONS_PAGETITLE": (AppiumBy.XPATH, '//android.widget.TextView[@text="coupons"]'),  # noqa:E501
    "COUPONS_NOTAVAVAILABLETEXT": (AppiumBy.XPATH, '//android.widget.TextView[@text="no coupons yet!"]'),  # noqa:E501
    "COUPONS_NOTAVAVAILABLETEXT_DESC": (AppiumBy.XPATH, '//android.widget.TextView[@text="I’ll come rushing when I have something for you!"]'),  # noqa:E501
    "COUPONS_XPLORE_STORES": (AppiumBy.XPATH, '//android.widget.TextView[@text="explore our stores"]'),  # noqa:E501
    "COUPONS_XPLORE_STORES_FILTER1": (AppiumBy.XPATH, '//android.widget.TextView[@text="credit cards"]'),  # noqa:E501
    "COUPONS_XPLORE_STORES_FILTER2": (AppiumBy.XPATH, '//android.widget.TextView[@text="entertainment"]'),  # noqa:E501
    "COUPONS_XPLORE_STORES_FILTER3": (AppiumBy.XPATH, '//android.widget.TextView[@text="food"]'),  # noqa:E501
    "COUPONS_XPLORE_STORES_FILTER4": (AppiumBy.XPATH, '//android.widget.TextView[@text="shopping"]'),  # noqa:E501
    "COUPONS_XPLORE_STORES_FILTER5": (AppiumBy.XPATH, '//android.widget.TextView[@text="travel"]'),  # noqa:E501

    # Locators under profile page
    "SAVEBUTTON": (AppiumBy.XPATH, '//android.widget.TextView[@text="save"]'),
    "TEXTDESC": (AppiumBy.XPATH, '//android.widget.TextView[@text="Order details will be sent to this email address"]'),  # noqa:E501
    "MYDETAILSPAGE": (AppiumBy.XPATH, '//android.widget.TextView[@text="my details"]'),  # noqa:E501
    "PROFILEPIC": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(1)'),  # noqa:E501
    "MOBILENUMBERFIELD": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(31)'),  # noqa:E501
    "EMAILIDFIELD": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(32)'),  # noqa:E501

    # Locators under saved payments page
    "SP_PAGE_TITLE": (AppiumBy.XPATH, '//android.view.View[@text="manage payment options"]'),  # noqa:E501
    "TITLE_TEXT": (AppiumBy.XPATH, '//android.widget.TextView[@text="nothing saved yet"]'),  # noqa:E501
    "CTA_BUTTON": (AppiumBy.XPATH, '//android.widget.TextView[@text="go back"]'),  # noqa:E501
    "NOTHING_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(1)'),   # noqa:E501
    "EDIT_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(4)'),  # noqa:E501
    "EDIT_ICON3": (AppiumBy.XPATH, '(//android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView)[5]'),  # noqa:E501
    "SAVED_CARDS": (AppiumBy.XPATH, '//android.widget.TextView[@text="saved cards"]'),  # noqa:E501
    "CARD_DISPLAYED": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(37)'),  # noqa:E501


    # Locators under FAQs page
    "FAQSEARCHBOX": (AppiumBy.XPATH, '//android.widget.EditText[@text="search for questions"]'),  # noqa:E501
    "FAQALLFILTER": (AppiumBy.XPATH, '//android.widget.TextView[@text="ALL"]'),
    "FAQACCOUNTFILTER": (AppiumBy.XPATH, '//android.widget.TextView[@text="Account"]'),  # noqa:E501
    "FAQCANCELLATIONFILTER": (AppiumBy.XPATH, '//android.widget.TextView[@text="Cancellation"]'),  # noqa:E501
    "FAQREFUNDFILTER": (AppiumBy.XPATH, '//android.widget.TextView[@text="Refund"]'),  # noqa:E501
    "FAQPAGETITLE": (AppiumBy.XPATH, '//android.widget.TextView[@text="FAQs"]'),  # noqa:E501
    "FAQ1": (AppiumBy.XPATH, '//android.widget.TextView[@text="How to make a purchase on Vi Shop?"]'),  # noqa:E501
    "FAQ2": (AppiumBy.XPATH, '//android.widget.TextView[@text="Where can I find the terms & conditions?"]'),  # noqa:E501
    "FAQ3": (AppiumBy.XPATH, '//android.widget.TextView[@text="What products are available on Vi Shop?"]'),  # noqa:E501
    "FAQ4": (AppiumBy.XPATH, '//android.widget.TextView[@text="Can I purchase a product for someone else?"]'),  # noqa:E501
    "FAQ5": (AppiumBy.XPATH, '//android.widget.TextView[@text="How do I view my order details?"]'),  # noqa:E501
    "FAQ6": (AppiumBy.XPATH, '//android.widget.TextView[@text="How do I redeem gift cards or vouchers?"]'),  # noqa:E501
    "FAQ7": (AppiumBy.XPATH, '//android.widget.TextView[@text="How long is the product valid?"]'),  # noqa:E501
    "FAQ8": (AppiumBy.XPATH, '//android.widget.TextView[@text="What all payment methods can I use?"]'),  # noqa:E501
    "FAQ9": (AppiumBy.XPATH, '//android.widget.TextView[@text="How do I claim a refund?"]'),  # noqa:E501
    "FAQ10": (AppiumBy.XPATH, '//android.widget.TextView[@text="How can I cancel or exchange a digital product?"]'),  # noqa:E501
}


class AccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = AndroidActions(driver)

    def verify_account_button(self):
        allureLogs("Verifying if the account button is displayed.")
        locators = [locators_ap["ACCOUNT_BUTTON1"], locators_ap["ACCOUNT_BUTTON2"]]   # noqa:E501
        for locator in locators:
            if self.actions.is_element_displayed(*locator):
                allureLogs(f"Account button is DISPLAYED")
                self.actions.screenshotAttachment("Account Button Displayed")
                return True
        allureLogs("Account button is not displayed.")
        self.actions.screenshotAttachment("Account Button Not Displayed")
        return False  # Return False if none of the locators are displayed

    def click_account_button(self):
        allureLogs("Clicking on the account button.")
        locators = [locators_ap["ACCOUNT_BUTTON1"], locators_ap["ACCOUNT_BUTTON2"]]   # noqa:E501
        for locator in locators:
            if self.actions.is_element_displayed(*locator):
                allureLogs(f"Account button is DISPLAYED")
                self.actions.click_button(*locator)  # Click the element
                allureLogs(f"Clicked on the account button")
                self.actions.screenshotAttachment("Clicked on the account button")    # noqa:E501
                return True  # Return True after clicking
        allureLogs("Account button is not clicked.")
        self.actions.screenshotAttachment("Account Button Not clicked")
        raise Exception("No account button is available to click")

    def verify_account_page_elements(self):
        allureLogs("Verifying All Elements are displayed on Account Page")
        locators = {
            "Account Page Title": locators_ap["PAGE_TITLE"],
            "Account Page Back Arrow": locators_ap["Back_arrow"],
            "Account Page Bell Icon1": locators_ap["BELL_ICON"],
            "Account Page Bell Icon2": locators_ap["BELL_ICON1"],
            "Account Page Search Icon": locators_ap["SEARCH_ICON"],
            "Account Page Search Icon1": locators_ap["SEARCH_ICON1"],
            "Account Page My Orders": locators_ap["YOUR_ORDERS"],
            "Account Page Credit Cards": locators_ap["CC"],
            "Account Page Coupons": locators_ap["COUPOUNS"],
            "Account Page Saved Payments": locators_ap["SAVEDPAY"],
            "Account Page Help & Support": locators_ap["HELPANDSUPPORT"],
            "Account Page Terms & Conditions": locators_ap["TANDC"],
            "Account Page Privacy Policy": locators_ap["PRIVACY_POLICY"],
            "Account Page FAQs": locators_ap["FAQ"],
            "About US": locators_ap["ABOUT_US"],
            "Powered By": locators_ap["POWERED_BY"],
            "Edit Icon": locators_ap["EDIT_ICON"],
            "Profile Number": locators_ap["PROFILE_NUMBER"],
            "Account Page Savings Banner": locators_ap["SAVINGS_BANNER"],
        }
        for element_name, locator in locators.items():
            if self.actions.is_element_displayed(*locator):
                elements = self.driver.find_elements(*locator)
                value = elements[0].text if elements else "No Text Available"
                allureLogs(f"Element {element_name} is DISPLAYED | (Value: {value})")     # noqa:E501
            else:
                allureLogs(f"Element {element_name} is NOT DISPLAYED")
        self.actions.screenshotAttachment("All Elements are displayed on Account Page")   # noqa:E501

    def verify_savings_banner(self):
        allureLogs("Verifying if the savings banner is displayed.")
        locator = locators_ap["SAVINGS_BANNER"]
        if self.actions.is_element_displayed(*locator):
            allureLogs("Savings banner is DISPLAYED")
            self.actions.screenshotAttachment("Savings Banner Displayed")
            return True  # Return True if displayed
        else:
            allureLogs("Savings banner is not displayed")
            self.actions.screenshotAttachment("Savings Banner Not Displayed")
            return False  # Return False if not displayed

    def verify_nav_to_orders_page(self):
        allureLogs("Navigating to the orders page.")
        locator = locators_ap["YOUR_ORDERS"]
        if self.actions.is_element_displayed(*locator):
            allureLogs("Element is DISPLAYED")
            self.actions.click_button(*locator)
            allureLogs("CLICKED on the element")
            self.actions.screenshotAttachment("Navigated to Orders Page")
            return True
        else:
            allureLogs(f"Element is NOT DISPLAYED with locator: {locator}")
            self.actions.screenshotAttachment("Failed to Navigate to Orders Page")    # noqa:E501
            return False

    def verify_nav_to_cc_page(self):
        allureLogs("Navigating to the credit cards page.")
        locator = locators_ap["CC"]
        if self.actions.is_element_displayed(*locator):
            allureLogs("Element is DISPLAYED")
            self.actions.click_button(*locator)
            allureLogs("CLICKED on the element")
            self.actions.screenshotAttachment("Navigated to Credit Cards Page")
            return True
        else:
            allureLogs(f"Element is NOT DISPLAYED with locator: {locator}")
            self.actions.screenshotAttachment("Failed to Navigate to Credit Cards Page")      # noqa:E501
            return False

    def verify_nav_to_coupons_page(self):
        allureLogs("Navigating to the coupons page.")
        locator = locators_ap["COUPOUNS"]
        if self.actions.is_element_displayed(*locator):
            allureLogs(f"Element is DISPLAYED")
            self.actions.click_button(*locator)
            allureLogs(f"CLCIKED on the element")
            self.actions.screenshotAttachment("Navigated to Coupons Page")
            return True
        else:
            allureLogs(f"Element is NOT DISPLAYED with locator: {locator}")
            self.actions.screenshotAttachment("Failed to Navigate to Coupons")
            return False

    def verify_nav_to_saved_payments_page(self):
        allureLogs("Navigating to the saved payments page.")
        locator = locators_ap["SAVEDPAY"]
        if self.actions.is_element_displayed(*locator):
            allureLogs("Element is DISPLAYED")
            self.actions.click_button(*locator)
            allureLogs("CLCIKED on the element")
            self.actions.screenshotAttachment("Navigated to Saved Payments Page")     # noqa:E501
            return True
        else:
            allureLogs(f"Element is NOT DISPLAYED with locator: {locator}")
            self.actions.screenshotAttachment("Failed to Navigate to Saved Payments Page")    # noqa:E501
            return False

    def verify_nav_to_help_and_support_page(self):
        allureLogs("Navigating to the help and support page.")
        locator = locators_ap["HELPANDSUPPORT"]
        if self.actions.is_element_displayed(*locator):
            allureLogs("Element is DISPLAYED")
            self.actions.click_button(*locator)
            allureLogs("CLICKED on the element")
            self.actions.screenshotAttachment("Navigated to Help and Support Page")   # noqa:E501
            return True
        else:
            allureLogs(f"Element is NOT DISPLAYED with locator: {locator}")
            self.actions.screenshotAttachment("Failed to Navigate to Help and Support Page")      # noqa:E501
            return False

    def verify_nav_to_faq_page(self):
        allureLogs("Navigating to the FAQs page.")
        locator = locators_ap["FAQ"]
        if self.actions.is_element_displayed(*locator):
            allureLogs("Element is DISPALYED")
            self.actions.click_button(*locator)
            allureLogs("CLICKED on the element")
            self.actions.screenshotAttachment("Navigated to FAQs Page")
            return True
        else:
            allureLogs(f"Element is NOT DISPLAYED with locator: {locator}")
            self.actions.screenshotAttachment("Failed to Navigate to FAQs Page")      # noqa:E501
            return False

    def verify_nav_to_tandc_page(self):
        allureLogs("Navigating to the terms and conditions page.")
        locator = locators_ap["TANDC"]
        if self.actions.is_element_displayed(*locator):
            allureLogs("Element is DISPLAYED")
            self.actions.click_button(*locator)
            allureLogs("CLCIKED on the element")
            time.sleep(5)
            self.actions.screenshotAttachment("Navigated to Terms and Conditions Page")   # noqa:E501
            return True
        else:
            allureLogs(f"Element is NOT DISPLAYED with locator: {locator}")
            self.actions.screenshotAttachment("Failed to Navigate to Terms and Conditions Page")      # noqa:E501
            return False

    def verify_nav_to_privacy_policy_page(self):
        allureLogs("Navigating to the privacy policy page.")
        locator = locators_ap["PRIVACY_POLICY"]
        if self.actions.is_element_displayed(*locator):
            allureLogs("Element is DISPLAYED")
            self.actions.click_button(*locator)
            allureLogs("CLICKED on the element")
            time.sleep(5)
            self.actions.screenshotAttachment("Navigated to Privacy Policy Page")     # noqa:E501
            return True
        else:
            allureLogs(f"Element is NOT DISPLAYED with locator: {locator}")
            self.actions.screenshotAttachment("Failed to Navigate to Privacy Policy Page")    # noqa:E501
            return False

    def verify_nav_to_about_us_page(self):
        allureLogs("Navigating to the about us page.")
        locator = locators_ap["ABOUT_US"]
        if self.actions.is_element_displayed(*locator):
            allureLogs(f"Element is displayed with locator: {locator}")
            self.actions.click_button(*locator)
            allureLogs(f"Clicked on the element with locator: {locator}")
            time.sleep(5)
            self.actions.screenshotAttachment("Navigated to About Us Page")
            return True
        else:
            allureLogs(f"Element is NOT DISPLAYED with locator: {locator}")
            self.actions.screenshotAttachment("Failed to Navigate to About Us Page")      # noqa:E501
            return False

    def verify_and_print_all_elements_on_faq_page(self):
        allureLogs("Verify All Elements are displayed on FAQ Page")
        locators = {
            "FAQ Search Box": locators_ap["FAQSEARCHBOX"],
            "FAQ All Filter": locators_ap["FAQALLFILTER"],
            "FAQ Account Filter": locators_ap["FAQACCOUNTFILTER"],
            "FAQ Cancellation Filter": locators_ap["FAQCANCELLATIONFILTER"],
            "FAQ Refund Filter": locators_ap["FAQREFUNDFILTER"],
            "FAQ Page Title": locators_ap["FAQPAGETITLE"],
            "FAQ Q1": locators_ap["FAQ1"],
            "FAQ Q2": locators_ap["FAQ2"],
            "FAQ Q3": locators_ap["FAQ3"],
            "FAQ Q4": locators_ap["FAQ4"],
            "FAQ Q5": locators_ap["FAQ5"],
            "FAQ Q6": locators_ap["FAQ6"],
            "FAQ Q7": locators_ap["FAQ7"],
            "FAQ Q8": locators_ap["FAQ8"],
            "FAQ Q9": locators_ap["FAQ9"],
            "FAQ Q10": locators_ap["FAQ10"],
        }
        for element_name, locator in locators.items():
            if self.actions.is_element_displayed(*locator):
                elements = self.driver.find_elements(*locator)
                value = elements[0].text if elements else "No Text Available"
                allureLogs(f"Element {element_name} is DISPLAYED | (Value: {value})")     # noqa:E501
            else:
                allureLogs(f"Element {element_name} is NOT DISPLAYED")
        self.actions.screenshotAttachment("All Elements are displayed on FAQ Page")   # noqa:E501

    def verify_and_print_all_elements_on_myorders_page(self):
        allureLogs("Verify All Elements are displayed on My Orders Page")
        locators = {
            "Order Page Search Box": locators_ap["ORDERSEARCHBOX"],
            "Order Page Title": locators_ap["ORDERSPAGETITLE"],
            "Order Page Search Icon": locators_ap["ORDERSEARCHICON"],
            "Order Page Filter Icon": locators_ap["ORDERSPAGEFILTERICON"],
        }
        for element_name, locator in locators.items():
            if self.actions.is_element_displayed(*locator):
                elements = self.driver.find_elements(*locator)
                value = elements[0].text if elements else "No Text Available"
                allureLogs(f"Element {element_name} is DISPLAYED | (Value: {value})")     # noqa:E501
            else:
                allureLogs(f"Element {element_name} is NOT DISPLAYED")
        self.actions.screenshotAttachment("All Elements are displayed on My Orders Page")   # noqa:E501

    def verify_and_print_all_elements_on_cc_page(self):
        allureLogs("Verify All Elements are displayed on Credit Card Page")
        locators = {
            "CC Page Title": locators_ap["CCRESUMEAPPLICATION"],
            "CC Resume Application": locators_ap["CCPAGETITLE"],
        }
        for element_name, locator in locators.items():
            if self.actions.is_element_displayed(*locator):
                elements = self.driver.find_elements(*locator)
                value = elements[0].text if elements else "No Text Available"
                allureLogs(f"Element {element_name} is DISPLAYED | (Value: {value})")     # noqa:E501
            else:
                allureLogs(f"Element {element_name} is NOT DISPLAYED")
        self.actions.screenshotAttachment("All Elements are displayed on Credit Card Page")   # noqa:E501

    def verify_nav_to_profile_page(self):
        allureLogs("Navigating to the profile page.")
        locator = locators_ap["EDIT_ICON3"]
        self.actions.wait(5)
        editicon = self.actions.wait_for_element(*locator)
        allureLogs(f"ICON is displayed with locator: {editicon}")
        if editicon:
            allureLogs(f"Element is displayed with locator: {editicon}")
            editicon.tap()
            allureLogs(f"Clicked on the element with locator: {editicon}")
            return True
        else:
            allureLogs(f"Element is NOT displayed with locator: {editicon}")
            return False

    def verify_and_print_all_elements_on_profile_page(self):
        allureLogs("Verify All Elements are displayed on Profile Page")
        locators = {
            "Save Button": locators_ap["SAVEBUTTON"],
            "Text Description": locators_ap["TEXTDESC"],
            "My Details Page": locators_ap["MYDETAILSPAGE"],
            "Profile Picture": locators_ap["PROFILEPIC"],
            "Mobile Number Field": locators_ap["MOBILENUMBERFIELD"],
            "Email ID Field": locators_ap["EMAILIDFIELD"],
        }
        for element_name, locator in locators.items():
            if self.actions.is_element_displayed(*locator):
                elements = self.driver.find_elements(*locator)
                value = elements[0].text if elements else "No Text Available"
                allureLogs(f"Element {element_name} is DISPLAYED | (Value: {value})")     # noqa:E501
            else:
                allureLogs(f"Element {element_name} is NOT DISPLAYED")
        self.actions.screenshotAttachment("All Elements are displayed on Profile Page")   # noqa:E501

    def verify_and_print_all_elements_under_CouponsPage(self):
        allureLogs("Verify All Elements are displayed on Coupon Page")
        locators = {
            "Coupon Page Title": locators_ap["COUPONS_PAGETITLE"],
            "Coupon Page Back Arrow": locators_ap["Back_arrow"],
            "Coupon Page Search Icon": locators_ap["SEARCH_ICON"],
            "Coupons not available Text": locators_ap["COUPONS_NOTAVAVAILABLETEXT"],      # noqa:E501
            "Coupons not available Text Description": locators_ap["COUPONS_NOTAVAVAILABLETEXT_DESC"],     # noqa:E501
            "Coupons Page Explore": locators_ap["COUPONS_XPLORE_STORES"],
            "Coupons Page Filter 1": locators_ap["COUPONS_XPLORE_STORES_FILTER1"],    # noqa:E501
            "Coupons Page Filter 2": locators_ap["COUPONS_XPLORE_STORES_FILTER2"],    # noqa:E501
            "Coupons Page Filter 3": locators_ap["COUPONS_XPLORE_STORES_FILTER3"],    # noqa:E501
            "Coupons Page Filter 4": locators_ap["COUPONS_XPLORE_STORES_FILTER4"],    # noqa:E501
            "Coupons Page Filter 5": locators_ap["COUPONS_XPLORE_STORES_FILTER5"],    # noqa:E501
        }
        for element_name, locator in locators.items():
            if self.actions.is_element_displayed(*locator):
                elements = self.driver.find_elements(*locator)
                value = elements[0].text if elements else "No Text Available"
                allureLogs(f"Element {element_name} is DISPLAYED | (Value: {value})")     # noqa:E501
            else:
                allureLogs(f"Element {element_name} is NOT DISPLAYED")
        self.actions.screenshotAttachment("All Elements are displayed on Coupon Page")    # noqa:E501

    def verify_and_print_all_elements_on_saved_payments_page(self):
        allureLogs("Verify All Saved Payments page elements are displayed")
        locators = {
            "SP_PAGE_TITLE": locators_ap["SP_PAGE_TITLE"],
            "TITLE_TEXT": locators_ap["TITLE_TEXT"],
            "CTA_BUTTON": locators_ap["CTA_BUTTON"],
            "NOTHING_ICON": locators_ap["NOTHING_ICON"],
            "SAVED_CARDS": locators_ap["SAVED_CARDS"],
            "CARD_DISPLAYED": locators_ap["CARD_DISPLAYED"],
        }

        for element_name, locator in locators.items():
            if self.actions.is_element_displayed(*locator):
                if element_name == "CTA_BUTTON":
                    self.actions.click_button(*locator)
                    allureLogs(f"CLICKED on the CTA button")
                else:
                    allureLogs(f"{element_name} is DISPLAYED")
            else:
                allureLogs(f"{element_name} is NOT DISPLAYED with locator: {locator}")    # noqa:E501
        self.actions.screenshotAttachment("All Saved Payments Page Elements Displayed")   # noqa:E501
        allureLogs("All saved payments page elements are displayed.")

