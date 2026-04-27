from pages.actions.android_actions import AndroidActions
from appium import webdriver


keycodes = {
    "KEYCODE_DPAD_UP": 19,
    "KEYCODE_DPAD_DOWN": 20,
    "KEYCODE_DPAD_LEFT": 21,
    "KEYCODE_DPAD_RIGHT": 22,
    "KEYCODE_DPAD_ENTER": 66,
    "KEYCODE_DEL": 67,
    "KEYCODE_DPAD_CENTER": 23,
    "KEYCODE_BACK": 4,
    "KEYCODE_MENU": 82
}


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.actions = None
        self.keys = keycodes
        self.platform_name = None
        self.appPackage = None

        if isinstance(driver, webdriver.Remote):
            print("Application Launched")

            capabilities = driver.capabilities
            self.platform_name = capabilities.get('platformName', '').lower()
            self.appPackage = capabilities.get('appium:appPackage')

            if self.platform_name == 'android':
                print("Inside Android")
                self.actions = AndroidActions(driver)

    # 🔹 USED ONLY WHEN YOU WANT TO ENSURE APP IS ACTIVE
    def launchApp(self, appPackage=None):
        print("Inside launchApp")

        if not isinstance(self.driver, webdriver.Remote):
            print("Driver not valid")
            return

        if appPackage is None:
            appPackage = self.appPackage

        if self.platform_name == 'android':
            try:
                current_package = self.driver.current_package
                if current_package == appPackage:
                    print(f"App {appPackage} is already active")
                    return
                else:
                    print(f"Activating app: {appPackage}")
                    self.driver.activate_app(appPackage)
            except Exception as e:
                print(f"Error in launchApp: {e}")
            except Exception as e:
                print(f"Error launching app: {e}")

    # 🔹 FORCE RELAUNCH (USED AFTER FAILURE / RESET STATE)
    def relaunchApp(self, appPackage):
        print("Inside relaunchApp")

        if not isinstance(self.driver, webdriver.Remote):
            print("Driver not valid")
            return

        if self.platform_name == 'android':
            try:
                print(f"Terminating app: {appPackage}")
                self.driver.terminate_app(appPackage)
            except Exception as e:
                print(f"Terminate failed, fallback to adb: {e}")

            try:
                print(f"Re-activating app: {appPackage}")
                self.driver.activate_app(appPackage)
            except Exception as e:
                print(f"Activation failed: {e}")

    # 🔹 OPTIONAL HELPER (VERY USEFUL)
    def is_app_installed(self, appPackage):
        if self.platform_name == 'android':
            try:
                return self.driver.is_app_installed(appPackage)
            except Exception as e:
                print(f"Error checking app install: {e}")
        return False
