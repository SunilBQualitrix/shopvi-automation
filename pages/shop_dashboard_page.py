import time
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from utils.custom_logger import allureLogs
from pages.actions.android_actions import AndroidActions

locators_sd = {
    "SHOP_BY_CATEGORY": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("shop by category")'),      # noqa:E501
    "CATEGORIES_TAB": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("categories")'),    # noqa:E501
    "DEALS_TAB": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("deals")'),  # noqa:E501
    "MY_ORDERS_TAB": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("my orders")'),  # noqa:E501
    "VI_SHOP_ICON": (AppiumBy.XPATH, '//android.widget.TextView[@text="shop"]'),    # noqa:E501
    "VI_APP_HOME_BUTTON": (AppiumBy.XPATH, '//android.widget.TextView[@text="home"]'),  # noqa:E501
    "DB_SEARCH_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png")'),  # noqa:E501
    "DB_ACCOUNTS_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOPshop-account-icon.webp")'),  # noqa:E501
    "DB_CART_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/Cart.webp")'),  # noqa:E501

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


    "CATEGORIES_PAGE_TITLE": (AppiumBy.XPATH, '//android.widget.TextView[@text="our store"]'),     # noqa:E501
    "CATEGORIES_CART_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/Cart.webp")'),  # noqa:E501
    "CATEGORIES_SEARCH_ICON": (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png"]'),   # noqa:E501
    "CATEGORIES_CC_MENU": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(2)'),    # noqa:E501
    "CATEGORIES_MOVIES_MENU": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(3)'),    # noqa:E501
    "CATEGORIES_FOOD_MENU": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(4)'),  # noqa:E501
    "CATEGORIES_SHOPPING_MENU": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(5)'),  # noqa:E501
    "CATEGORIES_TRAVEL_MENU": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(6)'),    # noqa:E501
    "CATEGORIES_SEARCH_ICON1": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(0)'),  # noqa:E501
    "CATEGORIES_CART_ICON1": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(1)'),  # noqa:E501

    "MYORDERS_BACK_ARROW": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/back-arrow.webp")'),  # noqa:E501
    "MYORDERS_PAGE_TITLE": (AppiumBy.XPATH, '//android.widget.TextView[@text="my orders"]'),    # noqa:E501
    "MYORDERS_SEARCH_ICON": (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png"]'),  # noqa:E501
    "MYORDERS_SEARCH_BOX": (AppiumBy.XPATH, '//android.widget.EditText[@text="search for orders..."]'),     # noqa:E501
    "MYORDERS_BACK_ARROW1": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(0)'),  # noqa:E501
    "MYORDERS_SEARCH_ICON1": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(1)'),  # noqa:E501

    "QP_FASHION": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("fashion")'),  # noqa:E501
    "QP_FOOD": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("food")'),  # noqa:E501
    "QP_GROCERIES": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("groceries")'),  # noqa:E501
    "QP_TRAVEL": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("travel")'),  # noqa:E501
    "QP_ENTERTAINMENT": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("entertainment")'),  # noqa:E501

    "QP_PRODUCT1": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(6)'),  # noqa:E501

    "TRAVEL_PAGE_TITLE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("travel")'),  # noqa:E501
    "TRAVEL_PAGE_BACK_BUTTON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/back-arrow.webp")'),  # noqa:E501
    "TRAVEL_PAGE_SEARCH_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png")'),  # noqa:E501
    "TRAVEL_PAGE_CART_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/Cart.webp")'),  # noqa:E501
    "TRAVEL_CABS": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("cabs")'),  # noqa:E501
    "TRAVEL_FLIGHTS": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("flights")'),  # noqa:E501
    "TRAVEL_HOTELS": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("hotels")'),  # noqa:E501
    "TRAVEL_EXPERIENCES": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("experiences")'),  # noqa:E501

    "TRAVEL_CABS_PAGE_TITLE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("cabs")'),  # noqa:E501
    "TRAVEL_CABS_BACK_BUTTON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/back-arrow.webp")'),  # noqa:E501
    "TRAVEL_CABS_SEARCH_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png")'),  # noqa:E501
    "TRAVEL_CABS_CART_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/Cart.webp")'),  # noqa:E501
    "TRAVEL_CABS_NO_OF_PRODUCTS": (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "products")]'),   # noqa:E501

    "TRAVEL_EXPERIENCES_PAGE_TITLE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("experiences")'),  # noqa:E501
    "TRAVEL_EXPERIENCES_BACK_BUTTON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/back-arrow.webp")'),  # noqa:E501
    "TRAVEL_EXPERIENCES_SEARCH_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png")'),  # noqa:E501
    "TRAVEL_EXPERIENCES_CART_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/Cart.webp")'),  # noqa:E501
    "TRAVEL_EXPERIENCES_NO_OF_PRODUCTS": (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "products")]'),   # noqa:E501

    "TRAVEL_FLIGHTS_PAGE_TITLE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("flights")'),  # noqa:E501
    "TRAVEL_FLIGHTS_BACK_BUTTON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/back-arrow.webp")'),  # noqa:E501
    "TRAVEL_FLIGHTS_SEARCH_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png")'),  # noqa:E501
    "TRAVEL_FLIGHTS_CART_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/Cart.webp")'),  # noqa:E501
    "TRAVEL_FLIGHTS_NO_OF_PRODUCTS": (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "products")]'),   # noqa:E501

    "TRAVEL_HOTELS_PAGE_TITLE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("hotels")'),  # noqa:E501
    "TRAVEL_HOTELS_BACK_BUTTON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/back-arrow.webp")'),  # noqa:E501
    "TRAVEL_HOTELS_SEARCH_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png")'),  # noqa:E501
    "TRAVEL_HOTELS_CART_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/Cart.webp")'),  # noqa:E501
    "TRAVEL_HOTELS_NO_OF_PRODUCTS": (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "products")]'),   # noqa:E501

    "MOVIES_PAGE_TITLE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("entertainment")'),  # noqa:E501
    "MOVIES_BACK_BUTTON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/back-arrow.webp")'),  # noqa:E501
    "MOVIES_SEARCH_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png")'),  # noqa:E501
    "MOVIES_CART_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/Cart.webp")'),  # noqa:E501
    "MOVIES_MOVIES": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("movies")'),  # noqa:E501
    "MOVIES_OTT": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ott")'),  # noqa:E501

    "MOVIES_MOVIES_PAGE_TITLE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("movies")'),  # noqa:E501
    "MOVIES_MOVIES_BACK_BUTTON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/back-arrow.webp")'),  # noqa:E501
    "MOVIES_MOVIES_SEARCH_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png")'),  # noqa:E501
    "MOVIES_MOVIES_CART_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/Cart.webp")'),  # noqa:E501
    "MOVIES_MOVIES_NO_OF_PRODUCTS": (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "products")]'),   # noqa:E501

    "MOVIES_OTT_PAGE_TITLE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ott")'),  # noqa:E501
    "MOVIES_OTT_BACK_BUTTON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/back-arrow.webp")'),  # noqa:E501
    "MOVIES_OTT_SEARCH_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png")'),  # noqa:E501
    "MOVIES_OTT_CART_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/Cart.webp")'),  # noqa:E501
    "MOVIES_OTT_NO_OF_PRODUCTS": (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "products")]'),   # noqa:E501

    "FOOD_PAGE_TITLE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("food")'),  # noqa:E501
    "FOOD_BACK_BUTTON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/back-arrow.webp")'),  # noqa:E501
    "FOOD_SEARCH_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png")'),  # noqa:E501
    "FOOD_CART_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/Cart.webp")'),  # noqa:E501
    "FOOD_DINING": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("dining")'),  # noqa:E501
    "FOOD_GROCERIES": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("groceries")'),  # noqa:E501

    "FOOD_DINING_PAGE_TITLE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("dining")'),  # noqa:E501
    "FOOD_DINING_BACK_BUTTON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/back-arrow.webp")'),  # noqa:E501
    "FOOD_DINING_SEARCH_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png")'),  # noqa:E501
    "FOOD_DINING_CART_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/Cart.webp")'),  # noqa:E501
    "FOOD_DINING_NO_OF_PRODUCTS": (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "products")]'),   # noqa:E501

    "FOOD_GROCERIES_PAGE_TITLE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("groceries")'),  # noqa:E501
    "FOOD_GROCERIES_BACK_BUTTON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/back-arrow.webp")'),  # noqa:E501
    "FOOD_GROCERIES_SEARCH_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png")'),  # noqa:E501
    "FOOD_GROCERIES_CART_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/Cart.webp")'),  # noqa:E501
    "FOOD_GROCERIES_NO_OF_PRODUCTS": (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "products")]'),   # noqa:E501

    "SHOPPING_PAGE_TITLE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("shopping")'),  # noqa:E501
    "SHOPPING_BACK_BUTTON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/back-arrow.webp")'),  # noqa:E501
    "SHOPPING_SEARCH_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png")'),  # noqa:E501
    "SHOPPING_CART_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/Cart.webp")'),  # noqa:E501
    "SHOPPING_AMAZON_EGIFT": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("amazon pay e-gift card")'),   # noqa:E501
    "SHOPPING_AMAZON_SHOPPING": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("amazon shopping voucher")'),  # noqa:E501
    "SHOPPING_FASHION_ACCESSORIES": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("fashion & accessories")'),  # noqa:E501
    "SHOPPING_FLIPKART": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("flipkart")'),  # noqa:E501
    "SHOPPING_GIFTING": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("gifting")'),  # noqa:E501
    "SHOPPING_JEWELLERY": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("jewellery")'),  # noqa:E501

    "SHOPPING_AMAZON_EGIFT_PAGE_TITLE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("amazon pay e-gift card")'),  # noqa:E501
    "SHOPPING_AMAZON_EGIFT_BACK_BUTTON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/back-arrow.webp")'),  # noqa:E501
    "SHOPPING_AMAZON_EGIFT_SEARCH_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png")'),  # noqa:E501
    "SHOPPING_AMAZON_EGIFT_CART_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/Cart.webp")'),  # noqa:E501
    "SHOPPING_AMAZON_EGIFT_NO_OF_PRODUCTS": (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "products")]'),   # noqa:E501

    "SHOPPING_AMAZON_SHOPPING_PAGE_TITLE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("amazon shopping voucher")'),  # noqa:E501
    "SHOPPING_AMAZON_SHOPPING_PAGE_BACK_BUTTON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/back-arrow.webp")'),  # noqa:E501
    "SHOPPING_AMAZON_SHOPPING_PAGE_SEARCH_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png")'),  # noqa:E501
    "SHOPPING_AMAZON_SHOPPING_PAGE_CART_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/Cart.webp")'),  # noqa:E501
    "SHOPPING_AMAZON_SHOPPING_PAGE_NO_OF_PRODUCTS": (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "products")]'),   # noqa:E501

    "SHOPPING_FASHION_ACCESSORIES_PAGE_TITLE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("fashion & accessories")'),  # noqa:E501
    "SHOPPING_FASHION_ACCESSORIES_BACK_BUTTON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/back-arrow.webp")'),  # noqa:E501
    "SHOPPING_FASHION_ACCESSORIES_SEARCH_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png")'),  # noqa:E501
    "SHOPPING_FASHION_ACCESSORIES_CART_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/Cart.webp")'),  # noqa:E501
    "SHOPPING_FASHION_ACCESSORIES_NO_OF_PRODUCTS": (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "products")]'),   # noqa:E501

    "SHOPPING_FLIPKART_PAGE_TITLE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("flipkart")'),  # noqa:E501
    "SHOPPING_FLIPKART_BACK_BUTTON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/back-arrow.webp")'),  # noqa:E501
    "SHOPPING_FLIPKART_SEARCH_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png")'),  # noqa:E501
    "SHOPPING_FLIPKART_CART_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/Cart.webp")'),  # noqa:E501
    "SHOPPING_FLIPKART_NO_OF_PRODUCTS": (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "products")]'),   # noqa:E501

    "SHOPPING_GIFTING_PAGE_TITLE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("gifting")'),  # noqa:E501
    "SHOPPING_GIFTING_BACK_BUTTON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/back-arrow.webp")'),  # noqa:E501
    "SHOPPING_GIFTING_SEARCH_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png")'),  # noqa:E501
    "SHOPPING_GIFTING_CART_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/Cart.webp")'),  # noqa:E501
    "SHOPPING_GIFTING_NO_OF_PRODUCTS": (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "products")]'),   # noqa:E501

    "SHOPPING_JEWELLERY_PAGE_TITLE": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("jewellery")'),  # noqa:E501
    "SHOPPING_JEWELLERY_BACK_BUTTON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/back-arrow.webp")'),  # noqa:E501
    "SHOPPING_JEWELLERY_SEARCH_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/search.png")'),  # noqa:E501
    "SHOPPING_JEWELLERY_CART_ICON": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("DS_SHOP_https://vishop.myvi.in/documents/35161/38258/Cart.webp")'),  # noqa:E501
    "SHOPPING_JEWELLERY_NO_OF_PRODUCTS": (AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "products")]'),   # noqa:E501

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

    def verify_shop_dashboard_page(self):
        # Define the elements to verify
        dashboard_elements = [
            locators_sd["DB_ACCOUNTS_ICON"],
            locators_sd["VI_APP_HOME_BUTTON"],
            locators_sd["VI_SHOP_ICON"],
            locators_sd["MY_ORDERS_TAB"],
        ]
        # Check if all elements are displayed
        all_elements_displayed = True
        for element in dashboard_elements:
            is_displayed = self.actions.is_element_displayed(*element)
            if not is_displayed:
                all_elements_displayed = False
                allureLogs(f"Element {element} not found on Shop Dashboard Page")     # noqa:E501
                break
        if all_elements_displayed:
            allureLogs("User is on Vi Shop DashBoard Page now ✅")     # noqa:E501
        else:
            allureLogs("User fails to navigate to Vi Shop DashBoard Page ❌")      # noqa:E501
        return all_elements_displayed

    def verify_quick_purchase_items_on_Shop_dashboard(self):
        allureLogs("Verifying Quick Purchase items on Shop Dashboard Page")
        locators = {
            "QP_FASHION": [locators_sd["QP_FASHION"]],
            "QP_FOOD": [locators_sd["QP_FOOD"]],
            "QP_GROCERIES": [locators_sd["QP_GROCERIES"]],
            "QP_TRAVEL": [locators_sd["QP_TRAVEL"]],
            "QP_ENTERTAINMENT": [locators_sd["QP_ENTERTAINMENT"]],
            "QP_PRODUCT1": [locators_sd["QP_PRODUCT1"]],
        }
        for element_name, locator_list in locators.items():
            element_found = False
            for locator in locator_list:
                if self.actions.is_element_displayed(*locator):
                    element = self.driver.find_element(*locator)
                    value = element.text.strip() if element.text else "No Text"
                    allureLogs(f"✅ Element {element_name} is DISPLAYED | [Value: {value}]")      # noqa:E501
                    element_found = True
                    break
            if not element_found:
                allureLogs(f"❌ Element {element_name} is NOT DISPLAYED")
                self.actions.screenshotAttachment(f"{element_name}: NOT DISPLAYED")  # noqa:E501
        self.actions.screenshotAttachment("Verified Quick Purchase items on Shop Dashboard Page")  # noqa:E501

    def verify_all_items_on_shop_dashboard(self):
        allureLogs("Verifying all items on Shop Dashboard Page")
        locators = {
            "VI App Home Button": [locators_sd["VI_APP_HOME_BUTTON"]],
            "Deals": [locators_sd["DEALS_TAB"]],
            "Categories": [locators_sd["CATEGORIES_TAB"]],
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
                    allureLogs(f"✅ Element {element_name} is DISPLAYED | [Value: {value}]")   # noqa:E501
                    element_found = True
                    break
            if not element_found:
                allureLogs(f"❌ Element {element_name} is NOT DISPLAYED")
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
            "DEALS Cart Icon": [locators_sd["CART_ICON"], locators_sd["DEALS_CART_ICON1"]],  # noqa:E501
        }
        for element_name, locator_list in locators.items():
            element_found = False
            for locator in locator_list:
                if self.actions.is_element_displayed(*locator):
                    element = self.driver.find_element(*locator)
                    value = element.text.strip() if element.text else "No Text"
                    allureLogs(f"✅ Element {element_name} is DISPLAYED | [Value: {value}]")     # noqa:E501
                    element_found = True
                    break
            if not element_found:
                allureLogs(f"❌ Element {element_name} is NOT DISPLAYED")
                self.actions.screenshotAttachment(f"{element_name}: NOT DISPLAYED")  # noqa:E501
        self.actions.screenshotAttachment("Verified All items on Deals TAB")

    def navigate_to_categories_tab(self):
        self.actions.click_button(*locators_sd["CATEGORIES_TAB"])
        allureLogs("Navigated to Categories Tab")
        self.actions.screenshotAttachment("Navigated to Categories Tab")
        time.sleep(2)

    def verify_all_items_on_categories_tab(self):
        allureLogs("Verifying all items on Explore Tab")
        locators = {
            "Categories Page Title": [locators_sd["CATEGORIES_PAGE_TITLE"]],
            "Categories Search Icon": [locators_sd["CATEGORIES_SEARCH_ICON"], locators_sd["CATEGORIES_SEARCH_ICON1"]],  # noqa:E501
            "Categories Cart Icon": [locators_sd["CATEGORIES_CART_ICON"], locators_sd["CATEGORIES_CART_ICON1"]],  # noqa:E501
            "Categories CC Menu": [locators_sd["CATEGORIES_CC_MENU"]],
            "Categories Movies Menu": [locators_sd["CATEGORIES_MOVIES_MENU"]],
            "Categories Food Menu": [locators_sd["CATEGORIES_FOOD_MENU"]],
            "categories Shopping Menu": [locators_sd["CATEGORIES_SHOPPING_MENU"]],  # noqa:E501
            "Categories Travel Menu": [locators_sd["CATEGORIES_TRAVEL_MENU"]],
        }
        for element_name, locator_list in locators.items():
            element_found = False
            for locator in locator_list:
                if self.actions.is_element_displayed(*locator):
                    element = self.driver.find_element(*locator)
                    value = element.text.strip() if element.text else "No Text"
                    allureLogs(f"✅ Element {element_name} is DISPLAYED | [Value: {value}]")   # noqa:E501
                    element_found = True
                    break
            if not element_found:
                allureLogs(f"❌ Element {element_name} is NOT DISPLAYED")
                self.actions.screenshotAttachment(f"{element_name}: NOT DISPLAYED")     # noqa:E501
        self.actions.screenshotAttachment("Verified All items on Explore TAB")

    def navigate_to_travel_subcategories(self):
        self.actions.click_button(*locators_sd["CATEGORIES_TRAVEL_MENU"])
        allureLogs("Navigated to Travel Sub-Category Tab")
        self.actions.screenshotAttachment("Navigated to Categories Tab")
        time.sleep(2)

    def verify_all_items_on_travel_subcategory(self):
        allureLogs("Verifying all items under Travel Sub-Category Tab")
        locators = {
            "Travel Page Title": [locators_sd["TRAVEL_PAGE_TITLE"]],
            "Travel Search Icon": [locators_sd["TRAVEL_PAGE_SEARCH_ICON"]],
            "Travel Cart Icon": [locators_sd["TRAVEL_PAGE_CART_ICON"]],
            "Travel Cabs": [locators_sd["TRAVEL_CABS"]],
            "Travel Flights": [locators_sd["TRAVEL_FLIGHTS"]],
            "Travel Hotels": [locators_sd["TRAVEL_HOTELS"]],
            "Travel Experiences": [locators_sd["TRAVEL_EXPERIENCES"]],
        }
        for element_name, locator_list in locators.items():
            element_found = False
            for locator in locator_list:
                if self.actions.is_element_displayed(*locator):
                    element = self.driver.find_element(*locator)
                    value = element.text.strip() if element.text else "No Text"
                    allureLogs(f"✅ Element {element_name} is DISPLAYED | [Value: {value}]")   # noqa:E501
                    element_found = True
                    break
            if not element_found:
                allureLogs(f"❌ Element {element_name} is NOT DISPLAYED")
                self.actions.screenshotAttachment(f"{element_name}: NOT DISPLAYED")     # noqa:E501
        self.actions.screenshotAttachment("Verified All items on Travel Sub-Category Tab")  # noqa:E501

    def navigate_to_travel_cabs_subcategories(self):
        self.actions.click_button(*locators_sd["TRAVEL_CABS"])
        allureLogs("Navigated to Cabs Sub-category under Travel Sub-Category Tab")  # noqa:E501
        self.actions.screenshotAttachment("Navigated to Cabs Sub-category under Travel Sub-Category Tab")   # noqa:E501
        time.sleep(2)

    def verify_all_items_on_travel_cabs_subcategory(self):
        allureLogs("Verifying all items on Cabs under Travel Sub-Category Tab")
        locators = {
            "Travel Cabs Page Title": [locators_sd["TRAVEL_CABS_PAGE_TITLE"]],
            "Travel Cabs Back Button": [locators_sd["TRAVEL_CABS_BACK_BUTTON"]],  # noqa:E501
            "Travel Cabs Search Icon": [locators_sd["TRAVEL_CABS_SEARCH_ICON"]],    # noqa:E501
            "Travel Cabs Cart Icon": [locators_sd["TRAVEL_CABS_CART_ICON"]],
            "Travel Cabs No of Products": [locators_sd["TRAVEL_CABS_NO_OF_PRODUCTS"]],  # noqa:E501
        }
        for element_name, locator_list in locators.items():
            element_found = False
            for locator in locator_list:
                if self.actions.is_element_displayed(*locator):
                    element = self.driver.find_element(*locator)
                    value = element.text.strip() if element.text else "No Text"
                    allureLogs(f"✅ Element {element_name} is DISPLAYED | [Value: {value}]")   # noqa:E501
                    element_found = True
                    break
            if not element_found:
                allureLogs(f"❌ Element {element_name} is NOT DISPLAYED")
                self.actions.screenshotAttachment(f"{element_name}: NOT DISPLAYED")     # noqa:E501
        self.actions.screenshotAttachment("Verified All items on cabs under Travel Sub-Category Tab")  # noqa:E501

    def navigate_to_travel_experinces_subcategories(self):
        self.driver.back()
        self.actions.click_button(*locators_sd["TRAVEL_EXPERIENCES"])
        allureLogs("Navigated to Experinces Sub-category under Travel Sub-Category Tab")  # noqa:E501
        self.actions.screenshotAttachment("Navigated to Experinces Sub-category under Travel Sub-Category Tab")   # noqa:E501
        time.sleep(2)

    def verify_all_items_on_travel_experinces_subcategory(self):
        allureLogs("Verifying all items on experinces under Travel Sub-Category Tab")   # noqa:E501
        locators = {
            "Travel Experinces Page Title": [locators_sd["TRAVEL_EXPERIENCES_PAGE_TITLE"]],   # noqa:E501
            "Travel Experinces Back Button": [locators_sd["TRAVEL_EXPERIENCES_BACK_BUTTON"]],  # noqa:E501
            "Travel Experinces Search Icon": [locators_sd["TRAVEL_EXPERIENCES_SEARCH_ICON"]],    # noqa:E501
            "Travel Experinces Cart Icon": [locators_sd["TRAVEL_EXPERIENCES_CART_ICON"]],   # noqa:E501
            "Travel Experinces No of Products": [locators_sd["TRAVEL_EXPERIENCES_NO_OF_PRODUCTS"]],  # noqa:E501
        }
        for element_name, locator_list in locators.items():
            element_found = False
            for locator in locator_list:
                if self.actions.is_element_displayed(*locator):
                    element = self.driver.find_element(*locator)
                    value = element.text.strip() if element.text else "No Text"
                    allureLogs(f"✅ Element {element_name} is DISPLAYED | [Value: {value}]")   # noqa:E501
                    element_found = True
                    break
            if not element_found:
                allureLogs(f"❌ Element {element_name} is NOT DISPLAYED")
                self.actions.screenshotAttachment(f"{element_name}: NOT DISPLAYED")     # noqa:E501
        self.actions.screenshotAttachment("Verified All items on experinces under Travel Sub-Category Tab")  # noqa:E501

    def navigate_to_travel_flights_subcategories(self):
        self.driver.back()
        self.actions.click_button(*locators_sd["TRAVEL_FLIGHTS"])
        allureLogs("Navigated to Flights Sub-category under Travel Sub-Category Tab")  # noqa:E501
        self.actions.screenshotAttachment("Navigated to flights Sub-category under Travel Sub-Category Tab")   # noqa:E501
        time.sleep(2)

    def verify_all_items_on_travel_flights_subcategory(self):
        allureLogs("Verifying all items on Flights under Travel Sub-Category Tab")  # noqa:E501
        locators = {
            "Travel Flights Page Title": [locators_sd["TRAVEL_FLIGHTS_PAGE_TITLE"]],    # noqa:E501
            "Travel Flights Back Button": [locators_sd["TRAVEL_FLIGHTS_BACK_BUTTON"]],  # noqa:E501
            "Travel Flights Search Icon": [locators_sd["TRAVEL_FLIGHTS_SEARCH_ICON"]],    # noqa:E501
            "Travel Flights Cart Icon": [locators_sd["TRAVEL_FLIGHTS_CART_ICON"]],  # noqa:E501
            "Travel Flights No of Products": [locators_sd["TRAVEL_FLIGHTS_NO_OF_PRODUCTS"]],  # noqa:E501
        }
        for element_name, locator_list in locators.items():
            element_found = False
            for locator in locator_list:
                if self.actions.is_element_displayed(*locator):
                    element = self.driver.find_element(*locator)
                    value = element.text.strip() if element.text else "No Text"
                    allureLogs(f"✅ Element {element_name} is DISPLAYED | [Value: {value}]")   # noqa:E501
                    element_found = True
                    break
            if not element_found:
                allureLogs(f"❌ Element {element_name} is NOT DISPLAYED")
                self.actions.screenshotAttachment(f"{element_name}: NOT DISPLAYED")     # noqa:E501
        self.actions.screenshotAttachment("Verified All items on flights under Travel Sub-Category Tab")  # noqa:E501

    def navigate_to_travel_hotels_subcategories(self):
        self.driver.back()
        self.actions.click_button(*locators_sd["TRAVEL_HOTELS"])
        allureLogs("Navigated to Flights Sub-category under Travel Sub-Category Tab")  # noqa:E501
        self.actions.screenshotAttachment("Navigated to flights Sub-category under Travel Sub-Category Tab")   # noqa:E501
        time.sleep(2)

    def verify_all_items_on_travel_hotels_subcategory(self):
        allureLogs("Verifying all items on Hotels under Travel Sub-Category Tab")  # noqa:E501
        locators = {
            "Travel Hotels Page Title": [locators_sd["TRAVEL_HOTELS_PAGE_TITLE"]],    # noqa:E501
            "Travel Hotels Back Button": [locators_sd["TRAVEL_HOTELS_BACK_BUTTON"]],  # noqa:E501
            "Travel Hotels Search Icon": [locators_sd["TRAVEL_HOTELS_SEARCH_ICON"]],    # noqa:E501
            "Travel Hotels Cart Icon": [locators_sd["TRAVEL_HOTELS_CART_ICON"]],  # noqa:E501
            "Travel Hotels No of Products": [locators_sd["TRAVEL_HOTELS_NO_OF_PRODUCTS"]],  # noqa:E501
        }
        for element_name, locator_list in locators.items():
            element_found = False
            for locator in locator_list:
                if self.actions.is_element_displayed(*locator):
                    element = self.driver.find_element(*locator)
                    value = element.text.strip() if element.text else "No Text"
                    allureLogs(f"✅ Element {element_name} is DISPLAYED | [Value: {value}]")   # noqa:E501
                    element_found = True
                    break
            if not element_found:
                allureLogs(f"❌ Element {element_name} is NOT DISPLAYED")
                self.actions.screenshotAttachment(f"{element_name}: NOT DISPLAYED")     # noqa:E501
        self.actions.screenshotAttachment("Verified All items on Hotels under Travel Sub-Category Tab")  # noqa:E501

    def navigate_to_food_subcategories(self):
        self.driver.back()
        self.driver.back()
        self.actions.click_button(*locators_sd["CATEGORIES_FOOD_MENU"])
        allureLogs("Navigated to Food Sub-Category Tab")
        self.actions.screenshotAttachment("Navigated to Food Sub-Category Tab")
        time.sleep(2)

    def verify_all_items_on_food_subcategory(self):
        allureLogs("Verifying all items on Food Sub-Category Tab")
        locators = {
            "Food Page Title": [locators_sd["FOOD_PAGE_TITLE"]],
            "Food Search Icon": [locators_sd["FOOD_SEARCH_ICON"]],
            "Food Cart Icon": [locators_sd["FOOD_CART_ICON"]],
            "Food Dining": [locators_sd["FOOD_DINING"]],
            "Food Groceries": [locators_sd["FOOD_GROCERIES"]],
            "Food Back Button": [locators_sd["FOOD_BACK_BUTTON"]],  # noqa:E501
        }
        for element_name, locator_list in locators.items():
            element_found = False
            for locator in locator_list:
                if self.actions.is_element_displayed(*locator):
                    element = self.driver.find_element(*locator)
                    value = element.text.strip() if element.text else "No Text"
                    allureLogs(f"✅ Element {element_name} is DISPLAYED | [Value: {value}]")   # noqa:E501
                    element_found = True
                    break
            if not element_found:
                allureLogs(f"❌ Element {element_name} is NOT DISPLAYED")
                self.actions.screenshotAttachment(f"{element_name}: NOT DISPLAYED")  # noqa:E501
        self.actions.screenshotAttachment("Verified All items on Food Sub-Category Tab")  # noqa:E501

    def navigate_to_food_dining_subcategories(self):
        self.actions.click_button(*locators_sd["FOOD_DINING"])
        allureLogs("Navigated to Dining Sub-category under Food Sub-Category Tab")  # noqa:E501
        self.actions.screenshotAttachment("Navigated to Dining Sub-category under Food Sub-Category Tab")   # noqa:E501
        time.sleep(2)

    def verify_all_items_on_food_dining_subcategory(self):
        allureLogs("Verifying all items on Dining under Food Sub-Category Tab")
        locators = {
            "Food Dining Page Title": [locators_sd["FOOD_DINING_PAGE_TITLE"]],    # noqa:E501
            "Food Dining Back Button": [locators_sd["FOOD_DINING_BACK_BUTTON"]],  # noqa:E501
            "Food Dining Search Icon": [locators_sd["FOOD_DINING_SEARCH_ICON"]],    # noqa:E501
            "Food Dining Cart Icon": [locators_sd["FOOD_DINING_CART_ICON"]],  # noqa:E501
            "Food Dining No of Products": [locators_sd["FOOD_DINING_NO_OF_PRODUCTS"]],  # noqa:E501
        }
        for element_name, locator_list in locators.items():
            element_found = False
            for locator in locator_list:
                if self.actions.is_element_displayed(*locator):
                    element = self.driver.find_element(*locator)
                    value = element.text.strip() if element.text else "No Text"
                    allureLogs(f"✅ Element {element_name} is DISPLAYED | [Value: {value}]")   # noqa:E501
                    element_found = True
                    break
            if not element_found:
                allureLogs(f"❌ Element {element_name} is NOT DISPLAYED")
                self.actions.screenshotAttachment(f"{element_name}: NOT DISPLAYED")     # noqa:E501
        self.actions.screenshotAttachment("Verified All items on Dining under Food Sub-Category Tab")   # noqa:E501

    def navigate_to_food_groceries_subcategories(self):
        self.driver.back()
        self.actions.click_button(*locators_sd["FOOD_GROCERIES"])
        allureLogs("Navigated to Groceries Sub-category under Food Sub-Category Tab")  # noqa:E501
        self.actions.screenshotAttachment("Navigated to Groceries Sub-category under Food Sub-Category Tab")  # noqa:E501
        time.sleep(2)

    def verify_all_items_on_food_groceries_subcategory(self):
        allureLogs("Verifying all items on Groceries under Food Sub-Category Tab")  # noqa:E501
        locators = {
            "Food Groceries Page Title": [locators_sd["FOOD_GROCERIES_PAGE_TITLE"]],    # noqa:E501
            "Food Groceries Back Button": [locators_sd["FOOD_GROCERIES_BACK_BUTTON"]],  # noqa:E501
            "Food Groceries Search Icon": [locators_sd["FOOD_GROCERIES_SEARCH_ICON"]],    # noqa:E501
            "Food Groceries Cart Icon": [locators_sd["FOOD_GROCERIES_CART_ICON"]],  # noqa:E501
            "Food Groceries No of Products": [locators_sd["FOOD_GROCERIES_NO_OF_PRODUCTS"]],  # noqa:E501
        }
        for element_name, locator_list in locators.items():
            element_found = False
            for locator in locator_list:
                if self.actions.is_element_displayed(*locator):
                    element = self.driver.find_element(*locator)
                    value = element.text.strip() if element.text else "No Text"
                    allureLogs(f"✅ Element {element_name} is DISPLAYED | [Value: {value}]")   # noqa:E501
                    element_found = True
                    break
            if not element_found:
                allureLogs(f"❌ Element {element_name} is NOT DISPLAYED")
                self.actions.screenshotAttachment(f"{element_name}: NOT DISPLAYED")  # noqa:E501
        self.actions.screenshotAttachment("Verified All items on Groceries under Food Sub-Category Tab")  # noqa:E501

    def navigate_to_movies_subcategories(self):
        self.driver.back()
        self.driver.back()
        self.actions.click_button(*locators_sd["CATEGORIES_MOVIES_MENU"])
        allureLogs("Navigated to Movies Sub-Category Tab")
        self.actions.screenshotAttachment("Navigated to Movies Sub-Category Tab")   # noqa:E501
        time.sleep(2)

    def verify_all_items_on_movies_subcategory(self):
        allureLogs("Verifying all items on Movies Sub-Category Tab")
        locators = {
            "Movies Page Title": [locators_sd["MOVIES_PAGE_TITLE"]],
            "Movies Search Icon": [locators_sd["MOVIES_SEARCH_ICON"]],
            "Movies Cart Icon": [locators_sd["MOVIES_CART_ICON"]],
            "Movies Movies": [locators_sd["MOVIES_MOVIES"]],
            "Movies OTT": [locators_sd["MOVIES_OTT"]],
            "Movies Back Button": [locators_sd["MOVIES_BACK_BUTTON"]],  # noqa:E501
        }
        for element_name, locator_list in locators.items():
            element_found = False
            for locator in locator_list:
                if self.actions.is_element_displayed(*locator):
                    element = self.driver.find_element(*locator)
                    value = element.text.strip() if element.text else "No Text"
                    allureLogs(f"✅ Element {element_name} is DISPLAYED | [Value: {value}]")   # noqa:E501
                    element_found = True
                    break
            if not element_found:
                allureLogs(f"❌ Element {element_name} is NOT DISPLAYED")
                self.actions.screenshotAttachment(f"{element_name}: NOT DISPLAYED")  # noqa:E501
        self.actions.screenshotAttachment("Verified All items on Movies Sub-Category Tab")  # noqa:E501

    def navigate_to_movies_movies_subcategories(self):
        self.actions.click_button(*locators_sd["MOVIES_MOVIES"])
        allureLogs("Navigated to Movies Sub-category under Movies Sub-Category Tab")  # noqa:E501
        self.actions.screenshotAttachment("Navigated to Movies Sub-category under Movies Sub-Category Tab")   # noqa:E501
        time.sleep(2)

    def verify_all_items_on_movies_movies_subcategory(self):
        allureLogs("Verifying all items on Dining under Food Sub-Category Tab")
        locators = {
            "Movies Dining Page Title": [locators_sd["MOVIES_MOVIES_PAGE_TITLE"]],    # noqa:E501
            "Movies Dining Back Button": [locators_sd["MOVIES_MOVIES_BACK_BUTTON"]],  # noqa:E501
            "Movies Dining Search Icon": [locators_sd["MOVIES_MOVIES_SEARCH_ICON"]],    # noqa:E501
            "Movies Dining Cart Icon": [locators_sd["MOVIES_MOVIES_CART_ICON"]],  # noqa:E501
            "Movies Dining No of Products": [locators_sd["MOVIES_MOVIES_NO_OF_PRODUCTS"]],  # noqa:E501
        }
        for element_name, locator_list in locators.items():
            element_found = False
            for locator in locator_list:
                if self.actions.is_element_displayed(*locator):
                    element = self.driver.find_element(*locator)
                    value = element.text.strip() if element.text else "No Text"
                    allureLogs(f"✅ Element {element_name} is DISPLAYED | [Value: {value}]")   # noqa:E501
                    element_found = True
                    break
            if not element_found:
                allureLogs(f"❌ Element {element_name} is NOT DISPLAYED")
                self.actions.screenshotAttachment(f"{element_name}: NOT DISPLAYED")     # noqa:E501
        self.actions.screenshotAttachment("Verified All items on Movies under Movies Sub-Category Tab")   # noqa:E501

    def navigate_to_movies_ott_subcategories(self):
        self.driver.back()
        self.actions.click_button(*locators_sd["MOVIES_OTT"])
        allureLogs("Navigated to OTT Sub-category under Movies Sub-Category Tab")  # noqa:E501
        self.actions.screenshotAttachment("Navigated to OTT Sub-category under Movies Sub-Category Tab")  # noqa:E501
        time.sleep(2)

    def verify_all_items_on_movies_ott_subcategory(self):
        allureLogs("Verifying all items on Groceries under Food Sub-Category Tab")  # noqa:E501
        locators = {
            "Movies OTT Page Title": [locators_sd["MOVIES_OTT_PAGE_TITLE"]],    # noqa:E501
            "Movies OTT Back Button": [locators_sd["MOVIES_OTT_BACK_BUTTON"]],  # noqa:E501
            "Movies OTT Search Icon": [locators_sd["MOVIES_OTT_SEARCH_ICON"]],    # noqa:E501
            "Movies OTT Cart Icon": [locators_sd["MOVIES_OTT_CART_ICON"]],  # noqa:E501
            "Movies OTT No of Products": [locators_sd["MOVIES_OTT_NO_OF_PRODUCTS"]],  # noqa:E501
        }
        for element_name, locator_list in locators.items():
            element_found = False
            for locator in locator_list:
                if self.actions.is_element_displayed(*locator):
                    element = self.driver.find_element(*locator)
                    value = element.text.strip() if element.text else "No Text"
                    allureLogs(f"✅ Element {element_name} is DISPLAYED | [Value: {value}]")   # noqa:E501
                    element_found = True
                    break
            if not element_found:
                allureLogs(f"❌ Element {element_name} is NOT DISPLAYED")
                self.actions.screenshotAttachment(f"{element_name}: NOT DISPLAYED")  # noqa:E501
        self.actions.screenshotAttachment("Verified All items on OTT under Movies Sub-Category Tab")  # noqa:E501

    def navigate_to_shopping(self):
        self.driver.back()
        self.driver.back()
        self.actions.click_button(*locators_sd["CATEGORIES_SHOPPING_MENU"])
        allureLogs("Navigated to Shopping Sub-Category Tab")
        self.actions.screenshotAttachment("Navigated to Shopping Sub-Category Tab")   # noqa:E501
        time.sleep(2)

    def verify_all_items_on_shopping_subcategory(self):
        allureLogs("Verifying all items on Shopping Sub-Category Tab")
        locators = {
            "Shopping Page Title": [locators_sd["SHOPPING_PAGE_TITLE"]],
            "Shopping Search Icon": [locators_sd["SHOPPING_SEARCH_ICON"]],
            "Shopping Cart Icon": [locators_sd["SHOPPING_CART_ICON"]],
            "Shopping Amazon E-Gift Card": [locators_sd["SHOPPING_AMAZON_EGIFT"]],  # noqa:E501
            "Shopping Amazon Shopping Voucher": [locators_sd["SHOPPING_AMAZON_SHOPPING"]],  # noqa:E501
            "Shopping Fashion and Accessories": [locators_sd["SHOPPING_FASHION_ACCESSORIES"]],  # noqa:E501
            "Shopping Flipkart": [locators_sd["SHOPPING_FLIPKART"]],
        }
        for element_name, locator_list in locators.items():
            element_found = False
            for locator in locator_list:
                if self.actions.is_element_displayed(*locator):
                    element = self.driver.find_element(*locator)
                    value = element.text.strip() if element.text else "No Text"
                    allureLogs(f"✅ Element {element_name} is DISPLAYED | [Value: {value}]")   # noqa:E501
                    element_found = True
                    break
            if not element_found:
                allureLogs(f"❌ Element {element_name} is NOT DISPLAYED")
                self.actions.screenshotAttachment(f"{element_name}: NOT DISPLAYED")  # noqa:E501
        self.actions.screenshotAttachment("Verified All items on Shopping Sub-Category Tab")  # noqa:E501

    def navigate_to_shopping_amazon_egift_card(self):
        self.actions.click_button(*locators_sd["SHOPPING_AMAZON_EGIFT"])
        allureLogs("Navigated to Amazon eGift Card Sub-category under Shopping Sub-Category Tab")  # noqa:E501
        self.actions.screenshotAttachment("Navigated to Amazon eGift Card Sub-category under Shopping Sub-Category Tab")   # noqa:E501
        time.sleep(2)

    def verify_all_items_on_shopping_amazon_egift_card_subcategory(self):
        allureLogs("Verifying all items on Amazon eGift Card under Shopping Sub-Category Tab")  # noqa:E501
        locators = {
            "Shopping Amazon eGift Card Page Title": [locators_sd["SHOPPING_AMAZON_EGIFT_PAGE_TITLE"]],    # noqa:E501
            "Shopping Amazon eGift Card Back Button": [locators_sd["SHOPPING_AMAZON_EGIFT_BACK_BUTTON"]],  # noqa:E501
            "Shopping Amazon eGift Card Search Icon": [locators_sd["SHOPPING_AMAZON_EGIFT_SEARCH_ICON"]],    # noqa:E501
            "Shopping Amazon eGift Card Cart Icon": [locators_sd["SHOPPING_AMAZON_EGIFT_CART_ICON"]],  # noqa:E501
            "Shopping Amazon eGift Card No of Products": [locators_sd["SHOPPING_AMAZON_EGIFT_NO_OF_PRODUCTS"]],  # noqa:E501
        }
        for element_name, locator_list in locators.items():
            element_found = False
            for locator in locator_list:
                if self.actions.is_element_displayed(*locator):
                    element = self.driver.find_element(*locator)
                    value = element.text.strip() if element.text else "No Text"
                    allureLogs(f"✅ Element {element_name} is DISPLAYED | [Value: {value}]")   # noqa:E501
                    element_found = True
                    break
            if not element_found:
                allureLogs(f"❌ Element {element_name} is NOT DISPLAYED")
                self.actions.screenshotAttachment(f"{element_name}: NOT DISPLAYED")     # noqa:E501
        self.actions.screenshotAttachment("Verified All items on Amazon eGift Card under Shopping Sub-Category Tab")  # noqa:E501

    def navigate_to_amazon_shopping_subcategories(self):
        self.driver.back()
        self.actions.click_button(*locators_sd["SHOPPING_AMAZON_SHOPPING"])
        allureLogs("Navigated to Amazon Sub-category under Shopping Sub-Category Tab")  # noqa:E501
        self.actions.screenshotAttachment("Navigated to Amazon Sub-category under Shopping Sub-Category Tab")   # noqa:E501
        time.sleep(2)

    def verify_all_items_on_amazon_shopping_subcategory(self):
        allureLogs("Verifying all items on Amazon under Shopping Sub-Category Tab")  # noqa:E501
        locators = {
            "Shopping Amazon Page Title": [locators_sd["SHOPPING_AMAZON_SHOPPING_PAGE_TITLE"]],   # noqa:E501
            "Shopping Amazon Search Icon": [locators_sd["SHOPPING_AMAZON_SHOPPING_PAGE_SEARCH_ICON"]],  # noqa:E501
            "Shopping Amazon Cart Icon": [locators_sd["SHOPPING_AMAZON_SHOPPING_PAGE_CART_ICON"]],  # noqa:E501
            "Shopping Amazon No of Products": [locators_sd["SHOPPING_AMAZON_SHOPPING_PAGE_NO_OF_PRODUCTS"]],  # noqa:E501
            "Shopping Amazon Back Button": [locators_sd["SHOPPING_AMAZON_SHOPPING_PAGE_BACK_BUTTON"]],  # noqa:E501
        }
        for element_name, locator_list in locators.items():
            element_found = False
            for locator in locator_list:
                if self.actions.is_element_displayed(*locator):
                    element = self.driver.find_element(*locator)
                    value = element.text.strip() if element.text else "No Text"
                    allureLogs(f"✅ Element {element_name} is DISPLAYED | [Value: {value}]")   # noqa:E501
                    element_found = True
                    break
            if not element_found:
                allureLogs(f"❌ Element {element_name} is NOT DISPLAYED")
                self.actions.screenshotAttachment(f"{element_name}: NOT DISPLAYED")     # noqa:E501
        self.actions.screenshotAttachment("Verified All items on Amazon under Shopping Sub-Category Tab")  # noqa:E501

    def navigate_to_shopping_fashion_accessories_subcategories(self):
        self.driver.back()
        self.actions.click_button(*locators_sd["SHOPPING_FASHION_ACCESSORIES"])
        allureLogs("Navigated to Fashion Sub-category under Shopping Sub-Category Tab")  # noqa:E501
        self.actions.screenshotAttachment("Navigated to Fashion Sub-category under Shopping Sub-Category Tab")   # noqa:E501
        time.sleep(2)

    def verify_all_items_on_shopping_fashion_accessories_subcategory(self):
        allureLogs("Verifying all items on Fashion & Accessories under Shopping Sub-Category Tab")  # noqa:E501
        locators = {
            "Shopping Fashion Page Title": [locators_sd["SHOPPING_FASHION_ACCESSORIES_PAGE_TITLE"]],    # noqa:E501
            "Shopping Fashion Back Button": [locators_sd["SHOPPING_FASHION_ACCESSORIES_BACK_BUTTON"]],  # noqa:E501
            "Shopping Fashion Search Icon": [locators_sd["SHOPPING_FASHION_ACCESSORIES_SEARCH_ICON"]],    # noqa:E501
            "Shopping Fashion Cart Icon": [locators_sd["SHOPPING_FASHION_ACCESSORIES_CART_ICON"]],  # noqa:E501
            "Shopping Fashion No of Products": [locators_sd["SHOPPING_FASHION_ACCESSORIES_NO_OF_PRODUCTS"]],  # noqa:E501
        }
        for element_name, locator_list in locators.items():
            element_found = False
            for locator in locator_list:
                if self.actions.is_element_displayed(*locator):
                    element = self.driver.find_element(*locator)
                    value = element.text.strip() if element.text else "No Text"
                    allureLogs(f"✅ Element {element_name} is DISPLAYED | [Value: {value}]")   # noqa:E501
                    element_found = True
                    break
            if not element_found:
                allureLogs(f"❌ Element {element_name} is NOT DISPLAYED")
                self.actions.screenshotAttachment(f"{element_name}: NOT DISPLAYED")     # noqa:E501
        self.actions.screenshotAttachment("Verified All items on Fashion & accessories under Shopping Sub-Category Tab")  # noqa:E501

    def navigate_to_shopping_gifting_subcategories(self):
        """yet to include in test & feature file"""
        self.driver.back()
        self.actions.click_button(*locators_sd["SHOPPING_GIFTING"])
        allureLogs("Navigated to Gifting Sub-category under Shopping Sub-Category Tab")  # noqa:E501
        self.actions.screenshotAttachment("Navigated to Gifting Sub-category under Shopping Sub-Category Tab")   # noqa:E501
        time.sleep(2)

    def verify_all_items_on_shopping_gifting_subcategory(self):
        """yet to include in test & feature file"""
        allureLogs("Verifying all items on Gifting under Shopping Sub-Category Tab")  # noqa:E501
        locators = {
            "Shopping Gifting Page Title": [locators_sd["SHOPPING_GIFTING_PAGE_TITLE"]],    # noqa:E501
            "Shopping Gifting Back Button": [locators_sd["SHOPPING_GIFTING_BACK_BUTTON"]],  # noqa:E501
            "Shopping Gifting Search Icon": [locators_sd["SHOPPING_GIFTING_SEARCH_ICON"]],    # noqa:E501
            "Shopping Gifting Cart Icon": [locators_sd["SHOPPING_GIFTING_CART_ICON"]],  # noqa:E501
            "Shopping Gifting No of Products": [locators_sd["SHOPPING_GIFTING_NO_OF_PRODUCTS"]],  # noqa:E501
        }
        for element_name, locator_list in locators.items():
            element_found = False
            for locator in locator_list:
                if self.actions.is_element_displayed(*locator):
                    element = self.driver.find_element(*locator)
                    value = element.text.strip() if element.text else "No Text"
                    allureLogs(f"✅ Element {element_name} is DISPLAYED | [Value: {value}]")   # noqa:E501
                    element_found = True
                    break
            if not element_found:
                allureLogs(f"❌ Element {element_name} is NOT DISPLAYED")
                self.actions.screenshotAttachment(f"{element_name}: NOT DISPLAYED")     # noqa:E501
        self.actions.screenshotAttachment("Verified All items on Gifting under Shopping Sub-Category Tab")  # noqa:E501

    def navigate_to_shopping_jewellery_subcategories(self):
        """yet to include in test & feature file"""
        self.driver.back()
        self.actions.click_button(*locators_sd["SHOPPING_JEWELLERY"])
        allureLogs("Navigated to Jewellery Sub-category under Shopping Sub-Category Tab")  # noqa:E501
        self.actions.screenshotAttachment("Navigated to Jewellery Sub-category under Shopping Sub-Category Tab")   # noqa:E501
        time.sleep(2)

    def verify_all_items_on_shopping_jewellery_subcategory(self):
        """yet to include in test & feature file"""
        allureLogs("Verifying all items on Jewellery under Shopping Sub-Category Tab")  # noqa:E501
        locators = {
            "Shopping Jewellery Page Title": [locators_sd["SHOPPING_JEWELLERY_PAGE_TITLE"]],    # noqa:E501
            "Shopping Jewellery Back Button": [locators_sd["SHOPPING_JEWELLERY_BACK_BUTTON"]],  # noqa:E501
            "Shopping Jewellery Search Icon": [locators_sd["SHOPPING_JEWELLERY_SEARCH_ICON"]],    # noqa:E501
            "Shopping Jewellery Cart Icon": [locators_sd["SHOPPING_JEWELLERY_CART_ICON"]],  # noqa:E501
            "Shopping Jewellery No of Products": [locators_sd["SHOPPING_JEWELLERY_NO_OF_PRODUCTS"]],  # noqa:E501
        }
        for element_name, locator_list in locators.items():
            element_found = False
            for locator in locator_list:
                if self.actions.is_element_displayed(*locator):
                    element = self.driver.find_element(*locator)
                    value = element.text.strip() if element.text else "No Text"
                    allureLogs(f"✅ Element {element_name} is DISPLAYED | [Value: {value}]")   # noqa:E501
                    element_found = True
                    break
            if not element_found:
                allureLogs(f"❌ Element {element_name} is NOT DISPLAYED")
                self.actions.screenshotAttachment(f"{element_name}: NOT DISPLAYED")     # noqa:E501
        self.actions.screenshotAttachment("Verified All items on Jewellery under Shopping Sub-Category Tab")  # noqa:E501

    def navigate_to_shopping_flipkart_subcategories(self):
        self.driver.back()
        self.actions.click_button(*locators_sd["SHOPPING_FLIPKART"])
        allureLogs("Navigated to Flipkart Sub-category under Shopping Sub-Category Tab")  # noqa:E501
        self.actions.screenshotAttachment("Navigated to Flipkart Sub-category under Shopping Sub-Category Tab")   # noqa:E501
        time.sleep(2)

    def verify_all_items_on_shopping_flipkart_subcategory(self):
        allureLogs("Verifying all items on Flipkart under Shopping Sub-Category Tab")  # noqa:E501
        locators = {
            "Shopping Flipkart Page Title": [locators_sd["SHOPPING_FLIPKART_PAGE_TITLE"]],  # noqa:E501
            "Shopping Flipkart Search Icon": [locators_sd["SHOPPING_FLIPKART_SEARCH_ICON"]],    # noqa:E501
            "Shopping Flipkart Cart Icon": [locators_sd["SHOPPING_FLIPKART_CART_ICON"]],    # noqa:E501
            "Shopping Flipkart No of Products": [locators_sd["SHOPPING_FLIPKART_NO_OF_PRODUCTS"]],  # noqa:E501
            "Shopping Flipkart Back Button": [locators_sd["SHOPPING_FLIPKART_BACK_BUTTON"]],  # noqa:E501
        }
        for element_name, locator_list in locators.items():
            element_found = False
            for locator in locator_list:
                if self.actions.is_element_displayed(*locator):
                    element = self.driver.find_element(*locator)
                    value = element.text.strip() if element.text else "No Text"
                    allureLogs(f"✅ Element {element_name} is DISPLAYED | [Value: {value}]")   # noqa:E501
                    element_found = True
                    break
            if not element_found:
                allureLogs(f"❌ Element {element_name} is NOT DISPLAYED")
                self.actions.screenshotAttachment(f"{element_name}: NOT DISPLAYED")     # noqa:E501
        self.actions.screenshotAttachment("Verified All items on Flipkart under Shopping Sub-Category Tab")  # noqa:E501

    def navigate_to_my_orders_tab(self):
        self.driver.back()
        self.driver.back()
        self.driver.back()
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
                    allureLogs(f"✅ Element {element_name} is DISPLAYED | (Value: {value})")   # noqa:E501
                    element_found = True
                    break
            if not element_found:
                allureLogs(f"❌ Element {element_name} is NOT DISPLAYED")
                self.actions.screenshotAttachment(f"{element_name}: NOT DISPLAYED")  # noqa:E501
        self.actions.screenshotAttachment("Verified All items on MY Orders TAB")    # noqa:E501
