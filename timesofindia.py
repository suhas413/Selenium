from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome()

print("Opening Times of India website...")
driver.get("https://timesofindia.com/")
time.sleep(3)

try:
    print("\nFetching top headlines")
    time.sleep(2)  # Wait for elements to load
    headlines = driver.find_elements(By.CSS_SELECTOR, ".w_tle")[:5]

    print("\nTop 5 Headlines:")
    for i, headline in enumerate(headlines, 1):
     print(f"{i}. {headline.text.strip()}")

    print("\nNavigating to Business section")
    business_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Business')]")
    business_link.click()
    time.sleep(3)
    print("Now on Business section")

    print("\nSearching for technology")
    search_button = driver.find_element(By.CSS_SELECTOR, ".search")
    search_button.click()
    time.sleep(2)

    search_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search']")
    search_input.clear()
    search_input.send_keys("technology")
    search_input.submit()
    time.sleep(3)
    print("Search completed")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("\nClosing browser...")
    driver.quit()