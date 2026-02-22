from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

# Set up the driver
driver = webdriver.Chrome()
driver.get("https://www.electronicsbazaar.com")

wait = WebDriverWait(driver, 10)

# Search for "laptops"
search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))
search_box.send_keys("laptops")
search_box.send_keys(Keys.RETURN)

time.sleep(3)
data = []

for page in range(1, 18):  # Number of Pages
    print(f"Processing Page {page}...")

    time.sleep(3)
    listings = driver.find_elements(By.XPATH, "//a[@class='product-item-link']")

    for i, listing in enumerate(listings):
        try:
            url = listing.get_attribute("href")
            driver.execute_script(f"window.open('{url}', '_blank');")
            time.sleep(0.1)
            driver.switch_to.window(driver.window_handles[1])
            print(f"Opened laptop {i + 1}")

            time.sleep(2)

            # Extract details with your correct XPaths
            try:
                brand = driver.find_element(By.XPATH, "//li[div[@class='col label attr-label' and text()='Brands']]/div[@class='col data attr-value']").text
            except:
                brand = "N/A"

            try:
                processor = driver.find_element(By.XPATH, "//li[div[@class='col label attr-label' and text()='Processor']]/div[@class='col data attr-value']").text
            except:
                processor = "N/A"

            try:
                ram = driver.find_element(By.XPATH, "//li[div[@class='col label attr-label' and text()='RAM']]/div[@class='col data attr-value']").text
            except:
                ram = "N/A"

            try:
                storage = driver.find_element(By.XPATH, "//li[div[text()='Hard Disk Drive (Storage)']]/div[@class='col data attr-value']").text
            except:
                storage = "N/A"

            try:
                screen_size = driver.find_element(By.XPATH, "//li[div[@class='col label attr-label' and text()='Screen Size']]/div[@class='col data attr-value']").text
            except:
                screen_size = "N/A"
                
            condition = "Refurbished"

            try:
                warranty = driver.find_element(By.XPATH, "//li[div[@class='col label attr-label' and text()='Warranty']]/div[@class='col data attr-value']").text
            except:
                warranty = "N/A"


            data.append({
                "Brand": brand,
                "Processor": processor,
                "RAM(GB)": ram,
                "Storage(GB)": storage,
                "Screen Size(inch)": screen_size,
                "Condition": condition,
                "Warranty": warranty,
            })

            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        except Exception as e:
            print(f"Error with listing {i + 1} on page {page}: {e}")
            continue

    try:
        next_button = wait.until(EC.presence_of_element_located((By.XPATH, "(//a[@class='action  next' and @title='Next'])[2]")))
        driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
        time.sleep(1)
        next_button.click()
    except:
        print("No more pages.")
        break

# Save to CSV
with open("raw_laptop_data.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["Brand", "Processor", "RAM(GB)", "Storage(GB)", "Screen Size(inch)", "Condition", "Warranty"])
    writer.writeheader()
    writer.writerows(data)

print("Data saved to raw_laptop_data.csv")
driver.quit()
