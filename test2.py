import PyPDF2  # Import PyPDF2 for reading the PDF
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

# Function to extract paper size from PDF file by searching for the "A" followed by a number (e.g., A4)
def get_paper_size_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        extracted_text = ""
        # Extract text from the first page
        first_page = reader.pages[0]
        extracted_text += first_page.extract_text()

        # Search for paper size in the text (e.g., "A4", "A1", etc.)
        if "A0" in extracted_text:
            return "A0"
        elif "A1" in extracted_text:
            return "A1"
        elif "A2" in extracted_text:
            return "A2"
        elif "A3" in extracted_text:
            return "A3"
        elif "A4" in extracted_text:
            return "A4"
        else:
            return "Not Applicable"  # Default if no size is found

# Function to determine document type from PDF content
def get_document_type_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        extracted_text = ""
        # Extract text from the first page
        first_page = reader.pages[0]
        extracted_text += first_page.extract_text()

        # Map keywords to document types
        if "Drawing" in pdf_path or any(word in extracted_text.lower() for word in ["plan", "ELEVATION", "drawing", "GROUND FLOOR", "LOCATION PLAN"]):
            return "Drawing"
        elif "Report" in pdf_path or any(word in extracted_text.lower() for word in ["report", "analysis", "summary"]):
            return "Report"
        elif "Photo" in pdf_path or any(word in extracted_text.lower() for word in ["photo", "image"]):
            return "Photo"
        else:
            return "Other"  # Default to "Other" if no keywords are matched
        
# Function to extract document title and description based on filename
def extract_title_and_description_from_filename(filename):
    # Split filename on underscore ('_')
    parts = filename.split('_')
    
    if len(parts) >= 2:
        title = parts[0]  # Everything before the underscore is the title
        description = ' '.join(parts[1:])  # Everything after the underscore is the description
    else:
        title = filename
        description = filename
    
    return title, description

        
# Set up credentials and paths
username = "jayveerchall17@gmail.com"
password = "Helloman231#"
pdf_folder_path = "C:\\Users\\Jayveer\\Building Portal\\Drawings"  # Replace with your actual folder path
placeholder_description = "Placeholder description"  # Placeholder text for the description field

# Set up the WebDriver (automatically manages ChromeDriver version)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Step 1: Open the eDevelopment main page
    driver.get("https://www.edevelopment.scot/eDevelopmentClient/default.aspx")
    print("Opened eDevelopment main page.")

    # Step 2: Wait for the initial "Login" button on the main page and click it
    initial_login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "Banner_btnLogin"))
    )
    initial_login_button.click()
    print("Clicked initial login button.")

    # Step 3: Wait for the login page to load completely by checking the presence of the email field
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "MainContent_UclLogin_LoginWizard_TbxEmail"))
    )
    print("Navigated to the login page successfully and email field found.")

    # Step 4: Enter email
    email_field.send_keys(username)
    print("Entered email.")

    # Step 5: Wait for the "Password" input field to be present and enter password
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "MainContent_UclLogin_LoginWizard_TbxPassword"))
    )
    password_field.send_keys(password)
    print("Entered password.")

    # Step 6: Wait for the "Login" button on the login page to be present and click it
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "MainContent_UclLogin_LoginWizard_BtnLogin"))
    )
    login_button.click()
    print("Clicked final login button.")

    # Step 7: Wait for the "ePlanning" button and click it to navigate to the ePlanning page
    eplanning_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "ctl00$sideBar$ctl13"))  # Use the provided name attribute for ePlanning button
    )
    eplanning_button.click()
    print("Clicked ePlanning button and redirected to ePlanning page.")

    # Step 8: Wait for the "New Proposal" button and click it
    new_proposal_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "MainContent_newProposal"))  # Use the provided ID attribute for New Proposal button
    )
    new_proposal_button.click()
    print("Clicked 'New Proposal' button. Now on the Create Proposal page.")

    # Step 9: Pause the script to allow user to enter details manually
    input("Please enter the required details on the 'Create Proposal' page and navigate to the 'Supporting Documentation' page. Press Enter to continue...")

    # Step 10: Confirm the user is on the "Supporting Documentation" page
    if driver.current_url != "https://www.eplanning.scot/ePlanningClient/CustomPages/Applications/SupportingDocumentation.aspx":
        input("Please navigate to the 'Supporting Documentation' page. Press Enter when ready...")

    # Step 11: Start uploading documents
    print("Starting document upload process...")

    # Step 12: Read all PDF files from the specified folder
    pdf_files = [f for f in os.listdir(pdf_folder_path) if f.endswith('.pdf')]
    if len(pdf_files) == 0:
        raise FileNotFoundError("No PDF files found in the specified folder.")

    # Loop through each PDF file in the folder and upload them
    for pdf_file in pdf_files:
        print(f"Processing file: {pdf_file}")
        
        # Step 13: Extract title and description from filename
        title, description = extract_title_and_description_from_filename(os.path.splitext(pdf_file)[0])

        # Step 14: Fill in the document title with the extracted title
        document_title_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "MainContent_edtDocumentTitle"))
        )
        document_title_field.clear()
        document_title_field.send_keys(title)
        print(f"Entered document title: {title}")

        # Step 15: Fill in the description field with the extracted description
        description_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "MainContent_edtDescription"))
        )
        description_field.clear()
        description_field.send_keys(description)
        print(f"Entered description: {description}")

        # Step 16: Automatically detect paper size from the PDF
        attach_file_path = os.path.join(pdf_folder_path, pdf_file)
        paper_size = get_paper_size_from_pdf(attach_file_path)
        paper_size_dropdown = Select(WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "MainContent_lbPaperSize"))
        ))
        paper_size_dropdown.select_by_visible_text(paper_size)
        print(f"Detected and selected paper size: {paper_size}")

       # Step 17: Automatically detect document type from the PDF
        document_type = get_document_type_from_pdf(attach_file_path)
        document_type_dropdown = Select(WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "MainContent_lbDocumentType"))
        ))
        document_type_dropdown.select_by_visible_text(document_type)
        print(f"Detected and selected document type: {document_type}")

        # Step 18: Attach the PDF file
        attach_file_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "MainContent_fuAttachFile"))
        )
        attach_file_input.send_keys(attach_file_path)
        print(f"Attached file: {attach_file_path}")

        # Step 19: Directly set the "Read and Understood" checkbox using JavaScript
        try:
            read_understood_checkbox = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "MainContent_rbReadAndUnderstood"))
            )
            driver.execute_script("arguments[0].checked = true;", read_understood_checkbox)  # Directly set checkbox to checked
            print("Ticked 'Read and Understood' checkbox using JavaScript.")
        except Exception as e:
            print(f"Failed to set 'Read and Understood' checkbox directly: {e}. Retrying...")
            # Fallback to click on the label if direct setting fails
            checkbox_label = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='MainContent_rbReadAndUnderstood']"))
            )
            driver.execute_script("arguments[0].click();", checkbox_label)
            print("Clicked the label for 'Read and Understood' checkbox as fallback.")

        # Step 20: Ensure button is in view and click the "Upload" button
        upload_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "MainContent_btnSaveDocEdit"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", upload_button)
        driver.execute_script("arguments[0].click();", upload_button)  # Use JavaScript to click
        print(f"Clicked 'Upload' button for {pdf_file}.")

        # Step 21: Wait for the upload to complete or the page to refresh
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://www.eplanning.scot/ePlanningClient/CustomPages/Applications/SupportingDocumentation.aspx")
        )
        print("Upload completed and returned to 'Supporting Documentation' page.")

        # Step 22: Click the "Add Document Details" button
        add_document_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "MainContent_btnAddDocumentation"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", add_document_button)
        driver.execute_script("arguments[0].click();", add_document_button)  # Use JavaScript to click
        print("Clicked 'Add Document Details' button.")

        # Step 23: Directly set the "Uploaded" radio button using JavaScript
        try:
            uploaded_radio_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "MainContent_rbUploaded"))
            )
            driver.execute_script("arguments[0].checked = true;", uploaded_radio_button)  # Directly set radio button to checked
            print("Ticked 'Uploaded' radio button using JavaScript.")
        except Exception as e:
            print(f"Failed to set 'Uploaded' radio button directly: {e}. Retrying...")
            # Fallback to click on the label if direct setting fails
            radio_label = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='MainContent_rbUploaded']"))
            )
            driver.execute_script("arguments[0].click();", radio_label)
            print("Clicked the label for 'Uploaded' radio button as fallback.")

        # Step 24: Click the "Continue" button
        try:
            continue_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "MainContent_btnAttachmentContinue"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", continue_button)
            driver.execute_script("arguments[0].click();", continue_button)  # Use JavaScript to click
            print("Clicked 'Continue' button.")
        except Exception as e:
            print(f"Failed to click 'Continue' button: {e}. Retrying...")
            time.sleep(2)  # Wait for 2 seconds before retrying
            continue_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "MainContent_btnAttachmentContinue"))
            )
            driver.execute_script("arguments[0].click();", continue_button)  # Retry clicking
            print("Retried and clicked 'Continue' button.")

        # Wait a few seconds to ensure the page has reloaded properly before the next loop iteration
        time.sleep(2)

finally:
    # Keep the browser open after all files are uploaded
    input("All files processed. Press Enter to close the browser...")
    driver.quit()
