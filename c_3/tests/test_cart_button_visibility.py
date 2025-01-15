# Import necessary modules for testing
import pytest
import sys
import os
from pages.login_page import LoginPage  # Import LoginPage class for login functionality
from utils.driver_setup import DriverSetup  # Import DriverSetup to initialize the driver
from selenium.webdriver.common.by import By  # For locating web elements
import time  # For adding delays between actions

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

# Test to check if the Cart button is visible after login
def test_cart_button_visibility(driver):
    # Print a message indicating the start of the test
    print("\nStarting test: test_cart_button_visibility")
    
    # Initialize the LoginPage object to perform login actions
    login_page = LoginPage(driver)

    # Step 1: Login with standard user credentials
    login_page.login("standard_user", "secret_sauce")
    time.sleep(2)  # Wait for the login process to complete

    # Step 2: Check if the Cart button is visible
    cart_button = driver.find_element(By.ID, "shopping_cart_container")  # Locate Cart button by ID
    # Assert that the Cart button is visible, else raise an assertion error
    assert cart_button.is_displayed(), "Cart button is not visible."
    # Print confirmation that the Cart button is visible
    print("Cart button is visible.")
    
    # Step 3: Print a message indicating the test has passed successfully
    print("Test test_cart_button_visibility passed successfully.")
