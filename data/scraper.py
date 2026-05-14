from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Open Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Go to kids page
url = "https://solbiatosport.com/product-category/solbiato-kids/"
driver.get(url)

#Wait for page to load
time.sleep(5)

#Find all products
products = driver.find_elements(By.CLASS_NAME, "product")

print("Number of products found:", len(products))

#Loop through products
for product in products:
    try:
        name = product.find_element(By.CLASS_NAME, "woocommerce-loop-product_title").text
        price = product.find_element(By.CLASS_NAME, "price").text

        print(name, "-", price)
    except:
        continue

driver.quit()
