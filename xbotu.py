import undetected_chromedriver as uc
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = uc.Chrome()

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
time.sleep(10)

IMAGE_PATH = "C:\\Users\\Ashik\\Desktop\\Shithil\\newbots\\x_bot\\temp_images\81UQDoHG7pL._AC_SY355_.jpg"
TWEET_TEXT = "SAMSUNG Galaxy Watch Ultra 47mm LTE AI Smartwatch w/Energy Score, Wellness Tips, Heart Rate Tracking, Sleep Monitor, Fitness Tracker, GPS, 2024,Titanium Gray [US Version, 1Yr Manufacturer Warranty]"


try:
    time.sleep(7)
    # Enter tweet text
    tweet_textarea = driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')
    tweet_textarea.send_keys(TWEET_TEXT)
    print("Enter tweet text")
    
    # Upload image
    image_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
    image_input.send_keys(IMAGE_PATH)
    print("Upload image")
    
    time.sleep(7)
    
    tweet_button = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')
    tweet_button.click()
    print("Click")

    
except Exception as e:
    print(f"An error occurred: {str(e)}")
    
finally:
    # Close the browser
    #driver.quit()
    print("Done")

