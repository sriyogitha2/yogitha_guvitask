# Import necessary modules for interacting with elements and handling expected conditions in Selenium.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the LoginPage class to handle login-related actions on the webpage.
class LoginPage:
    # Initialize the LoginPage class with the WebDriver instance.
    def __init__(self, driver):
        self.driver = driver
        # Locate the username field by ID.
        self.username_field = (By.ID, "user-name")
        # Locate the password field by ID.
        self.password_field = (By.ID, "password")
        # Locate the login button by its CSS selector.
        self.login_button = (By.CSS_SELECTOR, "input[type='submit']")
        # Locate the inventory container by its class name to verify successful login.
        self.inventory_container = (By.CLASS_NAME, "inventory_container")
        # Locate the burger menu button by its ID.
        self.burger_menu_button = (By.ID, "react-burger-menu-btn")
        # Locate the logout link in the sidebar by its ID.
        self.logout_link = (By.ID, "logout_sidebar_link")

    # Method to perform login by entering the username and password.
    def login(self, username, password):
        # Open the website.
        self.driver.get("https://www.saucedemo.com/")
        # Input the username in the username field.
        self.driver.find_element(*self.username_field).send_keys(username)
        # Input the password in the password field.
        self.driver.find_element(*self.password_field).send_keys(password)
        # Click the login button to submit the form.
        self.driver.find_element(*self.login_button).click()

    # Method to check if the login is successful by looking for the inventory container element.
    def check_login_success(self):
        try:
            # Try to find the inventory container element on the page.
            self.driver.find_element(*self.inventory_container)
            # If found, print login success message.
            print("Login successful!")
        except:
            # If element is not found, print login failure message.
            print("Login failed!")

    # Method to retrieve the cookies after login.
    def get_cookies(self):
        # Return all cookies stored in the browser.
        return self.driver.get_cookies()

    # Method to check if the logout button is visible on the page.
    def is_logout_button_visible(self):
        """Check if the Logout button is visible."""
        try:
            # Click the burger menu to reveal the logout link.
            self.driver.find_element(*self.burger_menu_button).click()
            # Wait for the logout link to become visible within 5 seconds.
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.logout_link)
            )
            # Return True if the logout link is visible.
            return True
        except:
            # Return False if the logout link is not visible.
            return False

    # Method to perform logout by clicking the logout button.
    def click_logout(self):
        """Click the Logout button to log out."""
        # Click the burger menu to open the sidebar.
        self.driver.find_element(*self.burger_menu_button).click()
        # Wait for the logout link to become clickable within 5 seconds and click it.
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.logout_link)
        ).click()