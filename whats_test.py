from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Navigate to the webpage containing the elements
driver.get("https://web.whatsapp.com/")

time.sleep(60)

# Find all elements containing the text "mensagens não lidas"
elements = driver.find_elements(By.XPATH, "//span[contains(@aria-label, 'mensagens não lidas') or contains(@aria-label, 'mensagen não lida')]")

# Store the matching elements in a list
matching_elements = []

# Iterate over the found elements and store them in the list
for element in elements:
    matching_elements.append(element)
    element.click()
    time.sleep(10)

# Print the number of matching elements found
print("Number of matching elements:", len(matching_elements))

# Close the WebDriver
driver.quit()
