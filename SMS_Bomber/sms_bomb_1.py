# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import threading

# def setup_browser_instance(phone_number, count_number, instance_id):
#     chrome_options = Options()
    
#     # Path to ChromeDriver
#     driver_path = "D:\\chromedriver-win64\\chromedriver.exe"  
#     service = Service(driver_path)
    
#     # Use a unique profile for each instance to avoid conflicts
#     chrome_options.add_argument(f"--user-data-dir=D:\\chrome_profiles\\profile_{instance_id}")
    
#     driver = webdriver.Chrome(service=service, options=chrome_options)

#     try:
#         url = "https://mytoolstown.com/smsbomber/"  # Change this to your target URL
#         driver.get(url)
        
#         # Increase the waiting time for page elements
#         wait = WebDriverWait(driver, 60)

#         # Handle ads or overlays (if any)
#         def handle_ads(driver, wait, instance_id):
#             try:
#                 overlay_elements = [
#                     (By.ID, 'popup-ad-id'),  # Replace with actual ID if known
#                     (By.CLASS_NAME, 'overlay-class'),  # Replace with actual class if known
#                     (By.XPATH, "//div[contains(@class, 'overlay-class')]")  # Replace with actual XPath if known
#                 ]
                
#                 for by, value in overlay_elements:
#                     try:
#                         element = wait.until(EC.element_to_be_clickable((by, value)))
#                         driver.execute_script("arguments[0].click();", element)
#                         print(f"[Instance {instance_id}] Ad overlay clicked.")
#                     except Exception as e:
#                         print(f"[Instance {instance_id}] No ad element found or could not click: {e}")
                
#                 # Remove ad iframes
#                 ad_iframes = driver.find_elements(By.CSS_SELECTOR, 'iframe[id^="google_ads_iframe_"]')
#                 for ad_iframe in ad_iframes:
#                     driver.execute_script("arguments[0].remove();", ad_iframe)
#                     print(f"[Instance {instance_id}] Ad iframe removed.")

#                 # Remove any elements by class or ID if known
#                 ad_elements = driver.find_elements(By.CSS_SELECTOR, '.ad-class, #ad-id')
#                 for ad_element in ad_elements:
#                     driver.execute_script("arguments[0].remove();", ad_element)
#                     print(f"[Instance {instance_id}] Ad element removed.")
            
#             except Exception as e:
#                 print(f"[Instance {instance_id}] Error while handling ads: {e}")

#         # Locate the phone number input box, count input box, and start button
#         phone_input = wait.until(EC.presence_of_element_located((By.ID, "mobno")))
#         count_input = wait.until(EC.presence_of_element_located((By.ID, "count")))

#         # Wait for the start button to be clickable and ensure no overlay or ad is blocking it
#         start_button = wait.until(EC.element_to_be_clickable((By.ID, "startsms")))

#         # Scroll into view to ensure the element is clickable
#         driver.execute_script("arguments[0].scrollIntoView(true);", start_button)

#         # Retry mechanism for clicking the start button
#         def safe_click(element, driver, instance_id, retries=5):
#             for attempt in range(retries):
#                 try:
#                     handle_ads(driver, wait, instance_id)
#                     driver.execute_script("arguments[0].scrollIntoView(true);", element)
#                     wait.until(EC.element_to_be_clickable((By.ID, "startsms")))
                    
#                     if element.is_displayed() and element.is_enabled():
#                         try:
#                             element.click()  # Attempt regular click first
#                         except:
#                             driver.execute_script("arguments[0].click();", element)  # Fallback to JavaScript click
                        
#                         print(f"[Instance {instance_id}] Start button clicked.")
#                         return
#                 except Exception as e:
#                     print(f"[Instance {instance_id}] Click attempt {attempt+1} failed: {e}")
#                     time.sleep(3)  # Increased wait time between retries
                    
#                     if attempt == retries - 1:
#                         screenshot_path = f"screenshot_instance_{instance_id}.png"
#                         driver.save_screenshot(screenshot_path)
#                         print(f"[Instance {instance_id}] Screenshot taken: {screenshot_path}")
#             print(f"[Instance {instance_id}] Failed to click element after multiple attempts.")
        
#         # Fill the phone number, count number, and click start
#         phone_input.send_keys(phone_number)
#         count_input.send_keys(count_number)
#         safe_click(start_button, driver, instance_id)
        
#         # Keep the browser open for 10 minutes
#         print(f"[Instance {instance_id}] Browser will stay open for 10 minutes...")
#         time.sleep(600)  # 10 minutes in seconds (600 seconds)
#     finally:
#         driver.quit()

# # Phone number and count number to fill in
# phone_number = "0000000000"
# count_number = '199'
# num_instances = 5  # Number of instances to open

# # Create and start threads for each browser instance
# threads = []
# for i in range(num_instances):
#     thread = threading.Thread(target=setup_browser_instance, args=(phone_number, count_number, i+1))
#     thread.start()
#     threads.append(thread)
    
#     time.sleep(5)  # Stagger start times by 5 seconds to reduce resource contention

# # Wait for all threads to complete
# for thread in threads:
#     thread.join()

# print("All browser instances completed.")




from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import threading

def setup_browser_instance(phone_number, count_number, instance_id, headless=False):
    chrome_options = Options()
    
    # Path to ChromeDriver
    driver_path = "D:\\chromedriver-win64\\chromedriver.exe"
    service = Service(driver_path)
    
    # Use a unique profile for each instance to avoid conflicts
    chrome_options.add_argument(f"--user-data-dir=D:\\chrome_profiles\\profile_{instance_id}")
    
    # Run in headless mode if specified
    if headless:
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920x1080")
    
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        url = "https://mytoolstown.com/smsbomber/"
        driver.get(url)
        
        wait = WebDriverWait(driver, 30)

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

        phone_input = wait.until(EC.presence_of_element_located((By.ID, "mobno")))
        count_input = wait.until(EC.presence_of_element_located((By.ID, "count")))
        start_button = wait.until(EC.element_to_be_clickable((By.ID, "startsms")))

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
                        screenshot_path = f"screenshot_instance_{instance_id}.png"
                        driver.save_screenshot(screenshot_path)
                        print(f"[Instance {instance_id}] Screenshot taken: {screenshot_path}")
            print(f"[Instance {instance_id}] Failed to click element after multiple attempts.")

        phone_input.send_keys(phone_number)
        count_input.send_keys(count_number)
        safe_click(start_button, driver, instance_id)
        
        print(f"[Instance {instance_id}] Browser will stay open for 10 minutes...")
        time.sleep(600)
    finally:
        driver.quit()

phone_number = "0000000000"
count_number = '199'
num_instances = 5

threads = []
for i in range(num_instances):
    headless = i > 0  # Run the first instance in normal mode and the rest in headless mode
    thread = threading.Thread(target=setup_browser_instance, args=(phone_number, count_number, i+1, headless))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("All browser instances completed.")
