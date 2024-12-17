# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.CSS_SELECTOR, "input[type='submit']")
        self.inventory_container = (By.CLASS_NAME, "inventory_container")
        self.burger_menu_button = (By.ID, "react-burger-menu-btn")  # Burger menu button
        self.logout_link = (By.ID, "logout_sidebar_link")  # Logout link

    def login(self, username, password):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def check_login_success(self):
        try:
            self.driver.find_element(*self.inventory_container)
            print("Login successful!")
        except:
            print("Login failed!")

    def get_cookies(self):
        return self.driver.get_cookies()

    def is_logout_button_visible(self):
        """Check if the Logout button is visible."""
        try:
            self.driver.find_element(*self.burger_menu_button).click()
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.logout_link)
            )
            return True
        except:
            return False

    def click_logout(self):
        """Click the Logout button to log out."""
        self.driver.find_element(*self.burger_menu_button).click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.logout_link)
        ).click()
