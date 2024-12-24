from pytest_bdd import given, when, then, scenarios, parsers
import allure
import pytest
from pages.base_page import BasePage
from pages.navto_shop import NavtoShop

import sys
import os

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


# ======== Step Definitions ========

@given(parsers.parse("I install vishop {application}"))
@allure.step("Given I install vishop {application}")
def install_vishop_application(basepage_instance, application):
    """Step to simulate installing the application."""
    print(f"Installing application: {application}")


@given("I launch vishop Application")
@allure.step("Given I launch vishop Application")
def launch_screener_application(basepage_instance):
    """Step to launch the Screener application."""
    print("Launching Screener application...")
    basepage_instance.launchApp()


@given("I open the app and navigate to the mobile number input screen")
@allure.step("Given I open the app and navigate to the mobile number input screen")  # noqa:E501
def step_open_app_and_navigate(navtoshop_instance):
    """Step to navigate to the mobile number input screen."""
    navtoshop_instance.click_number_input_field()


@when("I close the mobile number dialog box")
@allure.step("When I close the mobile number dialog box")
def step_confirm_number_in_dialog(navtoshop_instance):
    """Step to close the dialog box."""
    navtoshop_instance.click_dialog_box()


@when(parsers.parse("I input a valid 10-digit mobile number \"{mobile_number}\""))  # noqa:E501
@allure.step("When I input a valid 10-digit mobile number {mobile_number}")
def step_input_mobile_number(navtoshop_instance, mobile_number):
    """Step to input a valid mobile number."""
    navtoshop_instance.input_valid_mobilenumber(mobile_number)


@when("I click on the send OTP CTA button")
@allure.step("When I click on the send OTP CTA button")
def step_click_otp_button(navtoshop_instance):
    """Step to click on the OTP button."""
    navtoshop_instance.click_otp_button()


@when(parsers.parse("I input a valid 4-digit OTP \"{otp}\""))
@allure.step("When I input a valid 4-digit OTP {otp}")
def step_input_otp(navtoshop_instance, otp):
    """Step to input a valid OTP."""
    navtoshop_instance.input_otp(otp)


@when("I log into the app using login with OTP CTA button")
@allure.step("When I log into the app using login with OTP CTA button")
def step_log_in_with_otp(navtoshop_instance):
    """Step to log in using the OTP."""
    navtoshop_instance.login_wotp_button()


@then("I click on VI Shop from Bottom Navigation and should navigate to the shop Dashboard")  # noqa:E501
@allure.step("Then I click on VI Shop from Bottom Navigation and should navigate to the shop Dashboard")  # noqa:E501
def step_navigate_to_shop(navtoshop_instance):
    """Step to navigate to the shop dashboard."""
    navtoshop_instance.navto_shop()
    assert navtoshop_instance.is_dashboard_visible(), "Failed to navigate to Shop Dashboard"  # noqa:E501
