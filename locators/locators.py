class Locators:
    # Login Page Locators
    USERNAME_INPUT = "//input[@placeholder='Username']"
    PASSWORD_INPUT = "//input[@placeholder='Password']"
    LOGIN_BUTTON = "//button[@type='submit']"

    # Dashboard Locators
    USER_MENU = "//div[@class='oxd-topbar-header-title']/span"

    # User Management Locators
    ADMIN_TAB = "//span[text()='Admin']"
    SEARCH_BAR = "(//input[@class='oxd-input oxd-input--active'])[2]"
    SEARCH_BUTTON = "//button[@type='submit']"
    SEARCH_RESULT = '(//div[@class="oxd-table-row oxd-table-row--with-border"])[2]/div[2]'
    ADD_USER_BUTTON = "//i[@class='oxd-icon bi-plus oxd-button-icon']"
    USER_ROLE = "//div[@class='oxd-select-text-input']"
    SELECT_USER = "(//span[text()='Admin'])[2]"
    EMPLOYEE_NAME = "//input[@placeholder='Type for hints...']"
    EMPLOYEE_NAME_DROPDOWN = "(//div[@role='option'])[1]"
    STATUS = "(//div[@class='oxd-select-text-input'])[2]"
    SELECT_STATUS = "//span[text()='Enabled']"
    USERNAME_FIELD = "(//input[@class='oxd-input oxd-input--active'])[2]"
    PASSWORD_FIELD = "(//input[@type='password'])[1]"
    CONFIRM_PASSWORD_FIELD = "(//input[@type='password'])[2]"
    SAVE_BUTTON = "//button[@type='submit']"
    SUCCESSFULLY_MESSAGE = "//div[@class='oxd-toast-content oxd-toast-content--success']"

    # User delete Locators
    DELETE_ICON = "//i[@class='oxd-icon bi-trash']"
    POPUP_DELETE_ICON = "//i[@class='oxd-icon bi-trash oxd-button-icon']"
