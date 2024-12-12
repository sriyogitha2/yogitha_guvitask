# GUVI Website Automation Tests

This project contains automated tests for verifying the functionality of the [GUVI website](https://www.guvi.in). It uses Selenium WebDriver for browser automation and Pytest for organizing and running test cases. The focus of the tests is on login, sign-up, and general UI functionalities.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Test Cases](#test-cases)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project automates the following functionalities on the GUVI website:
- Validating the accessibility of the website.
- Checking the visibility and clickability of buttons like "Login" and "Sign-Up".
- Testing login functionality with valid and invalid credentials.

It ensures the site’s key features work as intended and helps in identifying potential issues in the user flow.

## Features

- **Selenium WebDriver**: Used for browser interactions.
- **Pytest**: Framework for organizing and running tests.
- **Requests**: For validating URL accessibility.
- Modular helper class for reusing WebDriver-related functions.

## Prerequisites

Before running the tests, ensure the following are installed:

- **Python**: Version 3.7 or higher.
- **Google Chrome Browser**: Latest version.
- **ChromeDriver**: Managed automatically via `webdriver_manager`.
- **pip**: For installing Python dependencies.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/guvi-automation-tests.git
    cd guvi-automation-tests
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Verify the installation by checking Pytest:
    ```bash
    pytest --version
    ```

## Usage

### Run All Test Cases

To execute all test cases:
```bash
pytest
```

### Run a Specific Test Case

Use the `-k` option to run a specific test case. For example:
```bash
pytest -k test_valid_url
```

### Generate an HTML Report

To generate a detailed test report:
```bash
pytest --html=report.html
```

## Code Structure

```plaintext
.
├── README.md               # Documentation file
├── requirements.txt        # Python dependencies
├── test_guvi_automation.py # Test script for GUVI website
└── utils/                  # Helper scripts
    ├── web_driver_helper.py # WebDriver helper functions
    ├── __init__.py         # Init file for utils
```

### Key Components

- **`test_guvi_automation.py`**: Contains all test cases.
- **`web_driver_helper.py`**: Helper class to perform common WebDriver actions, like navigating to URLs, clicking elements, and waiting for elements.

## Test Cases

### 1. URL Validation
- **Description**: Verifies that the GUVI homepage is accessible.
- **Command**: `pytest -k test_valid_url`

### 2. Homepage Title Validation
- **Description**: Checks if the homepage title matches the expected value.
- **Command**: `pytest -k test_homepage_title`

### 3. Button Visibility and Clickability
- **Description**: Ensures that the login and sign-up buttons are visible and clickable.
- **Command**:
  - Login button visibility: `pytest -k test_login_button_visibility`
  - Sign-up button visibility: `pytest -k test_signup_visibility`

### 4. Login Functionality
- **Description**: Tests login with valid and invalid credentials.
- **Command**:
  - Valid credentials: `pytest -k test_login`
  - Invalid credentials: `pytest -k test_invalid_login`

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-branch
    ```
3. Commit your changes:
    ```bash
    git commit -m "Add meaningful description of changes"
    ```
4. Push to your fork:
    ```bash
    git push origin feature-branch
    ```
5. Submit a pull request.

