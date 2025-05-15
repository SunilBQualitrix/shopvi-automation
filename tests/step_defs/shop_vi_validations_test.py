import time
from pytest_bdd import given, when, then, scenarios, parsers
import allure
import pytest
from pages.base_page import BasePage
from pages.navto_shop import NavtoShop
from pages.shop_dashboard_page import ShopDashboardPage
from pages.search_page import SearchPage
from pages.accountPage import AccountPage
from pages.pdp_flipkart import ProductDetailsPageFlipkart
from pages.actions.android_actions import AndroidActions

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../pages')))  # noqa:E501

# Load the feature file
scenarios('../features/Shop_Vi_Validations.feature')


# ======== Fixtures ========
@pytest.fixture
def navtoshop_instance(setup_platform):
    """Fixture to initialize the NavtoShop page object."""
    return NavtoShop(setup_platform)


@pytest.fixture
def basepage_instance(setup_platform):
    """Fixture to initialize the BasePage object."""
    return BasePage(setup_platform)


@pytest.fixture
def androidactions_instance(setup_platform):
    """Fixture to initialize the Android object."""
    return AndroidActions(setup_platform)


@pytest.fixture
def shoppage_instance(setup_platform):
    """Fixture to initialize the Shop Dashboard Page object."""
    return ShopDashboardPage(setup_platform)


@pytest.fixture
def searchpage_instance(setup_platform):
    """Fixture to initialize the Shop Dashboard Page object."""
    return SearchPage(setup_platform)


@pytest.fixture
def accountpage_instance(setup_platform):
    """Fixture to initialize the Account Page object."""
    return AccountPage(setup_platform)


@pytest.fixture
def pdpflipkart_instance(setup_platform):
    """Fixture to initialize the PDP Flipkart Page object."""
    return ProductDetailsPageFlipkart(setup_platform)


# ======== Step Definitions ===========================

# ======== Navugation to Shop ========

@given(parsers.parse("I install vishop {application}"))
@allure.step("Given I install vishop {application}")
def install_vishop_application(basepage_instance, application):
    """Step to simulate installing the application."""
    print(f"Installing application: {application}")


@given("I launch vishop Application")
@allure.step("Given I launch vishop Application")
def launch_vishop_application(basepage_instance):
    """Step to launch the vishop application."""
    print("Launching vishop application...")
    basepage_instance.launchApp()


@given("I open the app and navigate to the mobile number input screen")
@allure.step("Given I open the app and navigate to the mobile number input screen")       # noqa:E501
def open_app_and_navigate_to_mobile_number_input_screen(navtoshop_instance):
    """Step to navigate to the mobile number input screen."""
    enter_mobile_number = navtoshop_instance.click_number_input_field()
    assert enter_mobile_number, "Mobile number input screen is not displayed after launching the vishop application"          # noqa:E501


@when("I close the mobile number dialog box")
@allure.step("When I close the mobile number dialog box")
def close_the_mobile_number_dialog_box(navtoshop_instance):
    """Step to close the dialog box."""
    navtoshop_instance.click_dialog_box()


@when(parsers.parse("I input a valid 10-digit mobile number {mobile_number}"))
@allure.step("When I input a valid 10-digit mobile number {mobile_number}")
def input_a_valid_mobile_number(navtoshop_instance, mobile_number):
    """Step to input a valid mobile number."""
    navtoshop_instance.input_valid_mobilenumber(mobile_number)


@when("I click on the send OTP CTA button")
@allure.step("When I click on the send OTP CTA button")
def click_on_send_otp_cta_button(navtoshop_instance):
    """Step to click on the OTP button."""
    navtoshop_instance.click_otp_button()


@when(parsers.parse("I input a valid 4-digit OTP {otp}"))
@allure.step("When I input a valid 4-digit OTP {otp}")
def input_a_valid_otp(navtoshop_instance, otp):
    """Step to input a valid OTP."""
    time.sleep(5)
    navtoshop_instance.input_otp(otp)


@when("I log into the app using login with OTP CTA button")
@allure.step("When I log into the app using login with OTP CTA button")
def log_into_the_app_using_login_with_otp_cta_button(navtoshop_instance):
    """Step to log in using the OTP."""
    navtoshop_instance.login_wotp_button()


@then("I click on VI Shop from Bottom Navigation and should navigate to the shop Dashboard")      # noqa:E501
@allure.step("Then I click on VI Shop from Bottom Navigation and should navigate to the shop Dashboard")      # noqa:E501
def click_on_vi_shop_from_bottom_navigation_and_should_navigate_to_the_shop_dashboard(navtoshop_instance, shoppage_instance):     # noqa:E501
    """Step to navigate to the shop dashboard."""
    navtoshop_instance.navto_shop()
    shop_page_reached = shoppage_instance.verify_shop_dashboard_page()
    assert shop_page_reached, "Shop Dashboard page is not reached"


# ======== Account Page Validation ========

@when("I verify the account button is displayed")
@allure.step("When I verify the account button is displayed")
def verify_account_button_is_displayed(accountpage_instance):
    """Step to verify if the account button is displayed."""
    is_displayed = accountpage_instance.verify_account_button()
    assert is_displayed, "Account button is not displayed."


@when("I click on the account button and navigate to the account page")
@allure.step("When I click on the account button and navigate to the account page")   # noqa:E501
def click_account_button_and_navigate_to_account_page(accountpage_instance):
    """Step to click the account button and navigate to the account page."""
    clicked = accountpage_instance.click_account_button()
    assert clicked, "Failed to click on the account button and navigate to the account page."     # noqa:E501


@then("I verify all elements are displayed on the account page")
@allure.step("Then I verify all elements are displayed on the account page")
def verify_all_elements_on_account_page(accountpage_instance):
    """Step to verify all elements on the account page."""
    print("Verifying all elements on the account page...")
    accountpage_instance.verify_account_page_elements()
    print("Verification of account page elements completed.")


@when("I navigate to the FAQ page")
@allure.step("When I navigate to the FAQ page")
def navigate_to_faq_page(accountpage_instance):
    """Step to navigate to the FAQ page."""
    navigated = accountpage_instance.verify_nav_to_faq_page()
    assert navigated, "Failed to navigate to the FAQ page. FAQ element was not displayed."    # noqa:E501


@then("I verify all elements are displayed on the FAQ page")
@allure.step("Then I verify all elements are displayed on the FAQ page")
def verify_all_elements_on_faq_page(accountpage_instance):
    """Step to verify all elements are displayed on the FAQ page."""
    print("Verifying all elements on the FAQ page...")
    accountpage_instance.verify_and_print_all_elements_on_faq_page()
    print("Verification of FAQ page elements completed.")
    # Navigate back to the previous page
    try:
        accountpage_instance.driver.back()  # Or use faqpage_instance.driver.press_keycode(4)     # noqa:E501
        print("Navigated back from the FAQ page successfully.")
    except Exception as e:
        print(f"Failed to navigate back from the FAQ page: {e}")


@when("I navigate to the Credit Card (CC) page")
@allure.step("When I navigate to the Credit Card (CC) page")
def navigate_to_cc_page(accountpage_instance):
    """Step to navigate to the Credit Card (CC) page."""
    navigated = accountpage_instance.verify_nav_to_cc_page()
    assert navigated, "Failed to navigate to the Credit Card (CC) page."


@then("I verify all elements are displayed on the Credit Card (CC) page")
@allure.step("Then I verify all elements are displayed on the Credit Card (CC) page")     # noqa:E501
def verify_all_elements_on_cc_page(accountpage_instance):
    """Step to verify all elements are displayed on the Credit Card (CC) page."""         # noqa:E501
    print("Verifying all elements on the Credit Card (CC) page...")
    accountpage_instance.verify_and_print_all_elements_on_cc_page()
    print("Verification of Credit Card (CC) page elements completed.")
    # Navigate back to the previous page
    accountpage_instance.driver.back()
    print("Navigated back from the Credit Card (CC) page successfully.")


@when("I navigate to the Orders page")
@allure.step("When I navigate to the Orders page")
def navigate_to_orders_page(accountpage_instance):
    """Step to navigate to the Orders page."""
    navigated = accountpage_instance.verify_nav_to_orders_page()
    assert navigated, "Failed to navigate to the Orders page."


@then("I verify all elements are displayed on the Orders page")
@allure.step("Then I verify all elements are displayed on the Orders page")
def verify_all_elements_on_orders_page(accountpage_instance):
    """Step to verify all elements are displayed on the Orders page."""
    print("Verifying all elements on the Orders page...")
    accountpage_instance.verify_and_print_all_elements_on_myorders_page()
    print("Verifying all elements on the Orders page completed.")
    # Navigate back to the previous page
    accountpage_instance.driver.back()
    print("Navigated back from the Orders page successfully.")


@when("I navigate to the Coupons page")
@allure.step("When I navigate to the Coupons page")
def navigate_to_coupons_page(accountpage_instance):
    """Step to navigate to the Coupons page."""
    navigated = accountpage_instance.verify_nav_to_coupons_page()
    assert navigated, "Failed to navigate to the Coupons page."


@then("I verify all elements are displayed on the Coupons page")
@allure.step("Then I verify all elements are displayed on the Coupons page")
def verify_all_elements_on_coupons_page(accountpage_instance):
    """Step to verify all elements are displayed on the Coupons page."""
    print("Verifying all elements on the Coupons page...")
    accountpage_instance.verify_and_print_all_elements_under_CouponsPage()
    print("Verifying all elements on the Coupons page...")
    # Navigate back to the previous page
    accountpage_instance.driver.back()
    print("Navigated back from the Coupons page successfully.")


@when("I navigate to the T and C page")
@allure.step("When I navigate to the T and C page")
def navigate_to_t_and_c_page(accountpage_instance):
    """Step to navigate to the T and C page."""
    navigated = accountpage_instance.verify_nav_to_tandc_page()
    assert navigated, "Failed to navigate to the T and C page."
    accountpage_instance.driver.back()


@when("I navigate to the Privacy and Policy page")
@allure.step("When I navigate to the Privacy and Policy page")
def navigate_to_privacy_and_policy_page(accountpage_instance):
    """Step to navigate to the Privacy and Policy page."""
    navigated = accountpage_instance.verify_nav_to_privacy_policy_page()
    assert navigated, "Failed to navigate to the Privacy and Policy page."
    accountpage_instance.driver.back()


@when("I navigate to the About US page")
@allure.step("When I navigate to the About US page")
def navigate_to_about_us_page(accountpage_instance):
    """Step to navigate to the About US page."""
    navigated = accountpage_instance.verify_nav_to_about_us_page()
    assert navigated, "Failed to navigate to the About US page."
    accountpage_instance.driver.back()


@when(("I navigate to Saved Payments page"))
@allure.step("When I navigate to Saved Payments page")
def navigate_to_saved_payments_page(accountpage_instance):
    """Step to navigate to the Saved Payments page."""
    navigated = accountpage_instance.verify_nav_to_saved_payments_page()
    assert navigated, "Failed to navigate to the Saved Payments page."


@then("I Verify all elements are displayed on the Saved Payments page")
@allure.step("Then I Verify all elements are displayed on the Saved Payments page")       # noqa:E501
def verify_all_elements_on_saved_payments_page(accountpage_instance):
    """Step to verify all elements on the Saved Payments page."""
    print("Verifying all elements on the Saved Payments page...")
    accountpage_instance.verify_and_print_all_elements_on_saved_payments_page()
    print("Verification of Saved Payments page elements completed.")
    # Navigate back to the previous page
    print("Navigated back from the Saved Payments page successfully.")
    accountpage_instance.driver.back()
    accountpage_instance.driver.back()


# ======== Validation of navigation across Tabs Shop_db_page POM ========

@when(("I am on shop dashboard and verify Quick Purchase Section"))   # noqa:E501
@allure.step("When I am on shop dashboard and verify Quick Purchase Section")          # noqa:E501
def open_the_shop_tab_and_verify_quick_purchase_on_shop_dashboard(shoppage_instance):        # noqa:E501
    """Step to verify all items are displayed on the shop dashboard."""
    shoppage_instance.verify_quick_purchase_items_on_Shop_dashboard()


@when(("I am on shop dashboard and verify all items are displayed on shop dashboard"))   # noqa:E501
@allure.step("When I am on shop dashboard and verify all items are displayed on shop dashboard")          # noqa:E501
def open_the_shop_tab_and_verify_all_items_are_displayed_on_shop_dashboard(shoppage_instance):        # noqa:E501
    """Step to verify all items are displayed on the shop dashboard."""
    shoppage_instance.verify_all_items_on_shop_dashboard()


@when("I navigate to the deals tab")
@allure.step("When I navigate to the deals tab")
def navigate_to_deals_tab(shoppage_instance):
    """Step to navigate to the deals tab."""
    shoppage_instance.navigate_to_deals_tab()


@then("I verify all items are displayed on the deals tab")
@allure.step("Then I verify all items are displayed on the deals tab")
def verify_all_items_are_displayed_on_the_deals_tab(shoppage_instance):
    """Step to verify all items are displayed on the deals tab."""
    shoppage_instance.verify_all_items_on_deals_tab()


@when("I navigate to the categories tab")
@allure.step("When I navigate to the categories tab")
def navigate_to_categories(shoppage_instance):
    """Step to navigate to the categories tab."""
    shoppage_instance.navigate_to_categories_tab()


@then("I verify all items are displayed on the categories tab")
@allure.step("Then I verify all items are displayed on the categories tab")
def verify_all_items_are_displayed_on_the_categories_tab(shoppage_instance):
    """Step to verify all items are displayed on the categories tab."""
    shoppage_instance.verify_all_items_on_categories_tab()


@when("I navigate to the Travel Sub-category under Categories tab")
@allure.step("When I navigate to the Travel Sub-category under Categories tab")
def navigate_to_categories(shoppage_instance):
    """Step to navigate to the categories tab."""
    shoppage_instance.navigate_to_travel_subcategories()


@then("I verify all items that are displayed under Travel Sub-category")
@allure.step("Then I verify all items that are displayed under Travel Sub-category")    # noqa:E501
def verify_all_items_are_displayed_on_the_categories_tab(shoppage_instance):
    """Step to verify all items are displayed on the categories tab."""
    shoppage_instance.verify_all_items_on_travel_subcategory()


@when("I navigate to the CABS inside Travel Sub-category under Categories tab")
@allure.step("When I navigate to the CABS inside Travel Sub-category under Categories tab")   # noqa:E501
def navigate_to_categories(shoppage_instance):
    """Step to navigate to the categories tab."""
    shoppage_instance.navigate_to_travel_cabs_subcategories()


@then("I verify all items that are displayed under CABS inside Travel Sub-category")    # noqa:E501
@allure.step("Then I verify all items that are displayed under CABS inside Travel Sub-category")    # noqa:E501
def verify_all_items_are_displayed_on_the_categories_tab(shoppage_instance):
    """Step to verify all items are displayed on the categories tab."""
    shoppage_instance.verify_all_items_on_travel_cabs_subcategory()


@when("I navigate to the Hotels inside Travel Sub-category under Categories tab")   # noqa:E501
@allure.step("When I navigate to the Hotels inside Travel Sub-category under Categories tab")   # noqa:E501
def navigate_to_categories(shoppage_instance):
    """Step to navigate to the categories tab."""
    shoppage_instance.navigate_to_travel_hotels_subcategories()


@then("I verify all items that are displayed under Hotels inside Travel Sub-category")    # noqa:E501
@allure.step("Then I verify all items that are displayed under Hotels inside Travel Sub-category")    # noqa:E501
def verify_all_items_are_displayed_on_the_categories_tab(shoppage_instance):
    """Step to verify all items are displayed on the categories tab."""
    shoppage_instance.verify_all_items_on_travel_hotels_subcategory()


@when("I navigate to the Flights inside Travel Sub-category under Categories tab")  # noqa:E501
@allure.step("When I navigate to the Flights inside Travel Sub-category under Categories tab")   # noqa:E501
def navigate_to_categories(shoppage_instance):
    """Step to navigate to the categories tab."""
    shoppage_instance.navigate_to_travel_flights_subcategories()


@then("I verify all items that are displayed under Flights inside Travel Sub-category")    # noqa:E501
@allure.step("Then I verify all items that are displayed under Flights inside Travel Sub-category")    # noqa:E501
def verify_all_items_are_displayed_on_the_categories_tab(shoppage_instance):
    """Step to verify all items are displayed on the categories tab."""
    shoppage_instance.verify_all_items_on_travel_flights_subcategory()


@when("I navigate to the Experinces inside Travel Sub-category under Categories tab")   # noqa:E501
@allure.step("When I navigate to the Experinces inside Travel Sub-category under Categories tab")   # noqa:E501
def navigate_to_categories(shoppage_instance):
    """Step to navigate to the categories tab."""
    shoppage_instance.navigate_to_travel_experinces_subcategories()


@then("I verify all items that are displayed under Experinces inside Travel Sub-category")    # noqa:E501
@allure.step("Then I verify all items that are displayed under Experinces inside Travel Sub-category")    # noqa:E501
def verify_all_items_are_displayed_on_the_categories_tab(shoppage_instance):
    """Step to verify all items are displayed on the categories tab."""
    shoppage_instance.verify_all_items_on_travel_experinces_subcategory()


@when("I navigate to Food Subcategory under Categories tab")   # noqa:E501
@allure.step("When I navigate to Food Subcategory under Categories tab")   # noqa:E501
def navigate_to_categories(shoppage_instance):
    """Step to navigate to the categories tab."""
    shoppage_instance.navigate_to_food_subcategories()


@then("I verify all items that are displayed under Food Subcategory")    # noqa:E501
@allure.step("Then I verify all items that are displayed under Food Subcategory")    # noqa:E501
def verify_all_items_are_displayed_on_the_categories_tab(shoppage_instance):
    """Step to verify all items are displayed on the categories tab."""
    shoppage_instance.verify_all_items_on_food_subcategory()


@when("I navigate to dining subcategory under food")   # noqa:E501
@allure.step("When I navigate to dining subcategory under food")   # noqa:E501
def navigate_to_categories(shoppage_instance):
    """Step to navigate to the categories tab."""
    shoppage_instance.navigate_to_food_dining_subcategories()


@then("I verify all items that are displayed under dining subcategory")    # noqa:E501
@allure.step("Then I verify all items that are displayed under dining subcategory")    # noqa:E501
def verify_all_items_are_displayed_on_the_categories_tab(shoppage_instance):
    """Step to verify all items are displayed on the categories tab."""
    shoppage_instance.verify_all_items_on_food_dining_subcategory()


@when("I navigate to Groceries Subcategory under Food")   # noqa:E501
@allure.step("When I navigate to Groceries Subcategory under Food")   # noqa:E501
def navigate_to_categories(shoppage_instance):
    """Step to navigate to the categories tab."""
    shoppage_instance.navigate_to_food_groceries_subcategories()


@then("I verify all items that are displayed under Groceries Subcategory")    # noqa:E501
@allure.step("Then I verify all items that are displayed under Groceries Subcategory")    # noqa:E501
def verify_all_items_are_displayed_on_the_categories_tab(shoppage_instance):
    """Step to verify all items are displayed on the categories tab."""
    shoppage_instance.verify_all_items_on_food_groceries_subcategory()


@when("I navigate to Movies Subcategory under Categories tab")   # noqa:E501
@allure.step("When I navigate to Movies Subcategory under Categories tab")   # noqa:E501
def navigate_to_categories(shoppage_instance):
    """Step to navigate to the categories tab."""
    shoppage_instance.navigate_to_movies_subcategories()


@then("I verify all items that are displayed under Movies Subcategory")    # noqa:E501
@allure.step("Then I verify all items that are displayed under Movies Subcategory")    # noqa:E501
def verify_all_items_are_displayed_on_the_categories_tab(shoppage_instance):
    """Step to verify all items are displayed on the categories tab."""
    shoppage_instance.verify_all_items_on_movies_subcategory()


@when("I navigate to Movies subcategory under Movies")   # noqa:E501
@allure.step("When I navigate to Movies subcategory under Movies")   # noqa:E501
def navigate_to_categories(shoppage_instance):
    """Step to navigate to the categories tab."""
    shoppage_instance.navigate_to_movies_movies_subcategories()


@then("I verify all items that are displayed under Movies subcategory")    # noqa:E501
@allure.step("Then I verify all items that are displayed under Movies subcategory")    # noqa:E501
def verify_all_items_are_displayed_on_the_categories_tab(shoppage_instance):
    """Step to verify all items are displayed on the categories tab."""
    shoppage_instance.verify_all_items_on_movies_movies_subcategory()


@when("I navigate to OTT Subcategory under Movies")   # noqa:E501
@allure.step("When I navigate to OTT Subcategory under Movies")   # noqa:E501
def navigate_to_categories(shoppage_instance):
    """Step to navigate to the categories tab."""
    shoppage_instance.navigate_to_movies_ott_subcategories()


@then("I verify all items that are displayed under OTT Subcategory")    # noqa:E501
@allure.step("Then I verify all items that are displayed under OTT Subcategory")    # noqa:E501
def verify_all_items_are_displayed_on_the_categories_tab(shoppage_instance):
    """Step to verify all items are displayed on the categories tab."""
    shoppage_instance.verify_all_items_on_movies_ott_subcategory()


@when("I navigate to Shopping Subcategory")   # noqa:E501
@allure.step("When I navigate to Shopping Subcategory")   # noqa:E501
def navigate_to_categories(shoppage_instance):
    """Step to navigate to the categories tab."""
    shoppage_instance.navigate_to_shopping()


@then("I verify all items that are displayed under Shopping Subcategory")    # noqa:E501
@allure.step("Then I verify all items that are displayed under Shopping Subcategory")    # noqa:E501
def verify_all_items_are_displayed_on_the_categories_tab(shoppage_instance):
    """Step to verify all items are displayed on the categories tab."""
    shoppage_instance.verify_all_items_on_shopping_subcategory()


@when("I navigate to Amazon Egift card subcategory under Shopping")   # noqa:E501
@allure.step("When I navigate to Amazon Egift card subcategory under Shopping")   # noqa:E501
def navigate_to_categories(shoppage_instance):
    """Step to navigate to the categories tab."""
    shoppage_instance.navigate_to_shopping_amazon_egift_card()


@then("I verify all items that are displayed under Amazon Egift card subcategory")    # noqa:E501
@allure.step("Then I verify all items that are displayed under Amazon Egift card subcategory")    # noqa:E501
def verify_all_items_are_displayed_on_the_categories_tab(shoppage_instance):
    """Step to verify all items are displayed on the categories tab."""
    shoppage_instance.verify_all_items_on_shopping_amazon_egift_card_subcategory()  # noqa:E501


@when("I navigate to Amazon Shopping voucher subcategory under Shopping")   # noqa:E501
@allure.step("When I navigate to Amazon Shopping voucher subcategory under Shopping")   # noqa:E501
def navigate_to_categories(shoppage_instance):
    """Step to navigate to the categories tab."""
    shoppage_instance.navigate_to_amazon_shopping_subcategories()


@then("I verify all items that are displayed under Amazon Shopping voucher subcategory")    # noqa:E501
@allure.step("Then I verify all items that are displayed under Amazon Shopping voucher subcategory")    # noqa:E501
def verify_all_items_are_displayed_on_the_categories_tab(shoppage_instance):
    """Step to verify all items are displayed on the categories tab."""
    shoppage_instance.verify_all_items_on_amazon_shopping_subcategory()


@when("I navigate to Fashion and accessories subcategory under Shopping")   # noqa:E501
@allure.step("When I navigate to Fashion and accessories subcategory under Shopping")   # noqa:E501
def navigate_to_categories(shoppage_instance):
    """Step to navigate to the categories tab."""
    shoppage_instance.navigate_to_shopping_fashion_accessories_subcategories()


@then("I verify all items that are displayed under Fashion and accessories subcategory")    # noqa:E501
@allure.step("Then I verify all items that are displayed under Fashion and accessories subcategory")    # noqa:E501
def verify_all_items_are_displayed_on_the_categories_tab(shoppage_instance):
    """Step to verify all items are displayed on the categories tab."""
    shoppage_instance.verify_all_items_on_shopping_fashion_accessories_subcategory()    # noqa:E501


@when("I navigate to Flipkart subcategory under Shopping")   # noqa:E501
@allure.step("When I navigate to Flipkart subcategory under Shopping")   # noqa:E501
def navigate_to_categories(shoppage_instance):
    """Step to navigate to the categories tab."""
    shoppage_instance.navigate_to_shopping_flipkart_subcategories()


@then("I verify all items that are displayed under Flipkart subcategory")    # noqa:E501
@allure.step("Then I verify all items that are displayed under Flipkart subcategory")    # noqa:E501
def verify_all_items_are_displayed_on_the_categories_tab(shoppage_instance):
    """Step to verify all items are displayed on the categories tab."""
    shoppage_instance.verify_all_items_on_shopping_flipkart_subcategory()


@when("I navigate to the my orders tab")
@allure.step("When I navigate to the my orders tab")
def navigate_to_my_orders_tab(shoppage_instance):
    """Step to navigate to the my orders tab."""
    shoppage_instance.navigate_to_my_orders_tab()


@then("I verify all items are displayed on the my orders tab")
@allure.step("Then I verify all items are displayed on the my orders tab")
def verify_all_items_are_displayed_on_the_my_orders_tab(shoppage_instance):
    """Step to verify all items are displayed on the my orders tab."""
    shoppage_instance.verify_all_items_on_my_orders_tab()


# ======== Search page Validation ========


@when("I click on search icon")
@allure.step("When I click on search icon")
def click_on_search_icon(shoppage_instance, searchpage_instance):    # noqa:E501
    """Step to click on the search icon."""
    shoppage_instance.click_on_shop_icon()
    searchpage_instance.click_search_icon()


@when(parsers.parse("I enter the {input} in the search field"))
@allure.step("When I enter the {input} in the search field")
def enter_the_input_in_the_search_field(searchpage_instance, input):
    """Step to enter the input in the search field."""
    searchpage_instance.enter_search_input(input)


@then("I verify no search results are displayed")
@allure.step("Then I verify no search results are displayed")
def verify_no_search_results_are_displayed(searchpage_instance):
    """Step to verify no search results are displayed."""
    no_search_results = searchpage_instance.verify_no_search_results_are_displayed()    # noqa:E501
    assert no_search_results, "Search results are displayed"


@then("I verify expected content are displayed for flipkart")
@allure.step("Then I verify expected content are displayed for flipkart")
def verify_expected_content_are_displayed_for_flipkart(searchpage_instance):
    """Step to verify the expected content for flipkart."""
    flipkart_results = searchpage_instance.verify_search_results_displayed_for_flipkart()   # noqa:E501
    assert flipkart_results, "Expected contents are not displayed for flipkart"


'''@then("I verify expected content are displayed for amazon")
@allure.step("Then I verify expected content are displayed for amazon")
def verify_expected_content_are_displayed_for_amazon(searchpage_instance):
    """Step to verify the expected content for amazon."""
    amazon_results = searchpage_instance.verify_search_results_displayed_for_amazon()     # noqa:E501
    assert amazon_results, "Expected contents are not displayed for amazon"'''


@then("I click on Flipkart Search Results")
@allure.step("Then I click on Flipkart Search Results")
def verify_click_search(searchpage_instance):
    """Step to click on the Flipkart search results."""
    searchpage_instance.verify_click_search()

# ==== Add to cart Journey with Product Page Validation from search page====


@when("I Verify the Product Title, Price, Discount and OutofStock Tag")
@allure.step("When I Verify the Product Title, Price, Discount and OutofStock Tag")  # noqa:E501
def verify_product_title_price_discount_outofstock_tag(pdpflipkart_instance):
    pdpflipkart_instance.verify_product_title_price_discount()


@when("I Verify the Product details")
@allure.step("When I Verify the Product details")
def verify_product_details(pdpflipkart_instance):
    pdpflipkart_instance.verify_product_details()


@when("I Verify the buying quantity")
@allure.step("When I Verify the buying quantity")
def verify_buying_quantity(pdpflipkart_instance):
    pdpflipkart_instance.verify_buying_quantity()


@when('I scroll to the element with text product details')
@allure.step('When I scroll to the element with text product details')
def scroll_to_element(androidactions_instance):
    """Step to scroll to an element by text."""
    androidactions_instance.scroll_into_view("product details")


@when('I scroll to the element with text ratings and reviews')
@allure.step('When I scroll to the element with text ratings and reviews')
def scroll_to_element(androidactions_instance):
    """Step to scroll to an element by text."""
    androidactions_instance.scroll_into_view("ratings and reviews")


@when('I scroll to the element with text similar products comparison')
@allure.step('When I scroll to the element with text similar products comparison')        # noqa:E501
def scroll_to_element(androidactions_instance):
    """Step to scroll to an element by text."""
    androidactions_instance.scroll_into_view("similar products comparison")


@when('I scroll to the element with text out of stock')
@allure.step('When I scroll to the element with text out of stock')
def scroll_to_element(androidactions_instance):
    """Step to scroll to an element by text."""
    androidactions_instance.scroll_into_view("out of stock")


@then("I Verify more details after the swipe")
@allure.step("Then I Verify more details after the swipe")
def verify_more_details_after_swipe(pdpflipkart_instance):
    pdpflipkart_instance.verify_more_details()


@then("I Verify the Ratings and Review Section")
@allure.step("Then I Verify the Ratings and Review Section")
def verify_ratings_and_reviews_section(pdpflipkart_instance):
    pdpflipkart_instance.verify_ratings_and_reviews()


@then("I Verify more similar products comparison section")
@allure.step("Then I Verify more similar products comparison section")
def verify_similar_products_comparisoion(pdpflipkart_instance):
    pdpflipkart_instance.verify_similar_products_comparision()


@then("I Verify Add to cart and Buy Now CTA button")
@allure.step("Then I Verify Add to cart and Buy Now CTA button")
def verify_add_to_cart_buy_now_cta_button(pdpflipkart_instance):
    pdpflipkart_instance.verify_addtocart_buynow_cta()


@then("I Verify Different Denominations")
@allure.step("Then I Verify Different Denominations")
def verify_add_to_cart_buy_now_cta_button(pdpflipkart_instance):
    pdpflipkart_instance.verify_change_denomination()


@then("I Click on Add To Cart CTA Button")
@allure.step("Then I Click on Add To Cart CTA Button")
def verify_add_to_cart_buy_now_cta_button(pdpflipkart_instance):
    pdpflipkart_instance.verify_click_addto_gotocart_cta()


@then("I Verify the Product details added in the cart")
@allure.step("Then I Verify the Product details added in the cart")
def verify_added_product_details_in_cart(pdpflipkart_instance):
    pdpflipkart_instance.verify_cart_page_product_details()


@then("I verify Order Summary Details")
@allure.step("Then I verify Order Summary Details")
def verify_order_summary_details(pdpflipkart_instance):
    pdpflipkart_instance.verify_cart_page_order_summary()


@then("I verify cart page title and pagination details")
@allure.step("Then I verify cart page title and pagination details")
def verify_order_summary_details(pdpflipkart_instance):
    pdpflipkart_instance.verify_cart_page_pagination()


@when("I click on the Proceed to Buy CTA button")
@allure.step("When I click on the Proceed to Buy CTA button")
def verify_order_summary_details(pdpflipkart_instance):
    pdpflipkart_instance.verify_click_proceed_to_buy_cta()


@then("I verify the delivery address page")
@allure.step("Then I verify the delivery address page")
def verify_delivery_address_page(pdpflipkart_instance):
    pdpflipkart_instance.verify_payment_page()


@when("I click on the Proceed to Payment CTA button")
@allure.step("When I click on the Proceed to Payment CTA button")
def verify_delivery_address_page(pdpflipkart_instance):
    pdpflipkart_instance.verify_proceed_to_payment_cta()


@then("I verify the payment page")
@allure.step("Then I verify the payment page")
def verify_payment_page(pdpflipkart_instance):
    pdpflipkart_instance.verify_credit_debit_card_payment_section()


@then(parsers.parse("I enter the {input} in the credit card field"))
@allure.step("Then I enter the {input} in the credit card field")
def verify_payment_page_details(pdpflipkart_instance, input):
    pdpflipkart_instance.verify_input_cc_number(input)


@then("I verify Convenience Fee Details")
@allure.step("Then I verify Convenience Fee Details")
def verify_payment_page_details(pdpflipkart_instance):
    pdpflipkart_instance.verify_convenience_fee()


@then("I Navigate back to HomePage")
@allure.step("Then I Navigate back to HomePage")
def navigate_back_to_home_page(pdpflipkart_instance):
    pdpflipkart_instance.verify_navigation_to_home_page()
