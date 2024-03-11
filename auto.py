import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class ZoomAutomationApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Zoom Automation App")

        self.website_url_label = QLabel("Website URL:")
        self.website_url_input = QLineEdit()
        self.email_address_label = QLabel("Email Address:")
        self.email_address_input = QLineEdit()
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.join_button = QPushButton("Join Zoom Meeting")

        layout = QVBoxLayout()
        layout.addWidget(self.website_url_label)
        layout.addWidget(self.website_url_input)
        layout.addWidget(self.email_address_label)
        layout.addWidget(self.email_address_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.join_button)

        self.setLayout(layout)

        self.join_button.clicked.connect(self.join_zoom_meeting)

    def join_zoom_meeting(self):
        website_url = self.website_url_input.text()
        email_address = self.email_address_input.text()
        password = self.password_input.text()

 # Initialize the Chrome options
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")

# Provide the path to ChromeDriver executable in the executable_path option
        chrome_options.binary_location = r'C:\AUTO\chromedriver\chrome-win64\chrome.exe'
# Initialize the web driver (Chrome)
        driver = webdriver.Chrome(options=chrome_options)

# https://plpacademy.powerlearnproject.org/
# iddy2525@icloud.com
# Wrld2525_

        # Open the website
        driver.get(website_url)

        # Wait for the page to load
        time.sleep(2)

        # Enter login credentials
        username_input = driver.find_element_by_id(By.ID, 'iddy2525@icloud.com')  # Replace with the actual ID of the username input field
        password_input = driver.find_element_by_id('Wrld2525_')  # Replace with the actual ID of the password input field
        username_input.send_keys(email_address)
        password_input.send_keys(password)

        # Submit the login form
        sign_in_button = driver.find_element_by_id('Sign In')  # Replace with the actual ID of the login button
        sign_in_button.click()

        # Wait for the user to be logged in
        time.sleep(2)

        # Navigate to the specific button and click it
        button = driver.find_element_by_id('Sign_In')  # Replace with the actual ID of the specific button
        button.click()

        # Wait for the page to load after clicking the button
        time.sleep(2)

        # Open the Zoom meeting link
        zoom_link = driver.find_element_by_id('https://powerlearnproject-org.zoom.us/j/81781379156?pwd=ppuep0gi7jSkn5Ce8TbKh6t4SzPchg.oAof0YC0BiN7LyFQ')  # Replace with the actual ID of the Zoom meeting link
        zoom_link.click()

        # Wait for the Zoom meeting to open
        time.sleep(5)

        # Close the web driver
        driver.quit()

        # Clear the input fields
        self.website_url_input.clear()
        self.username_input.clear()
        self.password_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ZoomAutomationApp()
    window.show()
    sys.exit(app.exec_())