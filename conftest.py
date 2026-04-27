# Full rewritten conftest.py with centralized artifacts folder structure

import pytest
import os
import time
import json
import shutil
import subprocess
import urllib.request
import allure

from appium import webdriver as androidDriver
from appium.options.android import UiAutomator2Options
from allure_commons.types import AttachmentType
from utils.common_utils import readConstants    # noqa:F401


# =====================================================
# PROJECT + PATHS
# =====================================================
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

ARTIFACTS_DIR = os.path.join(PROJECT_ROOT, "artifacts")
ALLURE_RESULTS_DIR = os.path.join(ARTIFACTS_DIR, "allure-results")
ALLURE_REPORT_DIR = os.path.join(ARTIFACTS_DIR, "allure-reports")
REPORTS_DIR = os.path.join(ARTIFACTS_DIR, "reports")
SCREENSHOT_DIR = os.path.join(REPORTS_DIR, "screenshots")
LOGS_DIR = os.path.join(ARTIFACTS_DIR, "logs")
LOG_FILE = os.path.join(LOGS_DIR, "testreport.log")
SCREEN_RECORDING_DIR = os.path.join(ARTIFACTS_DIR, "screen-recordings")


# =====================================================
# APPIUM CONFIG
# =====================================================
APPIUM_HOST = "127.0.0.1"
APPIUM_PORT = 4723
APPIUM_URL = f"http://{APPIUM_HOST}:{APPIUM_PORT}"

# Use exact path from your machine
ALLURE_PATH = r"C:\Users\Administrator\AppData\Roaming\npm\allure.cmd"


# =====================================================
# CLI OPTIONS
# =====================================================
def pytest_addoption(parser):
    parser.addoption("--platform", action="store", default="android")
    parser.addoption("--appFileName", action="store", default="")
    parser.addoption("--app_package_name", action="store")
    parser.addoption("--app_activity", action="store")
    parser.addoption(
        "--enable_screen_recording",
        action="store_true",
        default=False,
    )


# =====================================================
# HELPERS
# =====================================================
def ensure_directories():
    paths = [
        ARTIFACTS_DIR,
        ALLURE_RESULTS_DIR,
        ALLURE_REPORT_DIR,
        REPORTS_DIR,
        SCREENSHOT_DIR,
        LOGS_DIR,
        SCREEN_RECORDING_DIR,
    ]

    for path in paths:
        os.makedirs(path, exist_ok=True)


def load_capabilities(config_name):
    config_path = os.path.join(PROJECT_ROOT, "utils", "platformconfig.json")
    with open(config_path, "r") as f:
        config = json.load(f)
    return config.get(config_name, {})


def is_appium_running(host=APPIUM_HOST, port=APPIUM_PORT, timeout=2):
    try:
        with urllib.request.urlopen(
            f"http://{host}:{port}/status",
            timeout=timeout,
        ) as response:
            return response.status == 200
    except Exception:
        return False


def get_connected_android_devices():
    try:
        output = subprocess.check_output(
            ["adb", "devices"],
            stderr=subprocess.STDOUT,
            text=True,
        )
        lines = [line.strip() for line in output.splitlines() if line.strip()]
        devices = [
            line.split()[0]
            for line in lines[1:]
            if len(line.split()) >= 2 and line.split()[1] == "device"
        ]
        return devices
    except Exception:
        return []


def clean_uiautomator():
    os.system("adb uninstall io.appium.uiautomator2.server")
    os.system("adb uninstall io.appium.uiautomator2.server.test")


def start_appium():
    if is_appium_running():
        print(f"Appium already running at {APPIUM_HOST}:{APPIUM_PORT}")
        return None

    appium_executable = shutil.which("appium") or "appium"

    try:
        process = subprocess.Popen(
            [appium_executable, "--port", str(APPIUM_PORT)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            shell=False,
        )
    except FileNotFoundError:
        raise Exception(
            "Appium executable not found. Install Appium globally or add to PATH."  # noqa:E501
        )

    for _ in range(20):
        if is_appium_running():
            print("Appium server started successfully")
            return process
        time.sleep(1)

    process.terminate()
    raise Exception("Unable to start Appium server")


# =====================================================
# CLEAN REPORTS BEFORE EXECUTION
# =====================================================
@pytest.fixture(scope="session", autouse=True)
def clean_reports():
    if os.path.exists(ARTIFACTS_DIR):
        shutil.rmtree(ARTIFACTS_DIR)

    ensure_directories()


# =====================================================
# MAIN DRIVER FIXTURE
# =====================================================
@pytest.fixture(scope="session")
def setup_platform(request):
    platform = request.config.getoption("--platform")
    app_file = request.config.getoption("--appFileName")
    app_package = request.config.getoption("--app_package_name")
    app_activity = request.config.getoption("--app_activity")

    driver = None
    service = None

    if platform.lower() == "android":
        print("Starting Android execution")

        devices = get_connected_android_devices()
        if not devices:
            raise Exception("No Android device connected")

        print(f"Connected devices: {', '.join(devices)}")

        clean_uiautomator()
        service = start_appium()

        capabilities = load_capabilities("android")
        capabilities.update(
            {
                "platformName": "Android",
                "appium:automationName": "UiAutomator2",
                "appium:noReset": True,
                "appium:fullReset": False,
                "appium:newCommandTimeout": 300,
                "appium:autoGrantPermissions": True,
                "appium:disableWindowAnimation": True,
                "appium:appPackage": app_package,
                "appium:appActivity": app_activity,
            }
        )

        if app_file:
            capabilities["appium:app"] = app_file

        options = UiAutomator2Options().load_capabilities(capabilities)

        driver = androidDriver.Remote(APPIUM_URL, options=options)
        driver.implicitly_wait(10)
        time.sleep(5)

    yield driver

    if driver:
        try:
            driver.quit()
        except Exception:
            pass

    if service:
        try:
            service.terminate()
            service.wait(timeout=10)
        except Exception:
            pass


# =====================================================
# FAILURE SCREENSHOT
# =====================================================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("setup_platform")

        if driver:
            try:
                screenshot = driver.get_screenshot_as_png()

                allure.attach(
                    screenshot,
                    name="Failure Screenshot",
                    attachment_type=AttachmentType.PNG,
                )
            except Exception:
                print("Screenshot capture failed")


# =====================================================
# ALLURE REPORT GENERATION
# =====================================================
@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    if os.path.exists(ALLURE_RESULTS_DIR):
        try:
            print("Generating Allure report...")

            subprocess.run(
                [
                    ALLURE_PATH,
                    "generate",
                    "--single-file",
                    ALLURE_RESULTS_DIR,
                    "--clean",
                    "-o",
                    ALLURE_REPORT_DIR,
                ],
                check=True,
                cwd=PROJECT_ROOT,
                shell=True,
            )

            print(f"Allure report generated at: {ALLURE_REPORT_DIR}")

        except Exception as e:
            print(f"Failed to generate Allure report: {e}")
    else:
        print("No Allure results found, skipping report generation")
