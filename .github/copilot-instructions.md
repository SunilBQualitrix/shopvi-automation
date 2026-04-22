# VI Shop Automation Framework Guidelines

This document outlines key patterns and workflows for the VI Shop mobile automation framework, built with Python, Appium, and BDD.

## Core Architecture

- **BDD Framework**: Uses pytest-bdd with feature files in `tests/features/` and step definitions in `tests/step_defs/`
- **Page Object Model**:
  - Base actions in `pages/actions/actions_parent.py`
  - Platform-specific actions in `pages/actions/android_actions.py`
  - Each page object inherits from `BasePage` (`pages/base_page.py`)

## Key Patterns

### 1. Page Objects
```python
from pages.base_page import BasePage

class SomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # Define page-specific locators here
```

### 2. Test Structure
- Feature files use the format: `@TagName` followed by `Scenario Outline` with examples
- Step definitions use pytest fixtures for page object initialization:
```python
@pytest.fixture
def page_instance(setup_platform):
    return PageClass(setup_platform)
```

### 3. Android Interactions
- Use `self.actions` for Android-specific operations in page objects
- Access keycodes via `self.keys` dictionary in BasePage (e.g., `self.keys["KEYCODE_BACK"]`)

## Critical Workflows

### Test Execution
1. Start Appium server first
2. Run tests with platform and app details:
```sh
pytest -v -m ViShopRegression --platform=android --app_package_name=com.mventus.selfcare.activity --app_activity=com.mventus.selfcare.activity.MainActivity --appFileName=path/to/vishop.apk --full-trace
```

### Test Development
1. Add new feature in `tests/features/Shop_Vi_Validations.feature`
2. Implement step definitions in `tests/step_defs/shop_vi_validations_test.py`
3. Create page object if needed in `pages/`
4. Add platform-specific actions in `pages/actions/android_actions.py`

## Configuration
- App capabilities in `utils/platformconfig.json`
- Test data in `utils/prereq.json`
- Constants in `utils/constants.json`

## Reporting
- Generate Allure reports after test execution:
```sh
allure generate --single-file shopvi-automation/allure-results --clean -o shopvi-automation/allure-report
```

## Common Gotchas
- Always initialize page objects through pytest fixtures
- Use explicit waits in Android actions for reliability
- Handle both WebView and native contexts appropriately