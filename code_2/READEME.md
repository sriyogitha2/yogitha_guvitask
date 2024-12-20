# **OrangeHRM Automation Testing**

This repository contains automated test scripts for **OrangeHRM** (a popular Human Resource Management software) using **Selenium WebDriver** and **Pytest**. The tests cover functionality such as login, user creation, menu visibility, and data validation. The tests also include data-driven testing and generate HTML reports upon execution.

## **Features**

- Automated tests using **Pytest** and **Selenium WebDriver**.
- Data-driven testing for login using credentials stored in Excel.
- HTML report generation with `pytest-html`.
- Verification of user creation, login, and visibility of menus.
- Checkout verification including screenshots.
- Support for WebDriver management via `webdriver_manager`.

## **Prerequisites**

Before running the tests, ensure the following are installed:

- Python 3.6+
- ChromeDriver (automatically managed by `webdriver_manager`)
- Google Chrome browser (for Selenium to interact with)
- Pip for managing Python packages

## **Installation**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/orangehrm-automation.git
   cd orangehrm-automation
Set up a Virtual Environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the Required Dependencies:

bash
Copy code
pip install -r requirements.txt
requirements.txt contains all necessary packages, including:

pytest for running the tests.
selenium for browser automation.
webdriver_manager for automatically managing ChromeDriver.
pytest-html for generating HTML reports.
openpyxl for Excel-based data-driven testing.
Install webdriver_manager: This will manage the ChromeDriver version automatically.

bash
Copy code
pip install webdriver_manager
Running Tests
Run Tests with HTML Report:

To run all tests and generate an HTML report, use the following command:

bash
Copy code
pytest TestScripts/ --html=report.html --maxfail=5 --disable-warnings
This command will:

Run all tests in the TestScripts/ directory.
Generate an HTML report and save it as report.html.
Stop running tests after 5 failures (--maxfail=5).
Disable warnings in the report (--disable-warnings).
View the Report:

After the tests complete, open the report.html file in your browser to view the test results.

Test Directory Structure
graphql
Copy code
orangehrm-automation/
│
├── TestData/
│   ├── data.py                   # Test data (login credentials, Excel file location)
│
├── TestLocators/
│   ├── locators.py               # Page element locators
│
├── TestScripts/
│   ├── test_cre.py               # Test for creating a new user in OrangeHRM
│   ├── test_login.py             # Test for verifying login functionality
│   ├── test_menu.py              # Test for verifying menu items visibility
│   ├── test_verify_user_in_records.py  # Test for verifying user in records
│
├── Utilities/
│   ├── excel_functions.py        # Helper functions for reading and writing Excel data
│
├── requirements.txt              # List of dependencies for the project
├── README.md                     # Project documentation
└── report.html                   # HTML test report (generated after running tests)
Test Breakdown
1. Login Tests:
Verifies login functionality using data from TestData/data.py.
Checks for successful login and proper session management.
2. User Creation:
Tests the process of creating a new user through the admin dashboard.
Verifies that the user appears in records after being created.
3. Menu Functionality:
Checks whether the menus are correctly visible upon logging in.
4. Excel Data-Driven Testing:
Loads user credentials from an Excel file for multiple login attempts.
5. Validation Tests:
Verifies data integrity by checking if the correct user is visible in the system after creation.
Ensures that the number of users created and listed matches the input data.
Customization
1. Changing Login Credentials:
You can add more user credentials to the TestData/data.py file. Just add new tuples to the data list, formatted as ("username", "password").

2. WebDriver Options:
If you need to customize the browser options (e.g., run headless), modify the initialize_driver method in Utilities/excel_functions.py.

3. Test Reports:
The test reports are generated in HTML format using pytest-html. You can customize the report settings in the pytest configuration file if needed.
