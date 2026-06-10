from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = "https://owasp.org/Top10/2025/"

try:
    driver.get(url)
    time.sleep(5)       
    
    elements = driver.find_elements(By.XPATH, "//a[contains(text(), 'A0') or contains(text(), 'A10')]")
    results = []
    for element in elements:
        title = element.text
        link = element.get_attribute("href")
        
        results.append({
            "Vulnerability": title,
            "Link": link
        })

except Exception as e:
    print("couldn't get the web page")
    print(f"Exception: {type(e).__name__} {e}")
finally:
    driver.quit()

print(results)
df = pd.DataFrame(results)
df.to_csv("owasp_top_10.csv", index=False)
