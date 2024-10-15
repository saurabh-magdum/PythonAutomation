import os
import pytest
from base.base import Base

# Define the path for the screenshots folder
SCREENSHOT_DIR = 'C:/Users/KUNAL/Desktop/Screenshots/'  # screenshot folder path, please add your path

# Create the screenshots directory if it doesn't exist
if not os.path.exists(SCREENSHOT_DIR):
    os.makedirs(SCREENSHOT_DIR)


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser to use (chrome, firefox, edge)"
    )


@pytest.fixture(scope="class")
def setup(request):
    """Fixture to set up the WebDriver before tests."""
    base = Base()
    browser = request.config.getoption("--browser")
    driver = base.setup_driver(browser)
    request.cls.driver = driver
    yield
    base.teardown()


@pytest.fixture(autouse=True)
def take_screenshot_on_failure(request):
    """Automatically take a screenshot if a test fails and print the screenshot path."""
    yield  # Run the test first
    if request.node.rep_call.failed:  # Check if the test failed
        # Only take a screenshot if the driver is available
        if hasattr(request.cls, 'driver') and request.cls.driver:
            test_name = request.node.name  # Test name to use for the screenshot filename
            screenshot_path = os.path.join(SCREENSHOT_DIR, f"{test_name}.png")  # Path to save screenshot
            request.cls.driver.save_screenshot(screenshot_path)  # Save the screenshot
            print(f"Screenshot saved: {screenshot_path}")  # Print the screenshot path in the console
        else:
            print("No driver found, cannot take a screenshot.")
