from selenium.webdriver.common.by import By  # Import By for locating elements
from selenium.webdriver.support.ui import WebDriverWait  # Import WebDriverWait for explicit waits
from selenium.webdriver.support import expected_conditions as EC  # Import EC for defining wait conditions


class HomePage:
    """Page class representing the homepage of the Guvi website."""

    # Locators for elements on the homepage
    LOGIN_BTN = (By.ID, "login-btn")  # Locator for the login button
    SIGNUP_BTN = (By.XPATH, "/html/body/div[1]/div/div[5]/div/div[2]/a")  # Locator for the signup button

    def __init__(self, driver):
        """Initialize the HomePage instance with the WebDriver."""
        self.driver = driver  # Assign the driver instance to a class variable

    def click_login(self):
        """Click the login button."""
        # Wait for the login button to be visible on the page
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.LOGIN_BTN)  # Ensures the login button is visible
        )
        # Wait for the login button to be clickable
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.LOGIN_BTN)  # Ensures the login button is clickable
        ).click()  # Click the login button
