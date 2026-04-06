import os
import time
import pickle
import requests
import pandas as pd
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
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-blink-features")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=chrome_options)



driver.get("https://www.x.com/")
time.sleep(5)


with open("xcookie.pkl", "rb") as f:
    cookies = pickle.load(f)

for cookie in cookies:
    cookie.pop('sameSite', None)
    cookie.pop('expiry', None)
    try:
        driver.add_cookie(cookie)
    except Exception as e:
        print("Error adding cookie:", cookie, "\n", e)

driver.refresh()
time.sleep(5)

def download_image(url, save_folder='temp_images'):
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    
    response = requests.get(url, stream=True)
    response.raise_for_status()
    

    parsed = urlparse(url)
    filename = os.path.basename(parsed.path) or 'twitter_image.jpg'
    filepath = os.path.join(save_folder, filename)
    
    with open(filepath, 'wb') as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)
    
    return filepath


df = pd.read_csv('demo.csv')
name = df['Title'].tolist()
price = df['Price'].tolist()
image = df['Image URL'].tolist()
link = df['Affiliate URL'].tolist()

for x in range(len(name)):
    
    image_url = image[x]
    local_path = download_image(image_url)
    current_path = os.getcwd()
    the_path = current_path + "\\" + local_path
    final_path = the_path.replace("\\", "\\\\")

    s_name = name[x]
    s_price = price[x]
    s_link = link[x]

    TWEET_TEXT = s_name + "\n" + "Price: " + s_price + "\n" + s_link

    try:
        time.sleep(5)
        tweet_textarea = driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')
        tweet_textarea.send_keys(TWEET_TEXT)
        print("Enter tweet text")
        

        image_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
        image_input.send_keys(final_path)
        print("Upload image")
        
        time.sleep(3)
        
        tweet_button = driver.find_element(By.XPATH, "//*[@data-testid='tweetButtonInline']")
        tweet_button.click()
        print("Post")

        os.remove(local_path)
        time.sleep(5)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
    finally:
        # Close the browser
        #driver.quit()
        print("Done " + str(x) + "\n")
        driver.refresh()
        time.sleep(10)
