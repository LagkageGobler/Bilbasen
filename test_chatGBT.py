import requests
from bs4 import BeautifulSoup
import re

articlelist = []
templist = []
x = 1

link_bil = open("link_til_bil.txt", "w")
link_bil.write("")
link_bil.close()


def article_list(templist, page):
    url = f"https://www.bilbasen.dk/brugt/bil?includeengroscvr=true&includeleasing=false&page={page}"
    print(url)
    headers = {
    "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    # find all <article> where class starts with "Listing_listing__"
    articles = soup.find_all(
    "article"
    )

    for article in articles:
        link = article.find("a", href=True)
    
        if link:
            href = link["href"]

            if href.startswith("/"):
                href = "https://www.bilbasen.dk" + href

            print(href)
            templist.append(href)
    return templist

for i in range(1, 100):
    templist = []
    print(i)
    templist = article_list(templist,i)
    link_bil = open("link_til_bil.txt", "a")
    for link in templist:
        link_bil.write(link + "\n")