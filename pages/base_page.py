from pages.actions.android_actions import AndroidActions
from appium import webdriver


keycodes = {
    "KEYCODE_DPAD_UP": 19,  # up arrow key
    "KEYCODE_DPAD_DOWN": 20,   # Down arrow key
    "KEYCODE_DPAD_LEFT": 21,   # Left arrow key
    "KEYCODE_DPAD_RIGHT": 22,   # Right arrow key
    "KEYCODE_DPAD_ENTER": 66,   # Enter key
    "KEYCODE_DEL": 67,  # delete key
    "KEYCODE_DPAD_CENTER": 23,  # OK button
    "KEYCODE_BACK": 4,  # Back button
    "KEYCODE_MENU": 82  # Menu button
}


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        if isinstance(driver, webdriver.Remote):
            print("Application Launched")
            self.driver = driver
            capabilities = driver.capabilities
            platform_name = capabilities.get('platformName', '').lower()
            if platform_name == 'android':
                print('Inside Android')
                self.actions = AndroidActions(driver)
                self.keys = keycodes

    def launchApp(self):
        print("what is driver type in basepage", isinstance(self.driver, webdriver.Remote))  # noqa:E501
        if isinstance(self.driver, webdriver.Remote):
            self.driver = self.driver
            capabilities = self.driver.capabilities
            platform_name = capabilities.get('platformName', '').lower()
            if platform_name == 'android':
                print("Launching vi shop ==launchApp basepage")
                self.actions = AndroidActions(self.driver)
                print("initialise android actions=====")

    def relaunchApp(self, appPackage):
        print("tryign to relaunch app =============")
        print("what is driver type in basepage", isinstance(self.driver, webdriver.Remote))  # noqa:E501
        if isinstance(self.driver, webdriver.Remote):
            self.driver = self.driver
            capabilities = self.driver.capabilities
            platform_name = capabilities.get('platformName', '').lower()
            if platform_name == 'android':
                print("KLaunching GD App in fireTV ==launchApp basepage")
                self.actions = AndroidActions(self.driver)
                self.actions.relaunch_app(appPackage)
                print("initialise android actions=====")
