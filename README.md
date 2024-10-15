# OrangeHRM Automation Framework

## Overview

This framework is designed for automating tests on the OrangeHRM application using Selenium WebDriver and pytest. 
It includes functionalities for user login, user management, and API testing, 
along with the ability to generate Allure reports for detailed test results.

## Features

- **Modular Code Structure**: Separate files for test data, locators, and base functionality.
- **Page Object Model**: Organized locators and actions for better maintainability.
- **Test Reporting**: Allure integration for enhanced test reporting.
- **Screenshot on Failure**: Automatically captures screenshots for failed tests.
- **Cross-Browser Testing**: Supports multiple browsers (Chrome, Firefox, Edge).

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.x**: Ensure that Python is added to your system's PATH.
- **Pip**: This should come with Python; verify installation by running `pip --version`.
- **WebDriver**: Install the appropriate WebDriver for the browser you intend to use: 
- **pytest**: The testing framework that needs to be installed via pip.
- **Allure**: Commandline tool for generating reports (installation instructions provided in the README).
- **Selenium**: The Python package for browser automation, included in `requirements.txt`.


## Installation

1. **Clone the Repository:**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-directory>
