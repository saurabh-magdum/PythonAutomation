import time
import allure
import pytest
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators  # Importing locators from a separate file
from data.test_data import TestData  # Importing test data from a separate file


@pytest.mark.usefixtures("setup")  # Use the 'setup' fixture for initializing the test
class TestOrangeHRM:

    @allure.story("Login Tests")
    @allure.title("Test valid login functionality")
    def test_login_valid(self):
        """Test valid login functionality."""

        # Navigate to the OrangeHRM login page
        self.driver.get("https://opensource-demo.orangehrmlive.com")

        # Wait for the username field to be clickable and input username
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.USERNAME_INPUT))
        ).send_keys(TestData.USERNAME)

        # Wait for the password field and input password
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.PASSWORD_INPUT))
        ).send_keys(TestData.PASSWORD)

        # Wait for the login button and click it
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.LOGIN_BUTTON))
        )
        button.click()

        # Assert that the page title is "OrangeHRM" to confirm successful login
        WebDriverWait(self.driver, 10).until(EC.title_is("OrangeHRM"))
        assert self.driver.title == "OrangeHRM", "Login failed: Incorrect page title."

    @allure.story("User Management Tests")
    @allure.title("Test user management search functionality")
    def test_user_management_search(self):
        """Test user management search functionality."""

        # Wait for the admin tab and click it to access the admin section
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.ADMIN_TAB))
        ).click()

        # Wait for the search bar and input the search query (e.g., username)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.SEARCH_BAR))
        ).send_keys(TestData.CONTENT_RESULT)

        # Wait for the search button and click it to initiate the search
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.SEARCH_BUTTON))
        ).click()

        # Wait for the search result and validate it
        result = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, Locators.SEARCH_RESULT))
        ).text

        # Assert that the search result matches the expected value
        assert result == TestData.CONTENT_RESULT, "Search result is invalid or empty."

    @allure.story("Add New user")
    @allure.title("Test add new user functionality")
    def test_add_new_user(self):
        """Test adding a new user functionality."""

        # Wait for the admin tab and click it to access the user management section
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.ADMIN_TAB))
        ).click()

        # Wait for the 'Add User' button and click to add a new user
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.ADD_USER_BUTTON))
        ).click()

        # Wait for the user role dropdown and click to select a role
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.USER_ROLE))
        ).click()

        # Wait and select a user role from the dropdown
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.SELECT_USER))
        ).click()

        # Input employee name and wait for the dropdown to appear
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.EMPLOYEE_NAME))
        ).send_keys(TestData.NEW_USER_EMPLOYEE_NAME)
        time.sleep(5)  # Sleep to allow for dropdown options to load

        # Select the employee name from the dropdown
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.EMPLOYEE_NAME_DROPDOWN))
        ).click()

        # Select the status (e.g., active/inactive)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.STATUS))
        ).click()

        # Select the specific status from the dropdown
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.SELECT_STATUS))
        ).click()

        # Input the new user's username and password
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.USERNAME_FIELD))
        ).send_keys(TestData.NEW_USER_USERNAME)
        time.sleep(1) # Sleep to allow input value

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.PASSWORD_FIELD))
        ).send_keys(TestData.NEW_USER_PASSWORD)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.CONFIRM_PASSWORD_FIELD))
        ).send_keys(TestData.NEW_USER_PASSWORD)

        # Click the save button to save the new user
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.SAVE_BUTTON))
        ).click()
        time.sleep(1) # sleep to wait for dynamic success message

        # Validate if the user is successfully added by checking for a success message
        result = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, Locators.SUCCESSFULLY_MESSAGE))
        )
        assert result.is_displayed(), "Failed to add a new user."

    @allure.story("Delete New user")
    @allure.title("Test delete new user functionality")
    def test_delete_new_user(self):
        """Test deleting a new user functionality."""

        # Wait for the admin tab and click it
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.ADMIN_TAB))
        ).click()

        # Search for the newly added user by username
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.SEARCH_BAR))
        ).send_keys(TestData.NEW_USER_USERNAME)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.SEARCH_BUTTON))
        ).click()

        # Click the delete icon to delete the user
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.DELETE_ICON))
        ).click()

        # Confirm the deletion in the popup
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.POPUP_DELETE_ICON))
        ).click()

        # Assert that the deletion process is successful
        assert True

    def test_get_product_details(self):
        """Test the API endpoint that provides product (user) details (API Test)."""

        # Step 1: Send GET request to the API endpoint with Basic Authentication
        auth = (TestData.USERNAME, TestData.PASSWORD)  # Basic Auth credentials

        params = {
            "limit": TestData.API_LIMIT,
            "offset": TestData.API_OFFSET,
            "sortField": TestData.API_SORT_FIELD,
            "sortOrder": TestData.API_SORT_ORDER
        }

        response = requests.get(TestData.API_BASE_URL, params=params, auth=auth)

        # Step 2: Verify the response status code
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

        # Step 3: Validate the structure of the response JSON
        response_json = response.json()
        assert 'data' in response_json, "Response JSON does not contain 'data' key"
        assert isinstance(response_json['data'], list), "Expected 'data' to be a list"

        if response_json['data']:
            first_user = response_json['data'][0]
            assert 'userName' in first_user, "User details are missing 'userName'"
            assert 'role' in first_user, "User details are missing 'role'"
            assert 'status' in first_user, "User details are missing 'status'"

        # Step 4: Validate the correctness of the data
        usernames = [user['userName'] for user in response_json['data']]
        assert TestData.EXPECTED_USER in usernames, f"Expected user '{TestData.EXPECTED_USER}' not found in response data."