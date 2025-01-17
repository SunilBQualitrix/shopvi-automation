from pytest_bdd import given, when, then, scenarios, parsers
import allure
import pytest
from pages.base_page import BasePage
from pages.navto_shop import NavtoShop
from pages.shop_dashboard_page import ShopDashboardPage
from pages.search_page import SearchPage
from pages.accountPage import AccountPage

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


# ======== Step Definitions ========

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
@allure.step("Given I open the app and navigate to the mobile number input screen")  
def open_app_and_navigate_to_mobile_number_input_screen(navtoshop_instance):
    """Step to navigate to the mobile number input screen."""
    enter_mobile_number = navtoshop_instance.click_number_input_field()
    assert enter_mobile_number, "Mobile number input screen is not displayed after lanuching the vishop application"


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
    navtoshop_instance.input_otp(otp)


@when("I log into the app using login with OTP CTA button")
@allure.step("When I log into the app using login with OTP CTA button")
def log_into_the_app_using_login_with_otp_cta_button(navtoshop_instance):
    """Step to log in using the OTP."""
    navtoshop_instance.login_wotp_button()


@then("I click on VI Shop from Bottom Navigation and should navigate to the shop Dashboard")  
@allure.step("Then I click on VI Shop from Bottom Navigation and should navigate to the shop Dashboard") 
def click_on_vi_shop_from_bottom_navigation_and_should_navigate_to_the_shop_dashboard(navtoshop_instance, shoppage_instance):
    """Step to navigate to the shop dashboard."""
    navtoshop_instance.navto_shop()
    shop_page_reached = shoppage_instance.verify_shop_dashborad_page()
    assert shop_page_reached, "Shop Dashboard page is not reached"



# ======== Account Page Validation ========

@when("I verify the account button is displayed")
@allure.step("When I verify the account button is displayed")
def verify_account_button_is_displayed(accountpage_instance):
    """Step to verify if the account button is displayed."""
    is_displayed = accountpage_instance.verify_account_button()
    assert is_displayed, "Account button is not displayed."


@when("I click on the account button and navigate to the account page")
@allure.step("When I click on the account button and navigate to the account page")
def click_account_button_and_navigate_to_account_page(accountpage_instance):
    """Step to click the account button and navigate to the account page."""
    clicked = accountpage_instance.click_account_button()
    assert clicked, "Failed to click on the account button and navigate to the account page."


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
    assert navigated, "Failed to navigate to the FAQ page. FAQ element was not displayed."


@then("I verify all elements are displayed on the FAQ page")
@allure.step("Then I verify all elements are displayed on the FAQ page")
def verify_all_elements_on_faq_page(accountpage_instance):
    """Step to verify all elements are displayed on the FAQ page."""
    print("Verifying all elements on the FAQ page...")
    accountpage_instance.verify_and_print_all_elements_on_faq_page()
    print("Verification of FAQ page elements completed.")
    # Navigate back to the previous page
    try:
        accountpage_instance.driver.back()  # Or use faqpage_instance.driver.press_keycode(4)
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
@allure.step("Then I verify all elements are displayed on the Credit Card (CC) page")
def verify_all_elements_on_cc_page(accountpage_instance):
    """Step to verify all elements are displayed on the Credit Card (CC) page."""
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

@when("I navigate to the Profile page")
@allure.step("When I navigate to the Profile page")
def navigate_to_profile_page(accountpage_instance):
    """Step to navigate to the Profile page."""
    navigated = accountpage_instance.verify_nav_to_profile_page()
    assert navigated, "Failed to navigate to the Profile page."
    accountpage_instance.driver.back()

@then("I verify all elements are displayed on the Profile page")
@allure.step("Then I verify all elements are displayed on the Profile page")
def verify_all_elements_on_profile_page(accountpage_instance):
    """Step to verify all elements are displayed on the Profile page."""
    print("Verifying all elements on the Profile page...")
    accountpage_instance.verify_and_print_all_elements_on_profile_page()
    print("Verification of Profile page elements completed.")
    # Navigate back to the previous page
    accountpage_instance.driver.back()
    print("Navigated back from the Profile page successfully.")
    accountpage_instance.driver.back()

@when(("I navigate to Saved Payments page"))
@allure.step("When I navigate to Saved Payments page")
def navigate_to_saved_payments_page(accountpage_instance):
    """Step to navigate to the Saved Payments page."""
    navigated = accountpage_instance.verify_nav_to_saved_payments_page()
    assert navigated, "Failed to navigate to the Saved Payments page."
    accountpage_instance.driver.back()

@then("I Verify all elements are displayed on the Saved Payments page")
@allure.step("Then I Verify all elements are displayed on the Saved Payments page")
def verify_all_elements_on_saved_payments_page(accountpage_instance):
    """Step to verify all elements on the Saved Payments page."""
    print("Verifying all elements on the Saved Payments page...")
    accountpage_instance.verify_and_print_all_elements_on_saved_payments_page()
    print("Verification of Saved Payments page elements completed.")
    # Navigate back to the previous page
    print("Navigated back from the Saved Payments page successfully.")







# ======== Search Page Validation ========

@when("I am on shop dashboard and verify search icon is displayed in shop Dashboard")
@allure.step("When I am on shop dashboard and verify search icon is displayed in shop Dashboard")
def open_the_shop_tab_and_verify_search_icon_is_displayed_in_shop_page(searchpage_instance):
    """Step to verify the search icon is displayed."""
    search_icon_displayed = searchpage_instance.verify_search_icon()
    assert search_icon_displayed, "Search icon is not displayed in the shop page"


@then("I open the explore tab and verify search icon is displayed in explore page")
@allure.step("Then I open the explore tab and verify search icon is displayed in explore page")
def open_the_explore_tab_and_verify_search_icon_is_displayed_in_explore_page(shoppage_instance, searchpage_instance):
    """Step to verify the search icon is displayed."""
    shoppage_instance.navigate_to_explore_tab()
    search_icon_displayed = searchpage_instance.verify_search_icon()
    assert search_icon_displayed, "Search icon is not displayed in the explore page"


@then("I open the my orders tab and verify search icon is displayed in my orders page")
@allure.step("Then I open the my orders tab and verify search icon is displayed in my orders page")
def open_the_my_orders_tab_and_verify_search_icon_is_displayed_in_my_orders_page(shoppage_instance, searchpage_instance):
    """Step to verify the search icon is displayed."""
    shoppage_instance.navigate_to_my_orders_tab()
    search_icon_displayed = searchpage_instance.verify_search_icon()
    assert search_icon_displayed, "Search icon is not displayed in the my orders page"


@when("I click on search icon")
@allure.step("When I click on search icon")
def click_on_search_icon(shoppage_instance,searchpage_instance):
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
    no_search_results = searchpage_instance.verify_no_search_results_are_displayed()
    assert no_search_results, "Search results are displayed"


@then("I verify expected content are displayed for flipkart")
@allure.step("Then I verify expected content are displayed for flipkart")
def verify_expected_content_are_displayed_for_flipkart(searchpage_instance):
    """Step to verify the expected content for flipkart."""
    flipkart_results = searchpage_instance.verify_search_results_displayed_for_flipkart()
    assert flipkart_results, "Expected contents are not displayed for flipkart"


@then("I verify expected content are displayed for amazon")
@allure.step("Then I verify expected content are displayed for amazon")
def verify_expected_content_are_displayed_for_amazon(searchpage_instance):
    """Step to verify the expected content for amazon."""
    amazon_results = searchpage_instance.verify_search_results_displayed_for_amazon()
    assert amazon_results, "Expected contents are not displayed for amazon"
