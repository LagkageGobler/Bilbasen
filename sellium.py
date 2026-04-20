from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--start-maximized")

# 👇 important anti-detection flags
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=options)

# 👇 remove "webdriver" flag
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.get("https://www.bilbasen.dk/brugt/bil/opel/astra/13-cdti-95-enjoy-5d/6842078")

import time
time.sleep(5)  # give JS time to load

html = driver.page_source

print(len(html))
print("var _props" in html)