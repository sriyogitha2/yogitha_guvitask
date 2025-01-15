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
# Test for checking the visibility of the logout button
def test_logout_button_visibility(driver):
    # Print a message indicating the start of the test
    print("\nStarting test: test_logout_button_visibility")
    
    # Initialize the LoginPage object to perform login actions
    login_page = LoginPage(driver)
    # Step 1: Login with standard user credentials
    login_page.login("standard_user", "secret_sauce")
    time.sleep(2)  # Wait for login to complete

    # Step 2: Check if the logout button is visible
    assert login_page.is_logout_button_visible(), "Logout button is not visible."
    print("Logout button is visible.")
    
    # Print a message indicating the test has passed successfully
    print("Test test_logout_button_visibility passed successfully.")
