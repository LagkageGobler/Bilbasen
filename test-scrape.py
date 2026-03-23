import requests
from bs4 import BeautifulSoup

url = "https://www.bilbasen.dk/brugt/bil?includeengroscvr=true&includeleasing=false"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

selector = "#__next > div.nmp-ads-layout__wrapper > div.nmp-ads-layout__page > div.nmp-ads-layout__content > div > main > div.Pagination_pagination__GywrN > div > span:nth-child(2)"

element = soup.select_one(selector)

print(element.text)
