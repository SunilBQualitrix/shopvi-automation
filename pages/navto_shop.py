from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from utils.custom_logger import allureLogs
from pages.actions.android_actions import AndroidActions

locators_ns = {
    "USB_DEBUGGING_POPUP": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("attention")'),      # noqa:E501
    "USB_DEBUGGING_CHECKBOX": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(1)'),   # noqa:E501
    "PROCEED_BUTTON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("proceed")'),     # noqa:E501
    "NUMBER_INPUT_FIELD": (AppiumBy.XPATH, '//android.widget.TextView[@text="enter mobile number"]'),     # noqa:E501
    "NUMBER_DIALOG_BOX_HEADER": (AppiumBy.ID, "com.google.android.gms:id/credentials_hint_picker_title"),     # noqa:E501
    "NUMBER_DIALOG_BOX_CANCEL": (AppiumBy.ID, 'com.google.android.gms:id/cancel'),    # noqa:E501
    "NUMBER_INPUT": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("{number}")'),      # noqa:E501
    "SEND_OTP": (AppiumBy.XPATH, '//android.widget.TextView[@text="send OTP"]'),      # noqa:E501
    "INPUT_OTP": (AppiumBy.XPATH, '//android.widget.TextView[@text="login with OTP"]'),   # noqa:E501
    "SHOP_BUTTON": (AppiumBy.XPATH, '//android.widget.TextView[@text="shop"]')
}


class NavtoShop(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = AndroidActions(driver)

    def click_number_input_field(self):
        """
        Handles the USB Debugging popup if displayed and clicks the number input field if visible.    # noqa:E501
        Returns:
        True if the number input field is successfully clicked, False otherwise.      # noqa:E501
        """
        allureLogs("Starting click_number_input_field method.")

        # Check if USB Debugging popup is displayed
        '''usb_debugging_popup = self.actions.is_element_displayed(*locators_ns["USB_DEBUGGING_POPUP"])   # noqa:E501
        if usb_debugging_popup:
            allureLogs("USB Debugging Popup is displayed.")
            self.actions.click_button(*locators_ns["USB_DEBUGGING_CHECKBOX"])
            allureLogs("Clicked on the USB Debugging checkbox.")
            self.actions.click_button(*locators_ns["PROCEED_BUTTON"])
            allureLogs("Clicked on the Proceed button.")'''

        # Check if Mobile Number Input field is displayed
        allureLogs("Checking if the Mobile Number Input Field is displayed.")
        mobile_num_input = self.actions.is_element_displayed(*locators_ns["NUMBER_INPUT_FIELD"])      # noqa:E501
        if mobile_num_input:
            allureLogs("Mobile Number Input Field is displayed.")
            self.actions.click_button(*locators_ns["NUMBER_INPUT_FIELD"])
            allureLogs("Clicked on the Mobile Number Input Field.")
            self.actions.screenshotAttachment("Mobile Number Input Field Clicked")    # noqa:E501
            return True
        else:
            allureLogs("Mobile Number Input Field is not displayed.")
            self.actions.screenshotAttachment("Mobile Number Input Field not displayed")      # noqa:E501
            return False

    def click_dialog_box(self):
        """
        Clicks the cancel button in the number dialog box if it is displayed.
        """
        allureLogs("Checking if the number dialog box is displayed.")
        dialog_box_header = self.actions.is_element_displayed(*locators_ns["NUMBER_DIALOG_BOX_HEADER"])   # noqa:E501
        if dialog_box_header:
            allureLogs("Number Dialog Box is displayed. Clicking the cancel button.")     # noqa:E501
            self.actions.click_button(*locators_ns["NUMBER_DIALOG_BOX_CANCEL"])
        else:
            allureLogs("Number Dialog Box is not displayed.")
        self.actions.screenshotAttachment("click_dialog_box")

    def input_valid_mobilenumber(self, mobile_number):
        """
        Inputs a valid mobile number by clicking the respective number buttons.
        """
        allureLogs(f"Entering the mobile number: {mobile_number}")
        by, value = locators_ns["NUMBER_INPUT"]
        for num in mobile_number:
            allureLogs(f"Entered mobile number: {num}")
            format_value = value.format(number=num)
            self.actions.click_button(by, format_value)
        allureLogs(f"{mobile_number} entered successfully.")
        self.actions.screenshotAttachment("input_valid_mobilenumber")

    def click_otp_button(self):
        """
        Clicks the OTP send button.
        """
        allureLogs("Clicking the OTP button.")
        self.actions.click_button(*locators_ns["SEND_OTP"])
        self.actions.screenshotAttachment("click_otp_button")

    def input_otp(self, OTP_number):
        """
        Inputs the OTP by clicking the respective number buttons.
        """
        allureLogs(f"Entering the OTP: {OTP_number}")
        by, value = locators_ns["NUMBER_INPUT"]
        for num in OTP_number:
            allureLogs(f"Entered OTP number: {num}")
            format_value = value.format(number=num)
            self.actions.click_button(by, format_value)
        allureLogs(f"{OTP_number} entered successfully.")
        self.actions.screenshotAttachment("input_otp")

    def login_wotp_button(self):
        """
        Clicks the login button after entering the OTP.
        """
        allureLogs("Clicking the login button after entering OTP.")
        self.actions.click_button(*locators_ns["INPUT_OTP"])
        self.actions.screenshotAttachment("login_wotp_button")

    def navto_shop(self):
        """
        Navigates to the shop page by clicking the shop button.
        """
        allureLogs("Navigating to the shop page.")
        if self.actions.is_element_displayed(*locators_ns["SHOP_BUTTON"]):
            allureLogs("Shop button is displayed. Clicking it.")
            self.actions.click_button(*locators_ns["SHOP_BUTTON"])
        else:
            allureLogs("Shop button is not displayed.")
        self.actions.screenshotAttachment("navto_shop")
