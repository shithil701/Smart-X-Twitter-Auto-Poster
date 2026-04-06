from selenium import webdriver
import pickle
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.x.com/")
time.sleep(5)

try:
    with open("xcookie.pkl", "rb") as file:
        cookies = pickle.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)
            time.sleep(2)
    print("Cookie add successfully")
    driver.refresh()
except:
    print("Cookie not add!")



