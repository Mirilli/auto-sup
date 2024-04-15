import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import keyboard

dir_path = os.getcwd()
profile = os.path.join(dir_path, "profile", "wpp")
options = webdriver.ChromeOptions()
options.add_argument(
    r"user-data-dir={}".format(profile))

driver = webdriver.Chrome(options=options)

driver.get("https://web.whatsapp.com")

def close_browser():
    driver.quit()

while True:
    elements = driver.find_elements(By.XPATH, "//span[contains(@aria-label, 'mensagens não lidas') or contains(@aria-label, 'mensagen não lida')]")

    # Store the matching elements in a list
    matching_elements = []

    # Iterate over the found elements and store them in the list
    for element in elements:
        matching_elements.append(element)
        

    # Print the number of matching elements found
    print("Number of matching elements:", len(matching_elements))

    time.sleep(10)

    
## Register a hotkey (e.g., 'q') to close the browser
#keyboard.add_hotkey('q', close_browser)
## Keep the script running until the hotkey is pressed
#keyboard.wait('esc')
## Unregister the hotkey
#keyboard.unhook_all_hotkeys()

    
    


