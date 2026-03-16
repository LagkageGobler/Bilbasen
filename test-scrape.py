from bs4 import BeautifulSoup
import requests

url = "https://www.bilbasen.dk/brugt/bil?includeengroscvr=true&includeleasing=false&page=2"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html")
print(soup.find("article"))