import os
import time
import pickle
import requests
from selenium import webdriver
from urllib.parse import urlparse
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)



driver.get("https://www.x.com/")
time.sleep(5)

# Load cookies
with open("xcookie.pkl", "rb") as f:
    cookies = pickle.load(f)

for cookie in cookies:
    cookie.pop('sameSite', None)  # Optional: avoid SameSite errors
    cookie.pop('expiry', None)    # Optional: avoid float/int mismatch
    try:
        driver.add_cookie(cookie)
    except Exception as e:
        print("Error adding cookie:", cookie, "\n", e)

# Refresh to apply cookies
driver.refresh()
time.sleep(15)

def download_image(url, save_folder='temp_images'):
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    
    response = requests.get(url, stream=True)
    response.raise_for_status()
    
    # Extract filename from URL
    parsed = urlparse(url)
    filename = os.path.basename(parsed.path) or 'twitter_image.jpg'
    filepath = os.path.join(save_folder, filename)
    
    with open(filepath, 'wb') as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)
    
    return filepath


image_url = "https://m.media-amazon.com/images/I/81UQDoHG7pL._AC_SY355_.jpg"
local_path = download_image(image_url)
current_path = os.getcwd()
the_path = current_path + "\\" + local_path
final_path = the_path.replace("\\", "\\\\")

name = "SAMSUNG Galaxy Watch Ultra 47mm LTE AI Smartwatch w/Energy Score, Wellness Tips, Heart Rate Tracking, Sleep Monitor, Fitness Tracker, GPS, 2024,Titanium Gray [US Version, 1Yr Manufacturer Warranty]"
price = "$395.02"
link = "https://www.amazon.com/dp/B0D1YL96ND"
TWEET_TEXT = name + "\n" + "Price: " + price + "\n" + link


try:
    time.sleep(3)
    # Enter tweet text
    tweet_textarea = driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')
    tweet_textarea.send_keys(TWEET_TEXT)
    print("Enter tweet text")
    
    # Upload image
    image_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
    image_input.send_keys(final_path)
    print("Upload image")
    
    time.sleep(3)
    
    tweet_button = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')
    tweet_button.click()
    print("Click")

    os.remove(local_path)
    
except Exception as e:
    print(f"An error occurred: {str(e)}")
    
finally:
    # Close the browser
    #driver.quit()
    print("Done")
