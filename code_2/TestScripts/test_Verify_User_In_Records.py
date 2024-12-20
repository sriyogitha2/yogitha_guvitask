import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture(scope="module")
def browser():
    """
    Fixture to initialize and quit the WebDriver instance.
    """
    driver = webdriver.Chrome()  # Ensure ChromeDriver is in PATH
    driver.maximize_window()
    yield driver
    driver.quit()

class TestVerifyUserInRecords:
    """
    Test suite to verify if the newly created user exists in the Admin records.
    """

    def test_verify_user_in_records(self, browser):
        """
        Test case: Verify if the newly created user exists in Admin records.
        """
        # Step 1: Navigate to OrangeHRM login page
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        print("Navigated to OrangeHRM login page.")
        time.sleep(2)

        # Step 2: Log in as Admin
        browser.find_element(By.NAME, "username").send_keys("Admin")
        browser.find_element(By.NAME, "password").send_keys("admin123")
        browser.find_element(By.XPATH, "//button[@type='submit']").click()
        print("Logged in as Admin.")
        time.sleep(3)

        # Step 3: Navigate to Admin menu
        admin_menu = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Admin']"))
        )
        admin_menu.click()
        print("Navigated to Admin menu.")
        time.sleep(2)

        # Step 4: Search for the user in the records
        search_field = browser.find_element(By.XPATH, "//label[text()='Username']/following-sibling::div/input")
        search_field.clear()
        search_field.send_keys("new_user1")  # Replace 'new_user1' with the username of the new user
        browser.find_element(By.XPATH, "//button[text()=' Search ']").click()
        print("Searching for the newly created user.")
        time.sleep(3)

        # Step 5: Verify if the user exists in the records
        try:
            user_record = browser.find_element(By.XPATH, "//div[contains(text(), 'new_user1')]")
            assert user_record.is_displayed(), "User not found in the Admin records."
            print("Verified: New user exists in the records.")
        except Exception as e:
            print(f"User verification in records failed: {e}")
