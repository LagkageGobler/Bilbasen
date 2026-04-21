import time
import random
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def find_hk(lst):
        for i, v in enumerate(lst):
            if "hk" in v:
                return i

def bil_info(url):
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    driver.get(url)
    time.sleep(random.uniform(1.5, 2.5))

    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, "html.parser")

    props = None

    for script in soup.find_all("script"):
        text = script.get_text()
        if "var _props" in text:
            start = text.find("var _props = ") + len("var _props = ")
            end = text.rfind("};") + 1

            json_text = text[start:end]
            props = json.loads(json_text)
            break

    if props is None:
        print("Could not find _props")
        return

    data = props["listing"]["vehicle"]["details"]
    display_values = [item["displayValue"] for item in data]
    print(display_values)
  

    hk = find_hk(display_values)
    pris = props["listing"]["price"]["displayValue"]
    pris = pris.replace("kr","")
    pris = pris.replace(".","")
    km = display_values[2]
    km = km.replace("km","")
    km = km.replace(".","")
    mærke = props["listing"]["vehicle"]["make"] + ": " + props["listing"]["vehicle"]["model"]
    
    return [display_values[hk], km, pris, display_values[0], display_values[3], mærke, url]




with open("link_til_bil_1.txt") as file:
    n = 0
    while n < 20:
        link = file.readline().strip()
        templist = bil_info(link)
        with open("data.txt", "a") as data:
            try:
                data.write(",".join(templist) + "\n")
            except Exception as e:
                print(e)
        n += 1