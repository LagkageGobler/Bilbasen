from bs4 import BeautifulSoup
import requests
import json

lines_in_link = 0
n = 1
def slet_bil_info_textfil():
    data_på_bil = open("data_på_bil.txt", "w")
    data_på_bil.write("")
    data_på_bil.close()

def lines_in_fil(filename):
    with open(filename) as file:
        lines = file.readlines()
        total_lines = len(lines)
        return total_lines

def bil_info():
    slet_bil_info_textfil()
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0.8",
    "Connection": "keep-alive"
}
    response = requests.get(
    "https://www.bilbasen.dk/brugt/bil/opel/astra/13-cdti-95-enjoy-5d/6842078",
    headers=headers
)

    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    props = None
    print(len(html))
    print(response.status_code)
    print(len(response.text))
    print("script" in response.text)
bil_info()