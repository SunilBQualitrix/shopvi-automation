import time
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

locators_ns = {
    "USB_DEBUGGING_POPUP": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("attention")'),
    "USB_DEBUGGING_CHECKBOX": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(1)'),
    "PROCEED_BUTTON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("proceed")'),
    "NUMBER_INPUT_FIELD": (AppiumBy.XPATH, '//android.widget.TextView[@text="enter mobile number"]'),
    "NUMBER_DIALOG_BOX_HEADER": (AppiumBy.ID, "com.google.android.gms:id/credentials_hint_picker_title"),
    "NUMBER_DIALOG_BOX_CANCEL": (AppiumBy.ID, 'com.google.android.gms:id/cancel'),
    "NUMBER_INPUT": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("{number}")'),
    "SEND_OTP": (AppiumBy.XPATH, '//android.widget.TextView[@text="send OTP"]'),
    "INPUT_OTP": (AppiumBy.XPATH, '//android.widget.TextView[@text="login with OTP"]'),
    "SHOP_BUTTON": (AppiumBy.XPATH, '//android.widget.TextView[@text="shop"]')
}


class NavtoShop(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_number_input_field(self):
        Usb_debugging_popup = self.actions.is_element_displayed(*locators_ns["USB_DEBUGGING_POPUP"])
        if Usb_debugging_popup:
            print("USB Debugging Popup is displayed")
            self.actions.click_button(*locators_ns["USB_DEBUGGING_CHECKBOX"])
            self.actions.click_button(*locators_ns["PROCEED_BUTTON"])
        mobile_num_input = self.actions.is_element_displayed(*locators_ns["NUMBER_INPUT_FIELD"])
        if mobile_num_input:
            self.actions.click_button(*locators_ns["NUMBER_INPUT_FIELD"])
            return True
        else:
            return False

    def click_dialog_box(self):
        Dialog_box_header = self.actions.is_element_displayed(*locators_ns["NUMBER_DIALOG_BOX_HEADER"])
        if Dialog_box_header:
            self.actions.click_button(*locators_ns["NUMBER_DIALOG_BOX_CANCEL"])
        else:
            print("Number Dialog Box is not displayed")

    def input_valid_mobilenumber(self, mobile_number):
        by, value = locators_ns["NUMBER_INPUT"]
        for num in mobile_number:
            format_value = value.format(number=num)
            self.actions.click_button(by, format_value)

    def click_otp_button(self):
        self.actions.click_button(*locators_ns["SEND_OTP"])

    def input_otp(self, OTP_number):
        by, value = locators_ns["NUMBER_INPUT"]
        for num in OTP_number:
            format_value = value.format(number=num)
            self.actions.click_button(by, format_value)

    def login_wotp_button(self):
        self.actions.click_button(*locators_ns["INPUT_OTP"])

    def navto_shop(self):
        self.actions.is_element_displayed(*locators_ns["SHOP_BUTTON"])
        self.actions.click_button(*locators_ns["SHOP_BUTTON"])
