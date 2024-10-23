import subprocess
import sys

def install_packages():
    # Ensure the required packages are installed using pip
    packages = ["PyPDF2", "selenium", "webdriver-manager"]

    for package in packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except subprocess.CalledProcessError:
            print(f"Failed to install {package}. Please install it manually.")
            sys.exit(1)

if __name__ == "__main__":
    # Upgrade pip first
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    # Install all required packages
    install_packages()
    print("All dependencies have been installed successfully.")
