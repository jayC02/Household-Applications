import PyPDF2  # Import PyPDF2 for reading the PDF
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

# Step 0: Set up credentials and paths
username = "jayveerchall17@gmail.com"
password = "Helloman231#"

# Step 1: Set up the WebDriver (automatically manages ChromeDriver version)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Step 2: Open the eDevelopment main page
    driver.get("https://www.edevelopment.scot/eDevelopmentClient/default.aspx")
    print("Opened eDevelopment main page.")

    # Step 3: Wait for the initial "Login" button on the main page and click it
    initial_login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "Banner_btnLogin"))
    )
    initial_login_button.click()
    print("Clicked initial login button.")

    # Step 4: Wait for the login page to load completely by checking the presence of the email field
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "MainContent_UclLogin_LoginWizard_TbxEmail"))
    )
    print("Navigated to the login page successfully and email field found.")

    # Step 5: Enter email
    email_field.send_keys(username)
    print("Entered email.")

    # Step 6: Wait for the "Password" input field to be present and enter password
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "MainContent_UclLogin_LoginWizard_TbxPassword"))
    )
    password_field.send_keys(password)
    print("Entered password.")

    # Step 7: Wait for the "Login" button on the login page to be present and click it
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "MainContent_UclLogin_LoginWizard_BtnLogin"))
    )
    login_button.click()
    print("Clicked final login button.")

    # Step 8: Click the 'eBuilding Standards' button
    ebuilding_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "ctl00$sideBar$ctl11"))
    )
    ebuilding_button.click()
    print("Clicked 'eBuilding Standards' button.")

    # Step 9: Wait until the user has navigated to the Building Warrant Application Main Details page
    while driver.current_url != "https://www.ebuildingstandards.scot/eBuildingStandardsClient/CustomPages/Applications/BuildingWarrantApplicationMainDetails.aspx":
        input("Please navigate to the 'Building Warrant Application Main Details' page and press Enter to continue...")

    # Step 10: Click the 'Next' button
    print("Clicking 'Next' button on Building Warrant Application Main Details page.")
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "MainContent_BuildingWarrantAppWizard_StepNavigationTemplateContainerID_btnNext"))
    )
    next_button.click()

      # Step 11: Tick the 'No' radio button
    print("Ticking 'No' radio button for 'Work Completed'.")
    no_radio_label = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[@for='MainContent_BuildingWarrantAppWizard_rbWorkCompletedNo']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", no_radio_label)
    no_radio_label.click()  # Click the label for the 'No' radio button
    time.sleep(2)  # Adding delay to ensure any JavaScript processing completes
    
    # Step 12: Click the 'Next' button again
    print("Clicking 'Next' button after ticking 'No' for 'Work Completed'.")
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "MainContent_BuildingWarrantAppWizard_StepNavigationTemplateContainerID_btnNext"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
    time.sleep(1)  # Adding a slight delay to ensure button is ready
    driver.execute_script("arguments[0].click();", next_button)  # Using JavaScript to click the button
    
     # Step 13: Tick the 'No' radio button again
    print("Ticking 'No' radio button again for confirmation.")
    no_radio_label = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[@for='MainContent_BuildingWarrantAppWizard_rbWorkStartedNo']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", no_radio_label)
    no_radio_label.click()  # Click the label for the 'No' radio button
    time.sleep(2)  # Adding delay to ensure any JavaScript processing completes

    # Step 14: Click the 'Next' button again
    print("Clicking 'Next' button again after confirming 'No'.")
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "MainContent_BuildingWarrantAppWizard_StepNavigationTemplateContainerID_btnNext"))
    )
    next_button.click()
    
   # Step 15: Select the 'Agent' radio button
    print("Selecting 'Agent' radio button.")
    agent_radio_label = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[@for='MainContent_BuildingWarrantAppWizard_ApplicantOrAgent_rbAgent']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", agent_radio_label)
    agent_radio_label.click()  # Click the label for the 'Agent' radio button

    # Step 16: Select registered account details
    print("Selecting 'Registered Account Details Button' radio button.")
    registered_radio_label = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[@for='MainContent_BuildingWarrantAppWizard_ApplicantOrAgent_rbAccountYes']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", registered_radio_label)
    driver.execute_script("arguments[0].click();", registered_radio_label)  # Using JavaScript to click the label
    
    # Step 17: Click the 'Next' button again
    print("Clicking 'Next' button again after confirming 'No'.")
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "MainContent_BuildingWarrantAppWizard_StepNavigationTemplateContainerID_btnNext"))
    )
    next_button.click()
    print("Clicked 'Next' button again.")
    
    # Step 18: Pause for manual user input
    input("Finish entering details for registerd account (autofill) and Applicant Details. Hit 'Enter' to Continue")

finally:
    # Step 16: Keep the browser open after all files are uploaded
    input("All files processed. Press Enter to close the browser...")
    driver.quit()
