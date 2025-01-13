# Automated Testing for Guvi Website

## Overview
This project is designed to automate testing for the Guvi website using Selenium WebDriver and Python's `pytest` framework. The automation covers functionalities like verifying the homepage, testing login and signup features, and validating error messages for invalid login attempts.

---

## Project Structure

```
project-directory
|
├── pages
│   ├── homepage.py        # Page Object Model for the homepage
│   ├── loginpage.py       # Page Object Model for the login page
│
├── tests
│   ├── test_guvi.py       # Test cases for Guvi website
│
├── utils
│   ├── webdriver_helper.py # Utility class for WebDriver operations
│
└── README.md             # Project documentation
```

---

## Prerequisites

1. **Python**: Version 3.7 or higher
2. **Google Chrome**: Latest version
3. **ChromeDriver**: Compatible with your Google Chrome version
4. **Dependencies**: Install required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

---

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/guvi-automation-tests.git
   ```

2. Navigate to the project directory:
   ```bash
   cd guvi-automation-tests
   ```

3. Install dependencies:
   ```bash
   pip install selenium pytest
   ```

4. Ensure `chromedriver` is added to your system PATH or place it in the project directory.

---

## How to Run Tests

1. **Execute all tests**:
   ```bash
   pytest tests/test_guvi.py
   ```

2. **Generate an HTML report**:
   ```bash
   pytest tests/test_guvi.py --html=report.html
   ```

3. **View the report**:
   Open `report.html` in your browser to view the test results.

---

## Files Explained

### 1. **`pages/homepage.py`**
   Implements the Page Object Model (POM) for the Guvi homepage:
   - Locators for login and signup buttons
   - Method to interact with the login button

### 2. **`pages/loginpage.py`**
   Implements the POM for the Guvi login page:
   - Locators for email, password fields, and submit button
   - Method to perform login
   - Method to retrieve error messages for invalid logins

### 3. **`tests/test_guvi.py`**
   Contains the test cases for the Guvi website:
   - Tests homepage URL and title
   - Tests visibility of login and signup buttons
   - Validates login functionality with both valid and invalid credentials

### 4. **`utils/webdriver_helper.py`**
   A utility class for interacting with WebDriver:
   - Methods to navigate, click elements, and wait for elements
   - Includes a method to quit the WebDriver session

---

## Sample Test Workflow

### Valid Login Test
1. Navigate to the Guvi homepage.
2. Click the login button.
3. Enter valid credentials and submit.
4. Verify that the login is successful by checking the page title.

### Invalid Login Test
1. Navigate to the Guvi homepage.
2. Click the login button.
3. Enter invalid credentials and submit.
4. Verify that the appropriate error message is displayed.

