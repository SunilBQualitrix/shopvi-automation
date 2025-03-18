import time
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from utils.custom_logger import allureLogs
from pages.actions.android_actions import AndroidActions

locators_sd = {
    "SHOP_BY_CATEGORY": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("shop by category")'),      # noqa:E501
    "EXPLORE_TAB": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("explore")'),    # noqa:E501
    "DEALS_TAB": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("deals")'),  # noqa:E501
    "MY_ORDERS_TAB": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("my orders")'),  # noqa:E501
    "VI_SHOP_ICON": (AppiumBy.XPATH, '//android.widget.TextView[@text="shop"]'),    # noqa:E501
    "VI_APP_HOME_BUTTON": (AppiumBy.XPATH, '//android.widget.TextView[@text="home"]'),  # noqa:E501
    "DB_SEARCH_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(1)'),  # noqa:E501

    "MY_ORDER_P": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(1)'),  # noqa:E501
    "ACCOUNT_ICON": (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="DS_SHOPshop-account-icon.webp"]'),    # noqa:E501
    "SEARCH_ICON": (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png"]'),   # noqa:E501
    "CART_ICON": (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="DS_SHOP_https://vishop.myvi.in/documents/35161/38258/Cart.webp"]'),  # noqa:E501
    "ACCOUNTS_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(0)'),  # noqa:E501
    "CART_ICON1": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(2)'),     # noqa:E501
    "DEALS_PAGE_TITLE": (AppiumBy.XPATH, '//android.widget.TextView[@text="offers"]'),  # noqa:E501
    "DEALS_BACK_BUTTON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/back-arrow.webp")'),    # noqa:E501
    "DEALS_BACK_BUTTON1": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(1)'),  # noqa:E501
    "DEALS_CART_ICON1": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(2)'),  # noqa:E501


    "EXPLORE_PAGE_TITLE": (AppiumBy.XPATH, '//android.widget.TextView[@text="our store"]'),     # noqa:E501
    "EXPLORE_CART_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/Cart.webp")'),  # noqa:E501
    "EXPLORE_SEARCH_ICON": (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png"]'),   # noqa:E501
    "EXPLORE_CC_MENU": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(2)'),    # noqa:E501
    "EXPLORE_MOVIES_MENU": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(3)'),    # noqa:E501
    "EXPLORE_FOOD_MENU": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(4)'),  # noqa:E501
    "EXPLORE_SHOPPING_MENU": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(5)'),  # noqa:E501
    "EXPLORE_TRAVEL_MENU": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(6)'),    # noqa:E501
    "EXPLORE_SEARCH_ICON1": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(0)'),  # noqa:E501
    "EXPLORE_CART_ICON1": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(1)'),  # noqa:E501

    "MYORDERS_BACK_ARROW": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/back-arrow.webp")'),  # noqa:E501
    "MYORDERS_PAGE_TITLE": (AppiumBy.XPATH, '//android.widget.TextView[@text="my orders"]'),    # noqa:E501
    "MYORDERS_SEARCH_ICON": (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png"]'),  # noqa:E501
    "MYORDERS_SEARCH_BOX": (AppiumBy.XPATH, '//android.widget.EditText[@text="search for orders..."]'),     # noqa:E501
    "MYORDERS_BACK_ARROW1": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(0)'),  # noqa:E501
    "MYORDERS_SEARCH_ICON1": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(1)'),  # noqa:E501


}


class ShopDashboardPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = AndroidActions(driver)

    def click_on_shop_icon(self):
        self.actions.is_element_displayed(*locators_sd["VI_SHOP_ICON"])
        allureLogs("Clicking on Shop Icon")
        self.actions.click_button(*locators_sd["VI_SHOP_ICON"])
        allureLogs("Clicked on Shop Icon")
        self.actions.screenshotAttachment("Shop Dashboard Page")
        time.sleep(2)

    def verify_shop_dashborad_page(self):   # this method is used only to verify the user is on shop dashboard page   # noqa:E501
        onshop = self.actions.is_element_displayed(*locators_sd["SHOP_BY_CATEGORY"])    # noqa:E501
        allureLogs("Shop Dashboard Page is displayed")
        return onshop

    def verify_all_items_on_shop_dashboard(self):
        allureLogs("Verifying all items on Shop Dashboard Page")
        locators = {
            "VI App Home Button": [locators_sd["VI_APP_HOME_BUTTON"]],
            "Deals": [locators_sd["DEALS_TAB"]],
            "Explore": [locators_sd["EXPLORE_TAB"]],
            "My Orders": [locators_sd["MY_ORDERS_TAB"], locators_sd["MY_ORDER_P"]],     # noqa:E501
            "Vi Shop Home": [locators_sd["VI_SHOP_ICON"]],
            "Accounts Icon": [locators_sd["ACCOUNT_ICON"], locators_sd["ACCOUNTS_ICON"]],   # noqa:E501
            "Search Icon": [locators_sd["SEARCH_ICON"], locators_sd["DB_SEARCH_ICON"]],    # noqa:E501
            "Cart Icon": [locators_sd["CART_ICON"], locators_sd["CART_ICON1"]],  # noqa:E501
        }
        for element_name, locator_list in locators.items():
            element_found = False
            for locator in locator_list:
                if self.actions.is_element_displayed(*locator):
                    element = self.driver.find_element(*locator)
                    value = element.text.strip() if element.text else "No Text"
                    allureLogs(f"Element {element_name} is DISPLAYED | [Value: {value}]")   # noqa:E501
                    element_found = True
                    break
            if not element_found:
                allureLogs(f"Element {element_name} is NOT DISPLAYED")
                self.actions.screenshotAttachment(f"{element_name}: NOT DISPLAYED")   # noqa:E501
        self.actions.screenshotAttachment("Verified All items on Shop Dashboard Page")  # noqa:E501

    def navigate_to_deals_tab(self):
        self.actions.click_button(*locators_sd["DEALS_TAB"])
        allureLogs("Navigated to Deals Tab")
        self.actions.screenshotAttachment("Navigated to Deals Tab")
        time.sleep(2)

    def verify_all_items_on_deals_tab(self):
        allureLogs("Verifying all items on Deals Tab")
        locators = {
            "DEALS Page Title": [locators_sd["DEALS_PAGE_TITLE"], locators_sd["DEALS_BACK_BUTTON1"]],  # noqa:E501
            "DEALS Back Button": [locators_sd["DEALS_BACK_BUTTON"]],
            "DEALS Cart Icon": [locators_sd["CART_ICON"], locators_sd["DEALS_CART_ICON1"]],  # noqa:E501
        }
        for element_name, locator_list in locators.items():
            element_found = False
            for locator in locator_list:
                if self.actions.is_element_displayed(*locator):
                    element = self.driver.find_element(*locator)
                    value = element.text.strip() if element.text else "No Text"
                    allureLogs(f"Element {element_name} is DISPLAYED | [Value: {value}]")     # noqa:E501
                    element_found = True
                    break
            if not element_found:
                allureLogs(f"Element {element_name} is NOT DISPLAYED")
                self.actions.screenshotAttachment(f"{element_name}: NOT DISPLAYED")  # noqa:E501
        self.actions.screenshotAttachment("Verified All items on Deals TAB")

    def navigate_to_explore_tab(self):
        self.actions.click_button(*locators_sd["EXPLORE_TAB"])
        allureLogs("Navigated to Explore Tab")
        self.actions.screenshotAttachment("Navigated to Explore Tab")
        time.sleep(2)

    def verify_all_items_on_explore_tab(self):
        allureLogs("Verifying all items on Explore Tab")
        locators = {
            "EXPLORE Page Title": [locators_sd["EXPLORE_PAGE_TITLE"]],
            "EXPLORE Search Icon": [locators_sd["EXPLORE_SEARCH_ICON"], locators_sd["EXPLORE_SEARCH_ICON1"]],  # noqa:E501
            "EXPLORE Cart Icon": [locators_sd["EXPLORE_CART_ICON"], locators_sd["EXPLORE_CART_ICON1"]],  # noqa:E501
            "EXPLORE CC Menu": [locators_sd["EXPLORE_CC_MENU"]],
            "EXPLORE Movies Menu": [locators_sd["EXPLORE_MOVIES_MENU"]],
            "EXPLORE Food Menu": [locators_sd["EXPLORE_FOOD_MENU"]],
            "EXPLORE Shopping Menu": [locators_sd["EXPLORE_SHOPPING_MENU"]],
            "EXPLORE Travel Menu": [locators_sd["EXPLORE_TRAVEL_MENU"]],
        }
        for element_name, locator_list in locators.items():
            element_found = False
            for locator in locator_list:
                if self.actions.is_element_displayed(*locator):
                    element = self.driver.find_element(*locator)
                    value = element.text.strip() if element.text else "No Text"
                    allureLogs(f"Element {element_name} is DISPLAYED | [Value: {value}]")   # noqa:E501
                    element_found = True
                    break
            if not element_found:
                allureLogs(f"Element {element_name} is NOT DISPLAYED")
                self.actions.screenshotAttachment(f"{element_name}: NOT DISPLAYED")     # noqa:E501
        self.actions.screenshotAttachment("Verified All items on Explore TAB")

    def navigate_to_my_orders_tab(self):
        self.actions.click_button(*locators_sd["MY_ORDERS_TAB"])
        allureLogs("Navigated to My Orders Tab")
        self.actions.screenshotAttachment("Navigated to My Orders Tab")
        time.sleep(2)

    def verify_all_items_on_my_orders_tab(self):
        allureLogs("Verifying all items on My Orders Tab")
        locators = {
            "MY ORDERS Page Title": [locators_sd["MYORDERS_PAGE_TITLE"]],
            "MY ORDERS Search Icon": [locators_sd["MYORDERS_SEARCH_ICON"]],
            "MY ORDERS Back Arrow": [locators_sd["MYORDERS_BACK_ARROW"], locators_sd["MYORDERS_BACK_ARROW1"]],  # noqa:E501
            "MY ORDERS Search BOX": [locators_sd["MYORDERS_SEARCH_BOX"], locators_sd["MYORDERS_SEARCH_ICON1"]],  # noqa:E501
        }
        for element_name, locator_list in locators.items():
            element_found = False
            for locator in locator_list:
                if self.actions.is_element_displayed(*locator):
                    element = self.driver.find_element(*locator)
                    value = element.text.strip() if element.text else "No Text"
                    allureLogs(f"Element {element_name} is DISPLAYED | (Value: {value})")   # noqa:E501
                    element_found = True
                    break
            if not element_found:
                allureLogs(f"Element {element_name} is NOT DISPLAYED")
                self.actions.screenshotAttachment(f"{element_name}: NOT DISPLAYED")  # noqa:E501
        self.actions.screenshotAttachment("Verified All items on MY Orders TAB")    # noqa:E501
