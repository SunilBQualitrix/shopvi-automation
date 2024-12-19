# from appium import webdriver
import random
import time
# from appium.webdriver.common.touch_action import TouchAction
# from selenium.webdriver.common.by import By
# from appium.webdriver.common.appiumby import AppiumBy
# from selenium.webdriver.common.by import By
import allure
from allure_commons.types import AttachmentType
import requests
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException   # noqa:E501
from pages.actions.actions_parent import ActionsParent
from conftest import readConstants


# from appium import webdriver
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# # from webdriver_manager.chrome import ChromeDriverManager


class AndroidActions(ActionsParent):

    def __init__(self, driver):
        self.driver = driver
        self.ultra_wait = WebDriverWait(self.driver, readConstants("ULTRA_WAIT"))
        self.short_wait = WebDriverWait(self.driver, readConstants("SHORT_WAIT"))
        print("long wait ===", readConstants("LONG_WAIT"))
        self.wait = WebDriverWait(self.driver, readConstants("DEFAULT_WAIT"))
        self.long_wait = WebDriverWait(self.driver, readConstants("LONG_WAIT"))
        self.super_wait = WebDriverWait(self.driver, readConstants("SUPER_WAIT"))
        self.dynamic_number = random.randint(1, 10000)

    def launch_app(self):
        print("firestaick app is already launched")

    def relaunch_app(self, appPackage):
        print("firestaick app is already launched")
        self.driver.activate_app(appPackage)

    def fluentWaitNew(self, ele, secs):
        WebDriverWait(self.driver, 60, poll_frequency=secs).until(EC.visibility_of_element_located(ele), 'Error')

    def screenshotAttachment(self, ScreenshotName):
        doIneedScreenshot = readConstants("NEED_SCREENSHOTS_FOR_PASS")
        print("want to take scrrenshot after sending values ", doIneedScreenshot)
        if str(doIneedScreenshot).lower() == 'true':
            allure.attach(self.driver.get_screenshot_as_png(), name=ScreenshotName, attachment_type=AttachmentType.PNG)

    def wait_for_element(self, locator, value, timeout=60):
        """
        Waits for an element to be present on the page.
        Arguments:
        locator - Locator strategy.
        value - Locator value.
        timeout - Maximum time to wait (default is 60 seconds).
        Returns : WebElement if found; WebDriver if not found.
        """
        print("Waiting for Element", value)
        again = 1
        while again < 3:
            try:

                return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((locator, value)))
            except NoSuchElementException:
                print("Inside no such element")
                return None

            except StaleElementReferenceException:
                # self.driver.refresh()
                again += 1
                print("Stale element, refreshed, trying again")
            except TimeoutError:
                again = 3
                print("Element not present")
                return self.driver

    def wait_for_elements(self, locator, value, timeout=60):
        """
        Waits for all elements to be present on the page.
        Arguments:
        locator - Locator strategy.
        value - Locator value.
        timeout - Maximum time to wait (default is 60 seconds).
        Returns : WebElement if found; WebDriver if not found.
        """
        print("Waiting for Element", timeout)
        again = 1
        while again < 3:
            try:
                return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located((locator, value)))
            except NoSuchElementException:
                print("Inside no such element")
                return None

            except StaleElementReferenceException:
                # self.driver.refresh()
                again += 1
                print("Stale element, refreshed, trying again")
            except TimeoutException:
                again = 3
                print("TimeoutException: Element not present")
                return None
            except Exception:
                print("Exception occured")

    def enter_text(self, locator_type, locator_value, text):
        """
        Enters text into an input field identified by the locator.
        Arguments:
        locator_type - Locator strategy.
        locator_value - Locator value.
        text - Text to enter into the input field.
        """
        print("passing locator_type", locator_type)

        try_count = 1
        while try_count < 5:
            try:
                print("locator_value  to enter_text ===", locator_value)
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((locator_type, locator_value)))
                print("typeing values ===", text)
                self.screenshotAttachment("element_before_clear_{}.jpg".format(self.dynamic_number))
                element.clear()
                self.screenshotAttachment("element_cleared.jpg_{}.jpg".format(self.dynamic_number))
                element.send_keys(text)
                self.screenshotAttachment("element_dataset_{}.jpg".format(self.dynamic_number))
                break
            except TimeoutException:
                self.screenshotAttachment("element_not_found_Timeout_Exception.jpg")
                print("Element Is Not Found To Perform Click Action Due To Timeout, Trying again after 2 seconds")
                try_count = try_count + 1
            except NoSuchElementException:
                self.screenshotAttachment("element_not_found_NoSuchElementException.jpg")

                print(
                    "Element Is Not Found To Perform Click Action Due To NoSuchElementException, Trying again after 2 seconds")

                try_count = try_count + 1
            except ElementClickInterceptedException:
                self.screenshotAttachment("element_not_clickable.jpg")
                print("Click was itercepted, Trying again after 2 seconds")
                try_count = try_count + 1
                # self.long_wait.until(EC.element_to_be_clickable(ele)).click()
            except StaleElementReferenceException:
                print("Stale element, refreshed, trying again")
                # self.driver.refresh()
                try_count += 1

    def click_button(self, locator_type, locator_value):
        """
        Clicks a button identified by the locator.
        Arguments:
        locator_type - Locator strategy.
        locator_value - Locator value.
        """
        print("passing locator_type", locator_type)

        try_count = 1
        while try_count < 5:
            try:

                element = self.long_wait.until(
                    EC.element_to_be_clickable(self.driver.find_element(locator_type, locator_value)))
                print("*****  Click element: ", locator_type, locator_value, element)
                self.screenshotAttachment("element_clickable_{}.jpg".format(self.dynamic_number))
                element.click()
                self.screenshotAttachment("after_element_click_{}.jpg".format(self.dynamic_number))

                # if(name!="Element"):
                #     print("Clicked on " + locator_value)
                break
            except TimeoutException:

                self.screenshotAttachment(
                    "element_not_clickable_NoSuchElementException{}.jpg".format(self.dynamic_number))

                print("Element Is Not Found To Perform Click Action Due To Timeout, Trying again after 2 seconds")
                try_count = try_count + 1
            except NoSuchElementException:
                self.screenshotAttachment("element_not_clickable_NoSuchElementException.jpg")

                print(
                    "Element Is Not Found To Perform Click Action Due To NoSuchElementException, Trying again after 2 seconds")

                try_count = try_count + 1
            except ElementClickInterceptedException:
                self.screenshotAttachment("element_not_clickable.jpg")
                print("Intercepted click_button, Trying again after 2 seconds")
                try_count = try_count + 1
                # self.long_wait.until(EC.element_to_be_clickable(ele)).click()
            except StaleElementReferenceException:
                print("Stale element, refreshed, trying again")
                # self.driver.refresh()
                try_count += 1

    def close_app(self):
        """
        Closes the application.
        """
        self.driver.close_app()

    # def move_to(self, locator_type, locator_value):
    #     """
    #     Moves the touch action to an element identified by the locator.
    #     Arguments:
    #     locator_type - Locator strategy.
    #     locator_value - Locator value.
    #     """
    #     element = self.driver.find_element(locator_type, locator_value)
    #     action = TouchAction(self.driver)
    #     action.move_to(element).perform()

    def open_app(self):
        """
        Closes the application.
        """
        self.driver.launch_app()

    def quit_Driver(self):
        self.driver.quit()

    def open_url(self, url):
        """
        Opens the specified URL in the web browser.
        Arguments:
        url - The URL to open in the web browser.
        """
        # self.driver.get(url)
        self.driver.get(url)

    def maximize_Window(self):
        """
        Maximizes the window
        """
        self.driver.maximize_window()

    def is_element_text_matches(self, locator: tuple[str, str], text: str) -> bool:

        return self.wait.until(EC.text_to_be_present_in_element(locator, text))

    def get_element_text(self, locator) -> str | None:
        """

        """
        ele_text: str | None = None

        try:
            element: WebElement | None = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(locator))
            ele_text = element.text
        except NoSuchElementException:
            self.screenshotAttachment("element_text_not_found.jpg")
        except StaleElementReferenceException:
            self.screenshotAttachment("stale_text_element.jpg")
        except Exception as e:
            pass

        return ele_text



    def get_text(self, locator_type, locator_value):
        """
        Retrieves the text of an element identified by the locator.
        Arguments:
        locator_type - Locator strategy.
        locator_value - Locator value.
        Returns : string - The text content of the located element.
        """
        try_count = 1
        while try_count < 5:
            try:
                print("before wait stattement===", locator_type)
                self.long_wait.until(EC.presence_of_element_located((locator_type, locator_value)))
                # self.long_wait.until(EC.visibility_of_element_located((By.ID, locator_value)))
                # WebDriverWait(self.driver, readConstants("LONG_WAIT")).until(EC.visibility_of_element_located((locator_type, locator_value)))
                print("waiting for element to fetch text")
                time.sleep(10)
                element = self.driver.find_element(locator_type, locator_value)
                self.screenshotAttachment("element_gettingText_{}.jpg".format(self.dynamic_number))
                print("fetching text from app ====", element.text)
                return element.text
                break
            except NoSuchElementException:
                self.screenshotAttachment("element_not_found.jpg")
                print("Click was itercepted to get_text, Trying again after 2 seconds")
                try_count = try_count + 1
                # self.long_wait.until(EC.element_to_be_clickable(ele)).click()
            except StaleElementReferenceException:
                print("Stale element, refreshed, trying again")
                # self.driver.refresh()
                try_count += 1

    # def press(self, locator_type, locator_value):
    #     """
    #     Presses on an element identified by the locator.
    #     Arguments:
    #     locator_type - Locator strategy.
    #     locator_value - Locator value.
    #     """
    #     element = self.long_wait.until(EC.visibility_of_element_located(locator_type, locator_value))
    #     # self.long_wait.until(EC.visibility_of(element)).click()
    #     # element = self.driver.find_element(locator_type, locator_value)
    #     action = TouchAction(self.driver)
    #     action.press(element).release().perform()

    # def trigger_back_button_event(self, locator_type, locator_value):
    #     element = self.driver.find_element(locator_type, locator_value)
    #     element.press_keycode(4)

    # def scroll(self, start_locator_type, start_locator_value, end_locator_type, end_locator_value):
    #     """
    #     Scrolls from one element to another.
    #     Arguments:
    #     start_locator_type: Locator strategy for the starting element.
    #     start_locator_value: Locator value for the starting element.
    #     end_locator_type: Locator strategy for the ending element.
    #     end_locator_value: Locator value for the ending element.
    #     """
    #     start_element = self.driver.find_element(start_locator_type, start_locator_value)
    #     end_element = self.driver.find_element(end_locator_type, end_locator_value)
    #     action = TouchAction(self.driver)
    #     action.press(start_element).move_to(end_element).release().perform()

    # deprivated, wil use abstract method enter_text
    # def set_text(self, locator_type, locator_value, text):
    #     """
    #     Clears and sets text in an input field identified by the locator.
    #     Arguments:
    #     locator_type - Locator strategy.
    #     locator_value - Locator value.
    #     text - Text to enter into the input field.
    #     """
    #     print("in android  settings chaange sedndi gvalue as ====", text)
    #     element = self.long_wait.until(EC.element_to_be_clickable(self.driver.find_element(locator_type, locator_value)))
    #     # element = self.driver.find_element(locator_type, locator_value)
    #     element.clear()
    #     print("in android  settings chaange sedndi after clear", text)
    #     element.send_keys(text)

    def suspend_app(self, seconds):
        """
        Suspends the app for a specified duration.
        Arguments:
        seconds - Duration to suspend the app, in seconds.
        """
        self.driver.background_app(seconds)

    def swipe(self, start_x, start_y, end_x, end_y, duration=800):
        """
        Performs a swipe gesture from one coordinate to another.
        Arguments:
        start_x - Starting X coordinate.
        start_y - Starting Y coordinate.
        end_x - Ending X coordinate.
        end_y - Ending Y coordinate.
        duration - Duration of the swipe in milliseconds (default is 800).
        """
        self.screenshotAttachment("element_before_swipe_{}.jpg".format(self.dynamic_number))
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)
        self.screenshotAttachment("element_after_swipe.jpg")

    # def tap(self, locator_type, locator_value):
    #     """
    #     Taps a button identified by the locator.
    #     Arguments:
    #     locator_type - Locator strategy.
    #     locator_value - Locator value.
    #     """
    #     self.screenshotAttachment("element_before_tap_{}.jpg".format(self.dynamic_number))
    #     element = self.driver.find_element(locator_type, locator_value)
    #     action = TouchAction(self.driver)
    #     action.tap(element).perform()

    def validate_element_visitbilty_within_time(self, locator_type, locator_value, duration):
        """
        Checks if an element is visible within the specified time frame.
        Arguments:
        locator_type - Locator strategy.
        locator_value - Locator value.
        duration - Maximum time to wait for visibility, in seconds.
        Returns : True if the element is visible within the duration; False otherwise.
        """
        start_time = time.time()  # Record the start time
        print("checking element loading with in given time frame", duration, locator_type, locator_value)
        print("my driver is ==", type(self.driver))
        try:
            # Wait up to 30 seconds for the element to be visible
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((locator_type, locator_value))
            )
            end_time = time.time()  # Record the end time

            load_time = end_time - start_time
            print("Element loaded in: {:.2f} seconds".format(load_time))  # Format to 2 decimal places
            element = self.driver.find_element(locator_type, locator_value)
            print('is the element is found===', type(element))
            print('is the element is displayed?===', element.is_displayed)
            return element.is_displayed

        except TimeoutException:
            print("Element is not visible within {} seconds".format(duration))
            return False
        except Exception as e:
            print("Element is not visible within", e)
            return False

    def get_element_visibility(self, locator_type, locator_value):
        """
        Checks if an element is visible on the page within a 10-second timeout.
        Arguments:
        locator_type - Locator strategy.
        locator_value - Locator value.
        Returns : True if the element is visible; False otherwise.
        """
        try:
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((locator_type, locator_value))
            )
            return True
        except TimeoutException:
            return False
        except Exception as e:
            print("Element is not visible within", e)
            return False

    def is_element_displayed(self, locator_type, locator_value):
        """
        Checks if an element is displayed on the page.
        Arguments:
        locator_type - Locator strategy.
        locator_value - Locator value.
        Returns : True if the element is displayed; False otherwise.
        """
        try:
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((locator_type, locator_value)))
            # self.driver.find_element(locator_type, locator_value)
            self.screenshotAttachment("element_displyed_{}.jpg".format(self.dynamic_number))
            return True
        except TimeoutException:
            print("TimeoutException")
            return False
        except Exception as e:
            print("Element is not visible within", e)
            return False


    def validate_text(self, locator_type, locator_value, expected_text):
        """
        Validates if the text of an element matches the expected text.
        Arguments:
        locator_type - Locator strategy.
        locator_value - Locator value.
        expected_text - Expected text to match.
        Returns : True if the actual text matches the expected text; False otherwise.
        """
        again = 1
        actual_text = None
        while again < 3:
            # BasePage.fluentWait(self,ele,3)
            try:
                print(" message expected========", expected_text)
                # print("error locator_type========", locator_type)
                # print("error locator_value========", locator_value)
                self.wait_for_element(locator_type, locator_value, 30)
                element = WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((locator_type, locator_value))
                )
                print("text  element========", element.is_displayed())
                actual_text = element.text
                print(" message i have read ========", actual_text)
                self.screenshotAttachment("element_text_{}.jpg".format(self.dynamic_number))
                return actual_text == expected_text
            except NoSuchElementException:
                print("Inside no such element")
                return actual_text

            except StaleElementReferenceException:
                # self.driver.refresh()
                again += 1
                print("Stale element, refreshed, trying again")
            except TimeoutError:
                again = 3
                print("Element not present")
                return False

            except TimeoutException:
                isVerify = False
                print("Inside timeout exception")
                return isVerify

    def validate_text_contains(self, by, value, expected_text):
        """
        Checks if the text of an element contains the expected text.
        Arguments:
        by - Locator strategy.
        value - Locator value.
        expected_text - Expected text to match.
        Returns : True if the expected text is found within the element's text; False otherwise.
        """
        print("Inside validate text")
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((by, value))
        )
        # print(element)
        actual_text = element.get_attribute("text")
        self.screenshotAttachment("element_actual_text_{}.jpg".format(self.dynamic_number))
        print("actual_text====", actual_text)
        print("expected_text====", expected_text)
        if expected_text.lower() in actual_text.lower():
            return True
        else:
            return False

    def is_checkbox_checked(self, locator_type, locator_value):
        """
        Checks if a checkbox element is selected.
        Arguments:
        locator_type - Locator strategy.
        locator_value - Locator value.
        Returns : True if the checkbox is selected; False otherwise.
        """
        try:
            # Locate the checkbox element
            checkbox = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((locator_type, locator_value)))
            self.screenshotAttachment("checkbox_status_{}.jpg".format(self.dynamic_number))
            checkbosStatus = checkbox.is_selected()
            print("what is login page check box status ====", checkbosStatus)
            # Check if the checkbox is selected
            return checkbosStatus
        except (NoSuchElementException, TimeoutException):
            # If the element is not found or there's a timeout, return False
            return False