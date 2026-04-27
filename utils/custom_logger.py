import logging
import allure
import os
import time

# Define framework root directory relative to this file
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.pardir)
)
ARTIFACTS_DIR = os.path.join(PROJECT_ROOT, "artifacts")
LOG_DIR = os.path.join(ARTIFACTS_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "testreport.log")
SCREENSHOT_DIR = os.path.join(ARTIFACTS_DIR, "reports", "screenshots")

# Ensure the log directory exists
os.makedirs(LOG_DIR, exist_ok=True)

# Attempt to reset the log file if it is not currently locked
if os.path.exists(LOG_FILE):
    try:
        logging.shutdown()  # Release any file handles
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.truncate(0)
    except PermissionError:
        # Log file is locked by another process; preserve the existing file.
        pass


def custom_logger(logLevel=logging.DEBUG):
    """Create a custom logger with a file handler and avoid duplicate handlers."""  # noqa:E501
    os.makedirs(LOG_DIR, exist_ok=True)

    logger = logging.getLogger("ShopVI")
    logger.setLevel(logLevel)

    # Avoid adding multiple handlers
    if not logger.handlers:
        try:
            file_handler = logging.FileHandler(
                LOG_FILE,
                mode='a',
                encoding='utf-8',
                delay=True,
            )
        except PermissionError:
            fallback_file = os.path.join(
                LOG_DIR,
                f"testreport_{int(time.time())}.log",
            )
            file_handler = logging.FileHandler(
                fallback_file,
                mode='a',
                encoding='utf-8',
                delay=True,
            )

        file_handler.setLevel(logLevel)
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


def allureLogs(message):
    """Log messages as Allure steps."""
    with allure.step(message):
        pass


def attach_logs_to_allure():
    """Attach testreport.log to Allure reports after each test."""
    try:
        if os.path.exists(LOG_FILE):
            try:
                with open(LOG_FILE, "r", encoding="utf-8") as f:
                    logs = f.read()
            except PermissionError:
                logs = (
                    "Unable to attach logs because the log file is locked "
                    "by another process."
                )

            allure.attach(
                logs,
                name="Test Report Logs",
                attachment_type=allure.attachment_type.TEXT,
            )
    except Exception as e:
        print(f"Failed to attach logs to Allure: {e}")
