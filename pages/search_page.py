
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from utils.custom_logger import allureLogs
from pages.actions.android_actions import AndroidActions

locators = {
    "SEARCH_ICON": (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png"]'),     # noqa:E501
    "SEARCH_INPUT_FIELD": (AppiumBy.CLASS_NAME, 'android.widget.EditText'),
    "NO_SEARCH_RESULTS": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Looks like there is no relevant products to your search.")'),   # noqa:E501
    "FLIPKART_SEARCH_RESULTS": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Flipkart Shopping")'),    # noqa:E501
    "AMAZON_SEARCH_RESULTS": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Amazon Shopping")'),    # noqa:E501
    "SEARCH_RESULTS_FLIPKART": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Flipkart Shopping Voucher")'),    # noqa:E501
    "SEARCH_ICON1": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(1)'),     # noqa:E501
}


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = AndroidActions(driver)

    def verify_search_icon(self):
        """
        Verify that the search icon is displayed by checking multiple locators.
        Returns True if found, otherwise False.
        """
        locators_list = [locators["SEARCH_ICON"], locators["SEARCH_ICON1"]]    # noqa:E501
        for locator in locators_list:
            if self.actions.is_element_displayed(*locator):
                allureLogs("Search Icon found")
                self.actions.screenshotAttachment("Search Icon found")
                return True
        allureLogs("Search Icon not found with any locator")
        self.actions.screenshotAttachment("Search Icon not found")
        return False

    def click_search_icon(self):
        """
        Click the search icon using the first available locator.
        Returns True after a successful click; otherwise, False.
        """
        locators_list = [locators["SEARCH_ICON"], locators["SEARCH_ICON1"]]
        for locator in locators_list:
            if self.actions.is_element_displayed(*locator):
                self.actions.click_button(*locator)
                allureLogs("Search Icon clicked")
                self.actions.screenshotAttachment("Search Icon clicked")
                return True
        allureLogs("Search Icon not found to click")
        self.actions.screenshotAttachment("Search Icon not clickable")
        return False

    def enter_search_input(self, search_text):
        self.actions.enter_text(*locators["SEARCH_INPUT_FIELD"], search_text)
        allureLogs(f"Entered search text: {search_text}")
        self.actions.screenshotAttachment(f"Entered search text: {search_text}")      # noqa:E501

    def verify_click_search(self):
        flipkart_results = self.actions.wait_for_elements(*locators['SEARCH_RESULTS_FLIPKART'])      # noqa:E501
        flipkart_results[0].click()
        self.actions.screenshotAttachment("Navigated to search results page")
