from selenium import webdriver
import pickle
import time

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Navigate to the webpage where you want to capture cookies
driver.get("https://web.whatsapp.com/")
time.sleep(120)

# Get and save the cookies
cookies = driver.get_cookies()
with open("cookies.pkl", "wb") as f:
    pickle.dump(cookies, f)

# Close the WebDriver
driver.quit()