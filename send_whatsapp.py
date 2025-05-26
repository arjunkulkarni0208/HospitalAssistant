from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up Firefox browser
driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com")

# Wait for QR code scan
input("Scan QR code and press Enter...")

# Search for the contact
contact = "+919607379080"  # or phone number with country code
message = "Hello from Hospital Assistant!"

search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
search_box.click()
search_box.send_keys(contact)
time.sleep(2)
search_box.send_keys(Keys.ENTER)

# Wait for chat to open
time.sleep(2)

# Type message
msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
msg_box.send_keys(message)
msg_box.send_keys(Keys.ENTER)

print("✅ Message sent.")

