
# Import necessary modules for testing
import pytest
import sys
import os
from pages.login_page import LoginPage  # Import LoginPage class for login functionality
from utils.driver_setup import DriverSetup  # Import DriverSetup to initialize the driver
import time

# Modify system path to include the parent directory for module imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Pytest fixture to set up the WebDriver instance for the entire module
@pytest.fixture(scope="module")
def driver():
    # Initialize the WebDriver
    driver = DriverSetup().initialize_driver()
    # Yield the driver for use in the tests, and quit the driver after test completion
    yield driver
    driver.quit()

# Test for logging in using cookies
def test_login_using_cookies(driver):
    # Print a message indicating the start of the test
    print("\nStarting test: test_login_using_cookies")
    
    # Initialize the LoginPage object to perform login actions
    login_page = LoginPage(driver)
    # Step 1: Login with standard user credentials
    login_page.login("standard_user", "secret_sauce")
    
    # Wait for the page to load
    time.sleep(2)
    
    # Step 2: Check if login was successful and fetch cookies
    login_page.check_login_success()
    cookies = login_page.get_cookies()
    print("Cookies after login:", cookies)
    
    # Optionally, save the cookies to a file for future use
    with open("cookies.json", "w") as cookie_file:
        import json
        json.dump(cookies, cookie_file)
    
    # Print a message indicating the test has passed successfully
    print("Test test_login_using_cookies passed successfully.")

