import requests
from bs4 import BeautifulSoup

def bil_data():
    url = "https://www.bilbasen.dk/brugt/bil/tesla/model-y/long-range-awd-5d/6843759"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(response.text, "html.parser")

    pris_path = "#root > div.nmp-ads-layout__wrapper > div.nmp-ads-layout__page > div.nmp-ads-layout__content > div:nth-child(2) > article > main > div.bas-MuiVipPageComponent-headerAndPrice > div.bas-MuiCarPriceComponent-container > div > div > span"
    pris_path = soup.select_one(pris_path)
    pris = pris_path.text

    årgang_path1 = "#root > div.nmp-ads-layout__wrapper > div.nmp-ads-layout__page > div.nmp-ads-layout__content > div:nth-child(2) > article > main > div:nth-child(8) > div"
    årgang_path2 = soup.select_one(årgang_path1)
    
    print(årgang_path2)
    
    #årgang = årgang_path.text

    pris = pris.replace("kr","")
    pris = pris.replace(".","")
    print("pris: " + pris)
    #print("årgang: " + årgang)
bil_data()
#root > div.nmp-ads-layout__wrapper > div.nmp-ads-layout__page > div.nmp-ads-layout__content > div:nth-child(2) > article > main > div:nth-child(8) > div > table > tbody > tr:nth-child(3) > td
#root > div.nmp-ads-layout__wrapper > div.nmp-ads-layout__page > div.nmp-ads-layout__content > div:nth-child(2) > article > main > div:nth-child(8) > div > table > tbody > tr:nth-child(1) > td