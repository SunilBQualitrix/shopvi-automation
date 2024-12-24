import time
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

locators_ns = {
    "NUMBER_INPUT_FIELD": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("enter mobile number")'),
    "NUMBER_DIALOG_BOX": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("NONE OF THE ABOVE")'),
    "SEND_OTP": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("send OTP")'),
    "INPUT_OTP": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("login with OTP")'),
    "SHOP_BUTTON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("shop")')
}


class NavtoShop(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_number_input_field(self):
        self.actions.is_element_displayed(*locators_ns["NUMBER_INPUT_FIELD"])
        self.actions.click_button(*locators_ns["NUMBER_INPUT_FIELD"])

    def click_dialog_box(self):
        self.actions.is_element_displayed(*locators_ns["NUMBER_DIALOG_BOX"])

    def input_valid_mobilenumber(self, mobile_number):
        if len(mobile_number) == 10 and mobile_number.isdigit():
            for digit in mobile_number:
                self.sendNumberViaKeypad(digit)
                time.sleep(0.5)
        else:
            raise ValueError("Mobile number must be exactly 10 digits and numeric.")

    def click_otp_button(self):
        self.actions.click_button(*locators_ns["SEND_OTP"])

    def input_otp(self, OTP_number):
        if len(OTP_number) == 4 and OTP_number.isdigit():
            for digit in OTP_number:
                self.sendOtpViaKeypad(digit)
                time.sleep(0.5)
        else:
            raise ValueError("OTP number must be exactly 4 digits and numeric.")

    def login_wotp_button(self):
        self.actions.click_button(*locators_ns["INPUT_OTP"])

    def navto_shop(self):
        self.actions.is_element_displayed(*locators_ns["SHOP_BUTTON"])
        self.actions.click_button(*locators_ns["SHOP_BUTTON"])
