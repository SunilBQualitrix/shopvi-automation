# Mobile Automation Framework (Python + Appium + BDD)

This repository contains a **mobile automation framework** built using **Python, Appium, and BDD**. The framework is designed for testing Android applications and integrates **Allure reporting, pytest-html, and Jenkins** for automation execution and reporting.

## 📌 Features
- **Appium-based UI automation** for Android apps.
- **BDD (Behavior-Driven Development)** using **pytest**.
- **Page Object Model (POM)** for maintainability.
- **Allure reporting** for detailed test reports.
- **Pytest & Pytest-HTML integration**.
- **Custom logger** for better debugging.

---

## 🛠 Setup Instructions

### **1️⃣ Prerequisites**
Ensure the following dependencies are installed:
- **Python** (>=3.8)
- **Appium Server** (installed and running)
- **Android SDK & ADB** (configured in PATH)
- **JDK 11 or later**
- **Google ChromeDriver** (for WebView testing, if applicable)
- **Git** (for version control)

### **2️⃣ Clone the Repository**
```sh
 git clone <your-github-repo-url>
 cd <your-repo-folder>
```

### **3️⃣ Create a Virtual Environment**
```sh
 python -m venv myenv
 source myenv/bin/activate   # For Mac/Linux
 myenv\Scripts\activate      # For Windows
```

### **4️⃣ Install Dependencies**
```sh
 pip install -r requirements.txt
```

---

## 🚀 Running Tests

### **1️⃣ Start Appium Server**
Ensure Appium server is running before executing tests:
```sh
 appium &   # Run in background (Mac/Linux)
 appium     # Run in foreground (Windows)
```

### **2️⃣ Run Pytest Tests**
```sh
 pytest -v -m ViShopRegression --platform=android --app_package_name=com.mventus.selfcare.activity --app_activity=com.mventus.selfcare.activity.MainActivity --appFileName=D:\PyProjects\PythonProject\ShopVI_Automation\builds\vishop.apk --full-trace
```

### **3️⃣ Generate Single file Allure Reports**
```sh
 allure generate --single-file shopvi-automation\allure-results --clean -o shopvi-automation\allure-report
```

---

## 📂 Project Structure
```
.
├── builds/                # APK builds
├── pages/                 # Actions and Page Object Model (POM) implementation
├── reports/               # Screenshots, HTML reports
├── tests/                 # Step definitions and feature files
├── utils/                 # Utilities (Customloger, prereq, platformconfig, constants etc.)
├── conftest.py            # Pytest fixtures & setup
├── requirements.txt       # Dependencies
├── README.md              # Project Documentation
```

---


## 🛠 Troubleshooting
### **Common Issues & Fixes**
- **Appium server not starting?** Ensure Appium is installed and running (`appium -v` to check version).
- **ADB device not found?** Check if the device is connected via USB and recognized (`adb devices`).
- **StaleElementException?** Implement retries using explicit waits in `basepage.py`.
- **Tests failing randomly?** Try increasing wait times or checking element locators.

---

### **🔗 Useful Links**
- [Appium Documentation](https://appium.io/docs/en/about-appium/)
- [Pytest](https://docs.pytest.org/en/stable/)
- [Selenium WebDriver](https://www.selenium.dev/documentation/)
- [Allure Reports](https://docs.qameta.io/allure/)

---

🎯 **Happy Testing! 🚀**
