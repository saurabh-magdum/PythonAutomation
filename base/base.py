from selenium import webdriver


class Base:
    def __init__(self, driver=None):
        # Initialize the driver attribute, default is None
        self.driver = driver

    def setup_driver(self, browser):
        # Method to set up the WebDriver based on the browser choice
        # Input: browser (string) - the browser to initialize (chrome, firefox, edge)

        if browser == "chrome":
            # Initialize the Chrome WebDriver if browser is 'chrome'
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            # Initialize the Firefox WebDriver if browser is 'firefox'
            self.driver = webdriver.Firefox()
        elif browser == "edge":
            # Initialize the Edge WebDriver if browser is 'edge'
            self.driver = webdriver.Edge()
        else:
            # Raise an exception for unsupported browsers
            raise ValueError(f"Unsupported browser: {browser}")

        # Maximize the browser window for better visibility during tests
        self.driver.maximize_window()
        return self.driver

    def teardown(self):
        # Method to close and clean up the WebDriver after tests are done
        if self.driver:
            self.driver.quit()  # Close the browser and end the session
