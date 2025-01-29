import time
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from utils.custom_logger import custom_logger, allureLogs
from pages.actions.android_actions import AndroidActions

locators = {
    "SEARCH_ICON": (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png"]'),
    "SEARCH_INPUT_FIELD": (AppiumBy.CLASS_NAME, 'android.widget.EditText'),
    "NO_SEARCH_RESULTS": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Looks like there is no relevant products to your search.")'),
    "FLIPKART_SEARCH_RESULTS": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Flipkart Shopping")'),
    "AMAZON_SEARCH_RESULTS": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Amazon Shopping")'),
    "SEARCH_RESULTS_FLIPKART": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Flipkart Shopping Voucher")'),
}

class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = AndroidActions(driver)


    def verify_search_icon(self):
        searchicon=self.actions.is_element_displayed(*locators["SEARCH_ICON"])
        allureLogs("Search Icon is displayed")
        self.actions.screenshotAttachment("Search Icon is displayed")
        return searchicon
    
    def click_search_icon(self):
        self.actions.click_button(*locators["SEARCH_ICON"])
        allureLogs("Search Icon Is clicked")
        self.actions.screenshotAttachment("Search Icon Is clicked")

    def enter_search_input(self, search_text):
        self.actions.enter_text(*locators["SEARCH_INPUT_FIELD"], search_text)
        allureLogs(f"Entered search text: {search_text}")
        self.actions.screenshotAttachment(f"Entered search text: {search_text}")
