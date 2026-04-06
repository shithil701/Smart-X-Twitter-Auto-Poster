import undetected_chromedriver as uc
import pickle
import time

# Start undetected Chrome
options = uc.ChromeOptions()
options.add_argument("--no-first-run --no-service-autorun --password-store=basic")
driver = uc.Chrome(options=options)

# Visit the target site
driver.get("https://www.x.com/")

# Wait for manual login or fully loaded page
time.sleep(30)  # You can replace this with proper waits (e.g., WebDriverWait)

thename = input("Enter a name to save: ")

finalname = thename + ".pkl"

# Save cookies to file
with open(finalname, "wb") as file:
    pickle.dump(driver.get_cookies(), file)

driver.quit()
