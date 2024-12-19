import time
from appium.webdriver.common.appiumby import AppiumBy
from pages.actions.android_actions import AndroidAction
from pages.base_page import BasePage

locators_ns = {
    "NUMBER_INPUT_FIELD": (AppiumBy.TEXT, 'enter mobile number'),
    "NUMBER_DIALOG_BOX": (AppiumBy.TEXT, 'NONE OF THE ABOVE'),
    "SEND_OTP": (AppiumBy.TEXT, 'send OTP'),
    "INPUT_OTP": (AppiumBy.TEXT, 'login with OTP'),
    "SHOP_BUTTON": (AppiumBy.TEXT, 'shop')
}


class NavtoShop(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_number_input_field(self):
        if isinstance(self.actions, AndroidAction):
            self.actions.is_element_displayed(*locators_ns["NUMBER_INPUT_FIELD"]),  # noqa:E501
            self.actions.click_button(*locators_ns["NUMBER_INPUT_FIELD"]),  # noqa:E501
        else:
            return True

    def click_dialog_box(self):
        if isinstance(self.actions, AndroidAction):
            self.actions.is_element_displayed(*locators_ns["NUMBER_DIALOG_BOX"])  # noqa:E501
        else:
            return True

    def input_valid_mobilenumber(self, mobile_number):
        if len(mobile_number) == 10 and mobile_number.isdigit():
            for digit in mobile_number:
                self.sendNumberViaKeypad(digit)
                time.sleep(0.5)
        else:
            raise ValueError("Mobile number must be exactly 10 digits and numeric.")  # noqa:E501

    def click_otp_button(self):
        if isinstance(self.actions, AndroidAction):
            self.actions.click_button(*locators_ns["SEND_OTP"])  # noqa:E501
        else:
            return True

    def input_otp(self, OTP_number):
        if len(OTP_number) == 4 and OTP_number.isdigit():
            for digit in OTP_number:
                self.sendOtpViaKeypad(digit)
                time.sleep(0.5)
        else:
            raise ValueError("OTP number must be exactly 4 digits and numeric.")  # noqa:E501

    def login_wotp_button(self):
        if isinstance(self.actions, AndroidAction):
            self.actions.click_button(*locators_ns["INPUT_OTP"])  # noqa:E501
        else:
            return True

    def navto_shop(self):
        if isinstance(self.actions, AndroidAction):
            self.actions.is_element_displayed(*locators_ns["SHOP_BUTTON"])
            self.actions.click_button(*locators_ns["SHOP_BUTTON"])  # noqa:E501