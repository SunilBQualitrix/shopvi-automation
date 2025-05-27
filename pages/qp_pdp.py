import time
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from utils.custom_logger import allureLogs
from pages.actions.android_actions import AndroidActions


locators_qp = {
    "QP_FASHION": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("fashion")'),  # noqa:E501
    "QP_FOOD": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("food")'),  # noqa:E501
    "QP_GROCERIES": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("groceries")'),  # noqa:E501
    "QP_TRAVEL": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("travel")'),  # noqa:E501
    "QP_ENTERTAINMENT": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("entertainment")'),  # noqa:E501

    "QP_PRODUCT1": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(6)'),  # noqa:E501

}


class QuickPurchase(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = AndroidActions(driver)
