from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from TestLocators.locators import HRMLocators
from TestData.data import HRMData
from Utilities.excel_functions import ExcelFunctions


class TestOrangeDDTF:

    def test_login_excel(self):
        # Load test data
        excel_file = HRMData.excel_file
        sheet_name = HRMData.sheet_number
        excel = ExcelFunctions(excel_file, sheet_name)

        # Initialize WebDriver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(HRMData.url)
        driver.maximize_window()
        driver.implicitly_wait(10)

        # Fetch row count from Excel
        rows = excel.row_count()

        for row in range(2, rows + 1):  # Skipping header row (assumed at row 1)
            username = excel.read_data(row, 3)  # Column 3 for username
            password = excel.read_data(row, 4)  # Column 4 for password

            try:
                # Wait for and interact with the username field
                username_field = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.NAME, HRMLocators.username_locator))
                )
                username_field.clear()
                username_field.send_keys(username)

                # Wait for and interact with the password field
                password_field = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.NAME, HRMLocators.password_locator))
                )
                password_field.clear()
                password_field.send_keys(password)

                # Click the login button
                login_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, HRMLocators.loginbutton_locator))
                )
                login_button.click()

                # Validate the result
                if HRMData.dashboard_url in driver.current_url:
                    print(f"Success: Login successful for row {row}")
                    excel.write_data(row, 7, "Test Pass")  # Write 'Test Pass' in column 7
                    driver.get(HRMData.url)  # Navigate back to login page for next test
                else:
                    print(f"Fail: Login failed for row {row}")
                    excel.write_data(row, 7, "Test Failed")  # Write 'Test Failed' in column 7

            except Exception as e:
                print(f"Error on row {row}: {e}")
                # Write a generic "Test Failed" in the Excel sheet to avoid dumping stack traces
                excel.write_data(row, 7, "Test Failed")

        # Quit the driver
        driver.quit()
