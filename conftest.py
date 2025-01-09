import base64
import http
from email.policy import default
from http.client import RemoteDisconnected
import platform
import socket
import subprocess
# import time
import allure
from bs4 import BeautifulSoup
import psutil
import pytest
from appium import webdriver as androidDriver
from selenium import webdriver
from appium.webdriver.appium_service import AppiumService
from allure_commons.types import AttachmentType
from selenium import webdriver
from requests.auth import HTTPDigestAuth
import re
import urllib3
import wget
import logging
# from src.app.application import Application
# from appium.webdriver.common.appiumby import AppiumBy
# from appium.webdriver.webdriver import AppiumOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium import webdriver as browserDriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import os
from pathlib import Path
import time
import zipfile
import signal

import json
import stat

import requests
from urllib3.util.retry import Retry

session = requests.Session()
retry = Retry(
    total=5,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504, 401],
)


def pytest_addoption(parser):
    parser.addoption(
        "--platform", action="store", default="android", help="platform to run test (Android)"  # noqa:E501
    )
    parser.addoption("--consecutive_failure_abort", default="true", action="store")
    parser.addoption("--consecutive_failure_count", default="5", action="store") #top stop the failures after 5runs
    parser.addoption("--appFileName", action="store")
    parser.addoption("--app_package_name", action="store")
    parser.addoption("--app_activity", action="store")
    parser.addoption("--screenShotToggle", default=True, action="store")
    parser.addoption("--enable_screen_recording", action="store_true", default=True, help='Enable screen recording')

@pytest.fixture(scope="session", autouse=True)
def env(request):
    """
        Fixture for setting up the testing environment.
    """
    return request.config.getoption("--platform")

def load_capabilities(config_name):
    print('config_name want to fetch ', config_name)
    project_root = os.getcwd()
    # os.path.dirname(os.path.dirname(__file__))
    print('project_root', project_root)
    config_path = os.path.join(project_root, 'utils', 'platformconfig.json')
    print('config_path', config_path)
    with open(config_path, 'r', encoding='utf-8') as config_file:
        config = json.load(config_file)
        # print('reading full config file ', config)
    return config.get(config_name, {})


def readConstants(constant_key):
    project_root = os.getcwd()
    constants_path = os.path.join(project_root, 'utils', 'constants.json')
    with open(constants_path) as constant_file:
        costant_value = json.load(constant_file)
        # print('reading full config file ', config)
    return costant_value.get(constant_key)


def readPreReqJson(prereqFileName, constant_key):
    project_root = os.getcwd()
    data_file_path = os.path.join(project_root, 'utils', prereqFileName + ".json")
    with open(data_file_path, 'r', encoding='utf-8') as constant_file:
        costant_value = json.load(constant_file)
    return costant_value.get(constant_key)


def fetchMultipleKeysFromJsonValue(prereqFileName, constant_key):
    project_root = os.getcwd()
    data_file_path = os.path.join(project_root, 'utils', prereqFileName + ".json")
    with open(data_file_path, 'r', encoding='utf-8') as constant_file:
        json_data = json.load(constant_file)
    matching_values = [value for key, value in json_data.items() if key.startswith(constant_key)]
    print("fetching mutiple matching ====", matching_values)
    return matching_values
    

def readPreReqJsonValue(prereqFileName, constant_key):
    project_root = os.getcwd()
    data_file_path = os.path.join(project_root, 'utils', prereqFileName + '.json')
    with open(data_file_path, 'r', encoding='utf-8') as constant_file:
        costant_value = json.load(constant_file)
    input_value = costant_value.get(constant_key)
    print("constant_key  i am reading is ===", constant_key)
    if input_value is not None:
        print("found value for key {} in prereq ".format(constant_key))
        return costant_value.get(constant_key)
    else:
        print("No value  so return key ")
        return constant_key


def screenshotAttachment(self, ScreenshotFileName):
    doIneedScreenshot = readConstants("NEED_SCREENSHOTS_FOR_PASS")
    print("will look for roku scrrens shots")
    appToLaunch = readConstants("ROKU_CURRENT_APP_FILENAME")
    print("appToLaunch   current roku app ful path==", appToLaunch)

    url = "http://{}/plugin_inspect".format(readConstants("roku_ip"))
    payload = {'mysubmit': 'Screenshot', 'passwd': readConstants("rokuPass")}
    with open(appToLaunch, 'rb') as f:
        RokuAppfiles = [('archive', ('file', open(appToLaunch, 'rb'), 'application/octet-stream'))]

    retry = 0
    while retry < 3:
        try:
            response = requests.post(url, files=RokuAppfiles, data=payload, auth=HTTPDigestAuth(readConstants("rokuUser"), readConstants("rokuPass"))) 
            retry = 4
        except (ConnectionError, TimeoutError, RemoteDisconnected) as e:
            print("Error  ===retring in screenshot ===", e)
            print(" Error ===retring ===", retry) 
            time.sleep(2)
            retry += 1
    
    if response.status_code == 200:
        print("roku screen shot taken in conf")
        # soup = BeautifulSoup(response.text, 'html.parser')
        html_content = response.text
        match = re.search(r"screenshoot\.innerHTML\s*=\s*'(.*?)';", html_content, re.DOTALL)
        if match:
            # Extract the innerHTML content with the <img> tag
            inner_html = match.group(1)
            soup = BeautifulSoup(inner_html, 'html.parser')
            img_tag = soup.find('img')
            if img_tag and 'src' in img_tag.attrs:
                img_src = img_tag['src']
                print("Image src:", img_src)

                    # Regular expression to match the 'time' parameter
                match = re.search(r"time=(\d+)", img_src)

                # Extract and print the value if a match is found
            if match:
                time_value = match.group(1)
                print("time_value", time_value)  # Output: 1726406465
                    
                fetch_screenshot_url_base = "http://{}".format(readConstants("roku_ip"))
                fetch_screenshot_url = fetch_screenshot_url_base + "/" + img_src
                print("fetch_screenshot_url===", fetch_screenshot_url)
                response = requests.get(fetch_screenshot_url, auth=HTTPDigestAuth(readConstants("rokuUser"), readConstants("rokuPass")))
                screenshot_folder = "rokuscreenshot"
                roku_screenshot_name = os.path.join(screenshot_folder, "dev_image_" + time_value + ".jpeg")
                "dev_image_" + time_value + ".jpeg"
                    
                print("save rokus creen sjot as ==", roku_screenshot_name)
                print("doIneedScreenshot ", doIneedScreenshot)
                if response.status_code == 200:
                    with open(roku_screenshot_name, "wb") as file:
                        file.write(response.content)
                        pass
                        if doIneedScreenshot:
                            print("attachign roku images in allure ===")
                            allure.attach(response.content, name=ScreenshotFileName, attachment_type=AttachmentType.PNG)
                        print("Image saved successfully!")
            else:
                print("No img tag or src attribute found.")
        else:
            print("No innerHTML found in the response.")
    else:
        print("Failed to fetch the page. Status code:", response.status_code)

def start_appium_service_with_retry(port=4723, retries=3, delay=5):
    appium_service = AppiumService()
    for attempt in range(retries):
        try:
            print(f"Attempt {attempt + 1} to start Appium service on port {port}...")
            appium_service.start(args=[f"--port={port}", "--log-level=debug"])
            if appium_service.is_running:
                print(f"Appium service started successfully on port {port}!")
                return appium_service
        except Exception as e:
            print(f"Error starting Appium service: {e}")
            time.sleep(delay)
    
    # If all retries fail, kill the process on the port and try one last time
    print(f"All {retries} retries failed. Checking and killing the process on port {port}.")
    kill_process_on_port(port)
    time.sleep(delay)  # Wait briefly before retrying
    try:
        appium_service.start(args=[f"--port={port}", "--log-level=debug"])
        if appium_service.is_running:
            print(f"Appium service started successfully on port {port} after killing the PID!")
            return appium_service
    except Exception as e:
        print(f"Failed to start Appium service even after killing the process: {e}")
        raise Exception("Unable to start Appium service.")

def kill_process_on_port(port):
    try:
        # Use lsof to find the PID and kill it
        result = os.popen(f"lsof -ti:{port}").read().strip()
        if result:
            print(f"Killing process with PID: {result} on port {port}.")
            os.system(f"kill -9 {result}")
        else:
            print(f"No process found running on port {port}.")
    except Exception as e:
        print(f"Error killing process on port {port}: {e}")


@pytest.fixture(scope="session", autouse=False)
def setup_platform(env, request):
    is_screen_recording_enabled = request.config.getoption('--enable_screen_recording')  # noqa:E501
    driver = None
    """
        Fixture for setting up the testing environment.
    """
    project_root = os.getcwd()
    constants_path = os.path.join(project_root, 'utils', 'constants.json')
    with open(constants_path) as constant_file:
        costant_value = json.load(constant_file)

    with open(constants_path, "w") as constant_file:
        json.dump(costant_value, constant_file, indent=4)
    currentPlatform = env
    appToLaunch = request.config.getoption("--appFileName")

    print('currentApp', currentPlatform)
    if currentPlatform == 'android':
        print("Inside android")
        os.system('adb shell svc power stayon true')  # wake up fire TV
        appium_service = AppiumService()
        print(f"*******  is appium service already running: {appium_service.is_running}")  # noqa:E501
        appium_service.start(args=['--allow-insecure=adb_shell', '--allow-cors'])  # noqa:E501
        if not appium_service.is_running:
            raise Exception("Appium server did not start!")

        # yield
        # appium_service.stop()
        # config_name = os.getenv('CONFIG_NAME', 'currentApp')
        capabilities = load_capabilities(currentPlatform)
        appPath = os.path.abspath(os.getcwd())

        # capabilities["appium:app"] = os.path.join(appPath, 'builds', appToLaunch)  # noqa:E501
        capabilities["appium:app"] = os.path.join(appPath, 'builds', appToLaunch)  # noqa:E501
        print('capabilities to load', capabilities)
        appPackage = request.config.getoption("--app_package_name")
        appActivity = request.config.getoption("--app_activity")
        capabilities["appPackage"] = appPackage
        capabilities["appActivity"] = appActivity

        options = UiAutomator2Options().load_capabilities(capabilities)
        print("loadingoptions ====", options)

        # capabilities_options = UiAutomator2Options().load_capabilities(capabilities)  # noqa:E501
        try:
            print("am i relunching app?=============================")
            for attempt in range(3):
                try:
                    driver = androidDriver.Remote("http://127.0.0.1:4723", options=options)  # noqa:E501
                    if driver is not None:
                        if is_screen_recording_enabled:
                            driver.start_recording_screen()
                        break
                except Exception as e:
                    print(f"Attempt {attempt + 1} to create driver failed: {e}")  # noqa:E501
                    time.sleep(5)

            print(" firetv driver started=====")
            print(" firetv driver started=  driver type ====", type(driver))
            try:
                # Attempt to terminate using Appium
                driver.terminate_app(readConstants("current_app_package"))
            except Exception as e:
                print(f"Appium terminate_app failed: {e}. Trying force stop.")
                # Fallback to ADB force stop
                os.system(f"adb shell am force-stop {readConstants('current_app_package')}")  # noqa:E501
            # driver.terminate_app(readConstants("current_app_package"))
            time.sleep(3)
            print("is app open after termination: ", driver.query_app_state(readConstants("current_app_package")))  # noqa:E501

            # driver.close()  // trying to debug InvalidSessionIdException
            # Launch (activate) the app again
            driver.activate_app(readConstants("current_app_package"))
            print("is app open after activation: ", driver.query_app_state(readConstants("current_app_package")))  # noqa:E501
            driver.implicitly_wait(10)
        except Exception as e:
            appium_service.stop()
            print("firetv appluanch error ===", e)
    if driver:
        print('yeidling driver instance condition')
        yield driver
        print('after yielding driver')
        if isinstance(driver, androidDriver.Remote):
            print('Inside tear down')
            if is_screen_recording_enabled:
                video_data = driver.stop_recording_screen()
                if video_data:
                    print("Video recorded")
                # Attach video data to Allure
                allure.attach(
                    base64.b64decode(video_data),  # Decode the base64 video data   # noqa:E501
                    name="Screen Recording",
                    attachment_type=allure.attachment_type.MP4,
                    extension=".mp4",
                )
            driver.quit()
            appium_service.stop()
        if currentPlatform == 'android':
            os.system("adb shell am force-stop io.appium.uiautomator2.server")
            os.system("adb shell am force-stop io.appium.uiautomator2.server.test")  # noqa:E501

    else:
        print('yielding nothing')
        yield None


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()
    print("came for failed test case",report)
    if report.when == "call":
        driver = None
        app_driver = item.funcargs.get('setup_platform', None)
        # print("app_driver instance in tear down ====" , type(app_driver))

        if app_driver:
            driver = app_driver

        if driver:  
            print("coming to take screenshot for failure")
            if isinstance(driver, webdriver):
                screenshot = driver.get_screenshot_as_png()
                print("secnario is failed so trying to kill app and relaunch ", readConstants("current_app_package"))
                # driver.terminate_app(readConstants("current_app_package"))
                try:
                    # Attempt to terminate using Appium
                    driver_status = driver.terminate_app(readConstants("current_app_package"))
                    print(f"status of the driver is: ======================= {driver_status}")
                except Exception as e:
                    print(f"Appium terminate_app failed: {e}. Trying force stop.")
                    # Fallback to ADB force stop
                    os.system(f"adb shell am force-stop {readConstants('current_app_package')}")  # noqa:E501
                time.sleep(2)
                print("app killed====lets relaunch")
                driver.activate_app(readConstants("current_app_package"))
                print("app killed====lets relaunch")
                allure.attach(screenshot, name="screenshot", attachment_type=AttachmentType.JPG)
                time.sleep(5)
            if isinstance(driver, str):
                print("its roku report")
                screenshotAttachment("onfailure.jpeg")

        # Make sure the setup_platform fixture is called
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if driver:  
                    if isinstance(driver, webdriver):
                        print("secnario is failed so trying to kill app and relaunch ", readConstants("current_app_package"))
                        driver.terminate_app(readConstants("current_app_package"))
                        time.sleep(2)
                        print("app killed====lets relaunch")
                        driver.activate_app(readConstants("current_app_package"))
                        print("app killed====lets relaunch")
                        allure.attach(screenshot, name="screenshot", attachment_type=AttachmentType.PNG)
                        time.sleep(5)
                    if isinstance(driver, str):
                        screenshotAttachment("onfailure.jpeg")
                        # screenshotAttachment("onfailure.jpeg")
                        # print("secnario is failed so trying to kill app and relaunch " ,readConstants("current_app_package"))
                        # driver.terminate_app(readConstants("current_app_package"))
                        time.sleep(2)
                        # print("app killed====lets relaunch")
                        # driver.activate_app(readConstants("current_app_package"))
                        print("app killed====lets relaunch")
                        # time.sleep(5)
            # Launch (activate) the app again
                  
        # Attach screenshot to allure report
                
        except Exception as e:
            print('Fail to take screen-shot:', e)


@pytest.fixture(scope="session", autouse=True)
def load_GD_prereq():
    def _load_GD_prereq(fileName, keyName):
        print("receving ", fileName)
        return readPreReqJson(fileName, keyName)
    return _load_GD_prereq


def getJSONFile(fileName):
    print("fetch json as file in given name  ", fileName)
    project_root = os.getcwd()
    jsonFile_path = os.path.join(project_root, 'utils', fileName + ".json")
    with open(jsonFile_path, 'r') as file:
        json_data = json.load(file)
    # json_file = json.dumps(jsonPath_path)
    # print("json_file in given name  ", json_data)
    return json_data


consecutive_failure_abort = False
consecutive_failure_count = 5
consecutive_failures = 0


def pytest_configure(config):
    global consecutive_failure_abort, consecutive_failure_count
    
    consecutive_failure_abort = config.getoption("--consecutive_failure_abort")
    print("Consecutive failure value", consecutive_failure_abort, type(consecutive_failure_abort))
    if config.getoption("--consecutive_failure_count"):
        consecutive_failure_count = int(config.getoption("--consecutive_failure_count"))

    app_file = config.getoption("--appFileName")
    app_package_name = config.getoption("--app_package_name")
    app_activity_name = config.getoption("--app_activity")
    current_platform = config.getoption("--platform")
    if not app_file:
        raise pytest.UsageError("--appFileName is required")
    
    if not app_package_name:
        raise pytest.UsageError("--app_package_name is required")

    if not app_activity_name:
        raise pytest.UsageError("--app_activity is required")

   
    isScreenshoreRequired = config.getoption("--screenShotToggle")
    
    project_root = os.getcwd()
    constants_path = os.path.join(project_root, 'utils', 'constants.json')
    with open(constants_path) as constant_file:
        costant_value = json.load(constant_file)

    costant_value["current_app_package"] = app_package_name
    print("reading from cons for screenshot ===", costant_value["NEED_SCREENSHOTS_FOR_PASS"])
    print("reading run tim e setup screenshot ===", isScreenshoreRequired)
    costant_value["NEED_SCREENSHOTS_FOR_PASS"] = isScreenshoreRequired
    print("reading from cons for screenshot after update ===", costant_value["NEED_SCREENSHOTS_FOR_PASS"])

    print("final value for screenshot ===", costant_value["NEED_SCREENSHOTS_FOR_PASS"])
   
    with open(constants_path, "w") as constant_file:
        json.dump(costant_value, constant_file, indent=4)
    


def pytest_runtest_logreport(report):
    global consecutive_failures, consecutive_failure_abort, consecutive_failure_count

    if consecutive_failure_abort:

        if report.when == 'call' and report.failed:
            consecutive_failures += 1

        elif report.when == 'call' and report.passed:
            consecutive_failures = 0
                

        if consecutive_failures >= consecutive_failure_count:
            # print("Aborting test suite due to consecutive failures!")
            pytest.exit(f" \n Aborting test suite due to {consecutive_failure_count} consecutive failures")


def updateConstantFile(contantKey, ConstantValue):
    project_root = os.getcwd()
    constants_path = os.path.join(project_root, 'utils', 'constants.json')
    with open(constants_path) as constant_file:
        costant_value = json.load(constant_file)
    costant_value[contantKey] = ConstantValue
    with open(constants_path, "w") as constant_file:
        json.dump(costant_value, constant_file, indent=4) 
    
