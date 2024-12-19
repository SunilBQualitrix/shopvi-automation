from pytest_bdd import given, when, then, scenarios, parsers
import allure
from pages.base_page import BasePage
from pages.NavtoShop import NavtoShop
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))  # noqa:E501


scenarios('../features/Shoptests.feature')


@given(parsers("I install vishop {application}"))
@allure.step('Given I install vishop {application}')
def install_vishop_application(setup_platform):
    basePage = BasePage(setup_platform)


@given("I launch Screener Application")
@allure.step("Given I launch Screener Application")
def launch_GD_application(setup_platform):
    print("Launch screener application")
    print('what is webdriver instance =====', type(setup_platform))
    basePage = BasePage(setup_platform)
    basePage.launchApp()


@given('I open the app and navigate to the mobile number input screen')
def step_open_app_and_navigate(context):
    context.navtoshop = NavtoShop(context.driver)
    context.navtoshop.click_number_input_field()


@when('I close the mobile number dialog box')
def step_confirm_number_in_dialog(context):
    context.navtoshop.click_dialog_box()


@when('I input a valid 10-digit mobile number "{mobile_number}"')
def step_input_mobile_number(context, mobile_number):
    context.navtoshop.input_valid_mobilenumber(mobile_number)


@when('I click on the send OTP CTA button')
def step_click_otp_button(context):
    context.navtoshop.click_otp_button()


@when('I input a valid 4-digit OTP "{otp}"')
def step_input_otp(context, otp):
    context.navtoshop.input_otp(otp)


@when('I log into the app using login with OTP CTA button')
def step_log_in_with_otp(context):
    context.navtoshop.login_wotp_button()


@then('I click on VI Shop from Bottom Navigation and should navigate to the shop Dashboard')  # noqa:E501
def step_navigate_to_shop(context):
    context.navtoshop.navto_shop()
