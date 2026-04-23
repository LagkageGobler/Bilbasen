import time
import random
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Finder indekset for elementet der indeholder "hk" (hestekræfter)
def find_hk(lst):
    for i, v in enumerate(lst):
        if "hk" in v:
            return i

# Finder indekset for elementet der indeholder "km" (kilometer)
def find_km(lst):
    for i, v in enumerate(lst):
        if "km" in v:
            return i

# Funktion der henter information om en bil fra en given URL
def bil_info(url):
    # Opsætning af Chrome browser options
    options = Options()
    options.add_argument("--start-maximized")  # Starter browser i fuld skærm
    options.add_argument("--disable-blink-features=AutomationControlled")  # Skjuler automation
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    # Starter webdriver
    driver = webdriver.Chrome(options=options)

    # Fjerner webdriver flag så siden ikke opdager scraping
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    # Åbner URL
    driver.get(url)

    # Venter lidt (tilfældigt) for at undgå at ligne en bot
    time.sleep(random.uniform(1.5, 2.5))

    # Henter HTML fra siden og lukker browser
    html = driver.page_source
    driver.quit()

    # Parser HTML med BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    props = None

    # Finder script-tag der indeholder JSON data (_props)
    for script in soup.find_all("script"):
        text = script.get_text()
        if "var _props" in text:
            start = text.find("var _props = ") + len("var _props = ")
            end = text.rfind("};") + 1

            # Udtrækker JSON tekst og loader det
            json_text = text[start:end]
            props = json.loads(json_text)
            break

    # Hvis data ikke findes, print fejl
    if props is None:
        print("Could not find _props")
        return

    # Henter details listen i props
    data = props["listing"]["vehicle"]["details"]

    # Henter display_values
    display_values = [item["displayValue"] for item in data]
  

    # Finder hestekræfter
    hk_index = find_hk(display_values)
    hk = display_values[hk_index]
    hk = hk.split(" ")[0]  # Fjerner tekst efter tallet

    # Henter pris og renser teksten
    pris = props["listing"]["price"]["displayValue"]
    pris = pris.replace("kr","")
    pris = pris.replace(".","")

    # Finder kilometer og renser teksten
    km = display_values[find_km(display_values)]
    km = km.replace("km","")
    km = km.replace(".","")
    
    # Samler mærke og model
    mærke = props["listing"]["vehicle"]["make"] + ": " + props["listing"]["vehicle"]["model"]
    
    # Returnerer relevante data om bilen
    return [display_values[hk_index], km, pris, display_values[0], display_values[3], mærke, url]


# Åbner fil med links til biler
def setter_data_ind_på_data_txt():
    with open("link_til_bil_1.txt") as file:
        n = 0
        while n < 20:
            # Læser ét link ad gangen
            link = file.readline().strip()

            # Henter info om bilen
            templist = bil_info(link)

            # Gemmer data i fil
            with open("data.txt", "a") as data:
                try:
                    # Skriver data som kommasepareret linje
                    data.write(",".join(templist) + "\n")
                except Exception as e:
                    # Printer fejl hvis noget går galt
                    print(e)
            n += 1

setter_data_ind_på_data_txt()