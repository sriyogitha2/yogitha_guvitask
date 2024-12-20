import requests  
from selenium import webdriver  
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager  
from TestLocators.locators import OrangeLocators  # Import the locators for the elements in the OrangeHRM application
from TestData.data import OrangeData  # Import test data such as URL, credentials, and other configurations
from Utilties.excel_functions import ExcelFunctions  # Import custom functions for handling Excel data
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  

class TestOrangeDDTF:

    def test_home_url(self):
        """
        Test to check if the home URL is accessible and responds with a status code 200.
        """
        # Send a GET request to the URL and store the response
        response = requests.get(OrangeData.url)
        
        # Assert that the status code of the response is 200, indicating the URL is working fine
        assert response.status_code == 200, f"Home URL is not working. Status Code: {response.status_code}"
        
        # Print a success message if the URL is working correctly
        print(f"Home URL is working fine: {OrangeData.url}")

    def test_login_excel(self):
        """
        Test to perform login using credentials read from an Excel file and verify login success/failure.
        """
        # Initialize Excel file path and sheet number from OrangeData class
        self.excel_file = OrangeData().excel_file
        self.sheet_number = OrangeData().sheet_number
        
        # Create an instance of ExcelFunctions class to read and write data from the Excel file
        self.excel = ExcelFunctions(self.excel_file, self.sheet_number)

        # Set up the WebDriver for Chrome browser
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(OrangeData.url)  # Navigate to the login page
        self.driver.maximize_window()  # Maximize the browser window

        # Initialize WebDriverWait to wait for elements to load on the page
        wait = WebDriverWait(self.driver, 10)

        # Get the number of rows in the Excel sheet to loop through for each login attempt
        self.rows = self.excel.row_count()

        # Loop through each row in the Excel sheet (starting from row 2 as row 1 is assumed to have headers)
        for row in range(2, self.rows + 1):
            # Read username and password from the Excel sheet
            username = self.excel.read_data(row, 6)  # Column 6 contains the username
            password = self.excel.read_data(row, 7)  # Column 7 contains the password

            try:
                # Wait for the username input field to be visible, then enter the username
                username_field = wait.until(EC.presence_of_element_located((By.XPATH, OrangeLocators.username_locators)))
                username_field.clear()  # Clear any pre-existing text
                username_field.send_keys(username)  # Enter the username

                # Wait for the password input field to be visible, then enter the password
                password_field = wait.until(EC.presence_of_element_located((By.XPATH, OrangeLocators.password_locators)))
                password_field.clear()  # Clear any pre-existing text
                password_field.send_keys(password)  # Enter the password

                # Wait for the login button to be clickable, then click the button
                login_button = wait.until(EC.element_to_be_clickable((By.XPATH, OrangeLocators.loginbutton_locators)))
                login_button.click()

                # Check if the current URL contains the dashboard URL to verify successful login
                if OrangeData.dashboard_url in self.driver.current_url:
                    print(f"Login successful for {username}")  # Print success message
                    self.excel.write_data(row, 8, "Test Pass")  # Update Excel with test result as "Test Pass"
                    self.driver.back()  # Go back to the login page for the next test case
                else:
                    print(f"Login failed for {username}")  # Print failure message
                    self.excel.write_data(row, 8, "Test Fail")  # Update Excel with test result as "Test Fail"
                    self.driver.refresh()  # Refresh the page for the next attempt

            except Exception as e:
                # If any exception occurs during the login process, mark the test as "Test Fail"
                print(f"Login failed for {username} due to an error: {e}")
                self.excel.write_data(row, 8, "Test Fail")
                self.driver.refresh()  # Refresh the page for the next attempt

        # Quit the WebDriver after all login attempts are completed
        self.driver.quit()

    def test_input_boxes_visibility(self):
        """
        Test to check the visibility of the username and password input boxes on the login page.
        """
        # Set up the WebDriver for Chrome browser
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(OrangeData.url)  # Navigate to the login page
        self.driver.maximize_window()  # Maximize the browser window

        # Initialize WebDriverWait to wait for elements to load on the page
        wait = WebDriverWait(self.driver, 10)

        try:
            # Wait for the username input box to be visible and assert that it's displayed
            username_field = wait.until(EC.presence_of_element_located((By.XPATH, OrangeLocators.username_locators)))
            assert username_field.is_displayed(), "Username input box is not visible"
            print("Username input box is visible.")  # Print success message if the username box is visible

            # Wait for the password input box to be visible and assert that it's displayed
            password_field = wait.until(EC.presence_of_element_located((By.XPATH, OrangeLocators.password_locators)))
            assert password_field.is_displayed(), "Password input box is not visible"
            print("Password input box is visible.")  # Print success message if the password box is visible
        
        except Exception as e:
            # If any exception occurs during the visibility check, mark the test as failed
            print(f"Error during visibility check: {e}")
            assert False, "Visibility test failed."  # Fail the test if there's an error during the visibility check

        # Quit the WebDriver after the visibility test is completed
        self.driver.quit()
