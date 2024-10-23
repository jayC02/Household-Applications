from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

# Define the folder containing PDF files
pdf_folder_path = "C:\\Users\\Jayveer\\Building Portal\\Drawings"  # Replace with your actual folder path

# Placeholder description text
placeholder_description = "Placeholder description"  # You can customize this text as needed

# Set up the WebDriver (automatically manages ChromeDriver version)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Step 1: Assume user is already on the upload page
    driver.get("https://www.eplanning.scot/ePlanningClient/CustomPages/Applications/SupportingDocumentation.aspx")
    print("Opened Supporting Documentation page.")

    # Step 2: Read all PDF files from the specified folder
    pdf_files = [f for f in os.listdir(pdf_folder_path) if f.endswith('.pdf')]
    
    # Step 3: Loop through each PDF file in the folder and upload them
    for pdf_file in pdf_files:
        # Fill in the document title with the file name (without the extension)
        document_title_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "MainContent_edtDocumentTitle"))
        )
        document_title = os.path.splitext(pdf_file)[0]  # Remove the file extension for the title
        document_title_field.clear()
        document_title_field.send_keys(document_title)
        print(f"Entered document title: {document_title}")

        # Fill in the description field with the placeholder text
        description_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "MainContent_edtDescription"))
        )
        description_field.clear()
        description_field.send_keys(placeholder_description)
        print(f"Entered description: {placeholder_description}")

        # Attach the PDF file
        attach_file_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "MainContent_fuAttachFile"))
        )
        attach_file_path = os.path.join(pdf_folder_path, pdf_file)
        attach_file_input.send_keys(attach_file_path)
        print(f"Attached file: {attach_file_path}")

        # Tick the "Read and Understood" checkbox
        read_understood_checkbox = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "MainContent_rbReadAndUnderstood"))
        )
        read_understood_checkbox.click()
        print("Ticked 'Read and Understood' checkbox.")

        # Click the "Upload" button
        upload_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "MainContent_btnSaveDocEdit"))
        )
        upload_button.click()
        print(f"Clicked 'Upload' button for {pdf_file}.")

        # Wait for a few seconds to ensure the file is uploaded before proceeding with the next file
        time.sleep(5)

finally:
    # Close the browser after all files are uploaded
    input("All files processed. Press Enter to close the browser...")
    driver.quit()
