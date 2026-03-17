import requests
from bs4 import BeautifulSoup
import re

articlelist = []

templist = []




def article_list(templist, page):
    url = f"https://www.bilbasen.dk/brugt/bil?includeengroscvr=true&includeleasing=false&page={page}"

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

for x in range(100):
  print(x)
  templist = article_list(templist,x)
  articlelist.extend(templist)

print(articlelist)