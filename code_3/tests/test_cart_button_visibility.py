# tests/test_cart_button_visibility.py
import pytest
import sys
import os
from pages.login_page import LoginPage
from utils.driver_setup import DriverSetup
from selenium.webdriver.common.by import By
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture(scope="module")
def driver():
    driver = DriverSetup().initialize_driver()
    yield driver
    driver.quit()

# Test Cart Button Visibility
def test_cart_button_visibility(driver):
    print("\nStarting test: test_cart_button_visibility")
    login_page = LoginPage(driver)

    # Login with standard user credentials
    login_page.login("standard_user", "secret_sauce")
    time.sleep(2)  # Wait for login to complete

    # Check if Cart button is visible
    cart_button = driver.find_element(By.ID, "shopping_cart_container")  # Cart button ID
    assert cart_button.is_displayed(), "Cart button is not visible."
    print("Cart button is visible.")
    print("Test test_cart_button_visibility passed successfully.")
