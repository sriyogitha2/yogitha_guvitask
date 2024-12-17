# tests/test_fetch_random_products.py
import pytest
import sys
import os
import random
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

# Test to fetch random 4 products and their details
def test_fetch_random_products(driver):
    print("\nStarting test: test_fetch_random_products")
    login_page = LoginPage(driver)

    # Step 1: Login with standard user credentials
    login_page.login("standard_user", "secret_sauce")
    time.sleep(2)  # Wait for login to complete
    
    # Step 2: Locate all product names and prices on the inventory page
    product_name_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    product_price_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

    # Step 3: Ensure there are six products on the page
    assert len(product_name_elements) == 6, "Expected 6 products, but found a different number."

    # Step 4: Combine product names and prices into a list of tuples
    products = [(name.text, price.text) for name, price in zip(product_name_elements, product_price_elements)]
    
    # Step 5: Randomly select 4 products out of the 6
    selected_products = random.sample(products, 4)
    
    # Step 6: Print the selected products and their prices
    print("Selected 4 random products:")
    for idx, (name, price) in enumerate(selected_products, start=1):
        print(f"Product {idx}: {name} - Price: {price}")

    print("Test test_fetch_random_products passed successfully.")
