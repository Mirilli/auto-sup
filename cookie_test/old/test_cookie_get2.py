import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
driver = webdriver.Chrome('/usr/bin/chromedriver', options=chrome_options)
chrome_options.add_argument("user-data-dir=chrome-data")
driver.get('https://web.whatsapp.com/')
time.sleep(120)  # Time to enter credentials
driver.quit()