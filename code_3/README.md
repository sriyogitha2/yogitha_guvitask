
# Sauce Demo Automation Tests

This repository contains automated test scripts for the Sauce Demo website using Selenium WebDriver and Pytest. The tests focus on user login, cart functionality, and the checkout process. The tests are designed with data-driven testing, and HTML reports are generated after running the tests.

## Features
- Automated tests using Pytest and Selenium WebDriver.
- Data-driven testing for multiple user credentials.
- HTML report generation using `pytest-html`.
- Random product selection and cart functionality validation.
- Checkout process verification, including screenshots of the checkout page.

## Prerequisites

Before running the tests, ensure the following are installed:

- Python 3.6+
- ChromeDriver (managed by `webdriver_manager`)
- Google Chrome browser (for Selenium to interact with)
- Pip for managing Python packages

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/sauce-demo-automation.git
   cd sauce-demo-automation
   ```

2. **Set up a Virtual Environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the Required Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   `requirements.txt` contains all necessary packages, including:
   - `pytest` for running the tests.
   - `selenium` for interacting with the web browser.
   - `webdriver_manager` for automatically managing ChromeDriver.
   - `pytest-html` for generating HTML reports.

4. **Install `webdriver_manager`:**
   This will manage the `ChromeDriver` version automatically.
   ```bash
   pip install webdriver_manager
   ```

## Running Tests

1. **Run Tests with HTML Report:**

   To run all tests and generate an HTML report, use the following command:
   ```bash
   pytest tests/ --html=report.html --maxfail=5 --disable-warnings
   ```

   This command will:
   - Run all tests in the `tests/` directory.
   - Generate an HTML report and save it as `report.html`.
   - Stop running tests after 5 failures (`--maxfail=5`).
   - Disable warnings in the report (`--disable-warnings`).

2. **View the Report:**

   After the tests complete, open the `report.html` file in your browser to view the test results.

## Test Directory Structure

```
sauce-demo-automation/
│
├── pages/
│   ├── login_page.py               # Page Object Model for login page
│
├── tests/
│   ├── test_login_using_cookies.py  # Test for login using cookies
│   ├── test_login_with_guvi_user.py # Test for login with Guvi user credentials
│   ├── test_cart_button_visibility.py # Test for cart button visibility
│   ├── test_add_random_products_to_cart.py # Test for adding random products to cart
│   ├── test_verify_cart_products.py # Test for verifying products in the cart
│   ├── test_checkout_process_verification.py # Test for verifying checkout process
│
├── utils/
│   ├── driver_setup.py             # WebDriver setup for initializing the Chrome driver
│
├── data/
│   ├── login_data.py               # User credentials for data-driven tests
│
├── screenshots/                    # Directory where screenshots (e.g., of the checkout page) are saved
│
├── requirements.txt                # List of dependencies for the project
├── README.md                       # Project documentation
└── report.html                     # HTML test report (generated after running tests)
```

## Test Breakdown

### 1. **Login Tests:**
   - Test login with multiple user credentials from the `login_data.py`.
   - Check if login is successful and save session cookies.

### 2. **Cart Functionality Tests:**
   - Test visibility of the cart button after logging in.
   - Randomly select 4 products from the inventory and add them to the cart.
   - Verify the correct number of items in the cart.

### 3. **Checkout Process:**
   - Add products to the cart and proceed with the checkout process.
   - Verify that the product details are consistent on the checkout page.
   - Take a screenshot of the checkout page and verify the completion message after finishing the checkout.

### 4. **Cookies Handling:**
   - Test logging in using cookies and checking whether the session persists.

## Customization

### 1. **Changing Login Credentials:**
   You can add more user credentials to the `data/login_data.py` file. Just add new tuples to the `login_data` list, formatted as `("username", "password")`.

### 2. **WebDriver Options:**
   If you need to customize the browser options (e.g., run headless), modify the `initialize_driver` method in `utils/driver_setup.py`.


