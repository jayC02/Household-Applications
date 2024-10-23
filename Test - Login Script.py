import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Retrieve credentials from environment variables
username = os.getenv("EDEV_USERNAME")
password = os.getenv("EDEV_PASSWORD")

# Check if credentials are retrieved successfully
if not username or not password:
    raise ValueError("Please set your environment variables for 'EDEV_USERNAME' and 'EDEV_PASSWORD'.")

# Set up the WebDriver (automatically manages ChromeDriver version)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Step 1: Open the eDevelopment login page
    driver.get("https://www.edevelopment.scot/eDevelopmentClient/default.aspx")

    # Step 2: Locate the username input field and enter your username
    username_field = driver.find_element(By.ID, "MainContentPlaceHolder_LoginControl_UserName")
    username_field.send_keys(username)

    # Step 3: Locate the password input field and enter your password
    password_field = driver.find_element(By.ID, "MainContentPlaceHolder_LoginControl_Password")
    password_field.send_keys(password)

    # Step 4: Locate the login button and click it
    login_button = driver.find_element(By.ID, "MainContentPlaceHolder_LoginControl_LoginButton")
    login_button.click()

    # Wait for a while to ensure the login process completes
    time.sleep(5)

    # You can add additional code here to verify login success or perform further actions
    print("Login attempted. Check the browser for results.")

finally:
    # Close the browser after the script runs
    driver.quit()
