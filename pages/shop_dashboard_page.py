import time
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

locators_sd = {
    "SHOP_BY_CATEGORY": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("shop by category")'),
    "EXPLORE_TAB": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("explore")'),
    "DEALS_TAB": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("deals")'),
    "MY_ORDERS_TAB": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("my orders")'),
    "VI_SHOP_ICON": (AppiumBy.XPATH, '//android.widget.TextView[@text="shop"]'),
    "VI_APP_HOME_BUTTON": (AppiumBy.XPATH, '//android.widget.TextView[@text="home"]'),

    "MY_ORDER_P": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(1)'),
    "ACCOUNT_ICON": (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="DS_SHOPshop-account-icon.webp"]'),
    "SEARCH_ICON": (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png"]'),
    "CART_ICON": (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="DS_SHOP_https://vishop.myvi.in/documents/35161/38258/Cart.webp"]'),
    "ACCOUNTS_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(0)'),
    "CART_ICON1": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(2)'),
    "DEALS_PAGE_TITLE": (AppiumBy.XPATH, '//android.widget.TextView[@text="offers"]'),
    "DEALS_BACK_BUTTON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/back-arrow.webp")'),
    "EXPLORE_PAGE_TITLE": (AppiumBy.XPATH, '//android.widget.TextView[@text="our store"]'),
    "EXPLORE_CART_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/Cart.webp")'),
    "EXPLORE_SEARCH_ICON": (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png"]'),
    "EXPLORE_CC_MENU": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(2)'),
    "EXPLORE_MOVIES_MENU": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(3)'),
    "EXPLORE_FOOD_MENU": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(4)'),
    "EXPLORE_SHOPPING_MENU": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(5)'),
    "EXPLORE_TRAVEL_MENU": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(6)'),
    "MYORDERS_BACK_ARROW": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/back-arrow.webp")'),
    "MYORDERS_PAGE_TITLE": (AppiumBy.XPATH, '//android.widget.TextView[@text="my orders"]'),
    "MYORDERS_SEARCH_ICON": (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png"]'),
    "MYORDERS_SEARCH_BOX": (AppiumBy.XPATH, '//android.widget.EditText[@text="search for orders..."]'),


}




class ShopDashboardPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_on_shop_icon(self):
        self.actions.is_element_displayed(*locators_sd["VI_SHOP_ICON"])
        self.actions.click_button(*locators_sd["VI_SHOP_ICON"])
        time.sleep(2)

    def verify_shop_dashborad_page(self):
        return self.actions.is_element_displayed(*locators_sd["SHOP_BY_CATEGORY"])

    def verify_all_items_on_shop_dashboard(self):
        locators = {
            "VI App Home Button": [locators_sd["VI_APP_HOME_BUTTON"]],
            "Deals": [locators_sd["DEALS_TAB"]],
            "Explore": [locators_sd["EXPLORE_TAB"]],
            "My Orders": [locators_sd["MY_ORDERS_TAB"], locators_sd["MY_ORDER_P"]],
            "Vi Shop Home": [locators_sd["VI_SHOP_ICON"]],
            "Accounts Icon": [locators_sd["ACCOUNT_ICON"], locators_sd["ACCOUNTS_ICON"]],
            "Search Icon": [locators_sd["SEARCH_ICON"]],
            "Cart Icon": [locators_sd["CART_ICON"],locators_sd["CART_ICON1"]],
        }
        for element_name, locator_list in locators.items():
            element_found = False
            for locator in locator_list:
                if self.actions.is_element_displayed(*locator):
                    print(f"{element_name}: Displayed (Locator: {locator})")
                    element_found = True
                    break
            if not element_found:
                print(f"{element_name}: Not Displayed")


    def navigate_to_deals_tab(self):
        self.actions.click_button(*locators_sd["DEALS_TAB"])
        time.sleep(2)

    def verify_all_items_on_deals_tab(self):
        locators = {
            "DEALS Page Title": [locators_sd["DEALS_PAGE_TITLE"]],
            "DEALS Back Button": [locators_sd["DEALS_BACK_BUTTON"]],
            "DEALS Cart Icon": [locators_sd["CART_ICON"]],
        }
        for element_name, locator_list in locators.items():
            element_found = False
            for locator in locator_list:
                if self.actions.is_element_displayed(*locator):
                    print(f"{element_name}: Displayed (Locator: {locator})")
                    element_found = True
                    break
            if not element_found:
                print(f"{element_name}: Not Displayed")

    def navigate_to_explore_tab(self):
        self.actions.click_button(*locators_sd["EXPLORE_TAB"])
        time.sleep(2)

    def verify_all_items_on_explore_tab(self):
        locators = {
            "EXPLORE Page Title": [locators_sd["EXPLORE_PAGE_TITLE"]],
            "EXPLORE Search Icon": [locators_sd["EXPLORE_SEARCH_ICON"]],
            "EXPLORE Cart Icon": [locators_sd["EXPLORE_CART_ICON"]],
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
                    print(f"{element_name}: Displayed (Locator: {locator})")
                    element_found = True
                    break
            if not element_found:
                print(f"{element_name}: Not Displayed")

    def navigate_to_my_orders_tab(self):
        self.actions.click_button(*locators_sd["MY_ORDERS_TAB"])
        time.sleep(2)

    def verify_all_items_on_my_orders_tab(self):
        locators = {
            "MY ORDERS Page Title": [locators_sd["MYORDERS_PAGE_TITLE"]],
            "MY ORDERS Search Icon": [locators_sd["MYORDERS_SEARCH_ICON"]],
            "MY ORDERS Back Arrow": [locators_sd["MYORDERS_BACK_ARROW"]],
            "MY ORDERS Search BOX": [locators_sd["MYORDERS_SEARCH_BOX"]],
        }
        for element_name, locator_list in locators.items():
            element_found = False
            for locator in locator_list:
                if self.actions.is_element_displayed(*locator):
                    print(f"{element_name}: Displayed (Locator: {locator})")
                    element_found = True
                    break
            if not element_found:
                print(f"{element_name}: Not Displayed")