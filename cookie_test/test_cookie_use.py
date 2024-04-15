from selenium import webdriver
import pickle
import time

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Load cookies from file
with open("cookies.pkl", "rb") as f:
    cookies = pickle.load(f)

# Navigate to the webpage where you want to reuse cookies
driver.get("https://web.whatsapp.com/")

# Modify the domain attribute of each cookie to match the current domain
current_domain = driver.current_url.split('/')[2]  # Extract current domain from the URL
for cookie in cookies:
    cookie['domain'] = current_domain
    driver.add_cookie(cookie)

# Refresh the page or navigate to another page to use the cookies
driver.get("https://web.whatsapp.com/")
time.sleep(60)

# Close the WebDriver
driver.quit()

