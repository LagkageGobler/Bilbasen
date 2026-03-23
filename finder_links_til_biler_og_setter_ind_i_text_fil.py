import requests
from bs4 import BeautifulSoup
import re

#lister som bruges senere
articlelist = []
templist = []

#åbner en tom fil eller sleter hvad der er i filen
link_bil = open("link_til_bil.txt", "w")
link_bil.write("")
link_bil.close()

def lide_antal():
    url = "https://www.bilbasen.dk/brugt/bil?includeengroscvr=true&includeleasing=false"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    selector = "#__next > div.nmp-ads-layout__wrapper > div.nmp-ads-layout__page > div.nmp-ads-layout__content > div > main > div.Pagination_pagination__GywrN > div > span:nth-child(2)"

    element = soup.select_one(selector)

    result = element.text
    result = result.replace(".","")
    return int(result)

    

#finder alle biler inde på en side og setter dem ind i en array
def article_list(templist, page):
    url = f"https://www.bilbasen.dk/brugt/bil?includeengroscvr=true&includeleasing=false&page={page}"
    headers = {
    "User-Agent": "Mozilla/5.0"
    }

    #find all <article> where class starts with "Listing_listing__"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("article")

    #går igennem alle artikler på siden og setter dem ind på en liste kalt templist
    for article in articles:
        link = article.find("a", href=True)
    
        if link:
            href = link["href"]

            if href.startswith("/"):
                href = "https://www.bilbasen.dk" + href
            templist.append(href)
    return templist

#loop som finder alle links på alle webpages og setter dem ind på en ext fill

for i in range(1, lide_antal()):
    templist = []
    print(i)
    templist = article_list(templist,i)
    link_bil = open("link_til_bil.txt", "a")
    for link in templist:
        link_bil.write(link + "\n")