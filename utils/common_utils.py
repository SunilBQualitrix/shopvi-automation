import os
import json


# Project root path
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)


def readConstants(constant_key):
    """
    Read value from utils/constants.json

    Example:
        value = readConstants("appPackage")
    """

    constants_path = os.path.join(
        PROJECT_ROOT,
        "utils",
        "constants.json"
    )

    if not os.path.exists(constants_path):
        print(f"constants.json not found at: {constants_path}")
        return None

    try:
        with open(constants_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data.get(constant_key)

    except Exception as e:
        print(f"Error reading constants.json: {e}")
        return None
