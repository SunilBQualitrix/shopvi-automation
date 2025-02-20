import logging
import allure
import os

# Define log file path
LOG_DIR = "D:\\VIL\\shopvi-automation"
LOG_FILE = os.path.join(LOG_DIR, "testreport.log")
# Ensure the log file is cleared before the script starts
if os.path.exists(LOG_FILE):
    logging.shutdown()  # Release any file handles
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.truncate(0)  # Clear the contents of the log file


def custom_logger(logLevel=logging.DEBUG):
    """Create a custom logger with a file handler and avoid duplicate handlers."""  # noqa:E501
    os.makedirs(LOG_DIR, exist_ok=True)

    logger = logging.getLogger("ShopVI")
    logger.setLevel(logLevel)

    # Avoid adding multiple handlers
    if not logger.handlers:
        file_handler = logging.FileHandler(LOG_FILE, mode='w')
        file_handler.setLevel(logLevel)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")      # noqa:E501
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
            logging.shutdown()  # Ensure file is not in use
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                logs = f.read()

            allure.attach(logs, name="Test Report Logs", attachment_type=allure.attachment_type.TEXT)    # noqa:E501

    except PermissionError as e:
        print(f"PermissionError: {e}. Retrying after 2 seconds...")
        import time
        time.sleep(2)
        try:
            logging.shutdown()
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                logs = f.read()
            allure.attach(logs, name="Test Report Logs", attachment_type=allure.attachment_type.TEXT)         # noqa:E501
        except Exception as e:
            print(f"Failed again: {e}")
