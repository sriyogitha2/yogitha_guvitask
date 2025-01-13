from selenium.webdriver.common.by import By  # Import By for locating elements


class LoginPage:
    """Page class for the login page."""

    # Locators for the elements on the login page
    EMAIL_FIELD = (By.ID, "email")  # Locator for the email input field
    PASSWORD_FIELD = (By.ID, "password")  # Locator for the password input field
    SUBMIT_BTN = (By.ID, "login-btn")  # Locator for the login button
    ERROR_MSG = (By.XPATH, "//div[contains(text(), 'Incorrect Email or Password')]")  # Locator for the error message

    def __init__(self, driver):
        """Initialize the LoginPage instance with the WebDriver."""
        self.driver = driver  # Assign the driver instance to a class variable

    def login(self, email, password):
        """Perform login action."""
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)  # Enter the email in the email field
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)  # Enter the password in the password field
        self.driver.find_element(*self.SUBMIT_BTN).click()  # Click the login button

    def get_error_message(self):
        """Retrieve the error message after failed login."""
        return self.driver.find_element(*self.ERROR_MSG).text.strip()  # Get the text of the error message and strip whitespace
