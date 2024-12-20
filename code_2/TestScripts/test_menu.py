import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class OrangeData:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"  # Correct username
    password = "admin123"  # Correct password

class OrangeLocators:
    # Login page locators
    username_locators = "//input[@name='username']"
    password_locators = "//input[@name='password']"
    loginbutton_locators = "//button[@type='submit']"

    # Updated Menus locators after copying from the Inspect tool
    admin_locators = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span'  # Ensure this XPath is correct
    pim_locators = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span'  # Ensure this XPath is correct
    leave_locators = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a/span'  # Ensure this XPath is correct
    time_locators = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a/span'  # Ensure this XPath is correct
    recruitment_locators = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span'  # Ensure this XPath is correct
    myinfo_locators = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span'  # Ensure this XPath is correct
    performance_locators = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span'  # Ensure this XPath is correct
    dashboard_locators = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a/span'  # Ensure this XPath is correct

class TestOrangeMenus:

    @pytest.fixture(scope="class")
    def setup(self):
        """Fixture to setup WebDriver for test."""
        driver = webdriver.Chrome()
        driver.get(OrangeData.url)
        driver.maximize_window()
        yield driver  # This makes the driver available in test methods
        driver.quit()

    def test_login_and_check_menus(self, setup):
        """Test login and check if dashboard menus are visible."""
        driver = setup  # Use the driver passed from the fixture
        wait = WebDriverWait(driver, 30)  # Increased wait time to ensure page loads

        # Login process
        try:
            # Wait for the username field and enter the username
            username_field = wait.until(EC.visibility_of_element_located((By.XPATH, OrangeLocators.username_locators)))
            username_field.send_keys(OrangeData.username)

            # Wait for the password field and enter the password
            password_field = wait.until(EC.visibility_of_element_located((By.XPATH, OrangeLocators.password_locators)))
            password_field.send_keys(OrangeData.password)

            # Wait for the login button to be clickable and click
            login_button = wait.until(EC.element_to_be_clickable((By.XPATH, OrangeLocators.loginbutton_locators)))
            login_button.click()

            # Wait for the dashboard page to load by checking the URL
            wait.until(EC.url_contains("dashboard"))

            # Confirm that the dashboard page is loaded and check menu visibility
            print("Successfully logged in and dashboard loaded.")

            # List of menu items and their updated locators
            menu_items = [
                ("Admin", OrangeLocators.admin_locators),
                ("PIM", OrangeLocators.pim_locators),
                ("Leave", OrangeLocators.leave_locators),
                ("Time", OrangeLocators.time_locators),
                ("Recruitment", OrangeLocators.recruitment_locators),
                ("My Info", OrangeLocators.myinfo_locators),
                ("Performance", OrangeLocators.performance_locators),
                ("Dashboard", OrangeLocators.dashboard_locators),
            ]

            # Check visibility for each menu item
            for menu_name, menu_locator in menu_items:
                try:
                    menu_item = wait.until(EC.visibility_of_element_located((By.XPATH, menu_locator)))
                    assert menu_item.is_displayed(), f"{menu_name} menu is not visible"
                    print(f"{menu_name} menu is visible: PASS")
                except TimeoutException:
                    print(f"{menu_name} menu did not load in time.")
                    assert False, f"{menu_name} menu did not load in time."
                except AssertionError:
                    print(f"{menu_name} menu is not visible.")
                    assert False, f"{menu_name} menu is not visible."

        except TimeoutException:
            print("Login failed or Dashboard did not load in time.")
            assert False, "Login failed or Dashboard did not load in time."
