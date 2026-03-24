from bs4 import BeautifulSoup
import requests
import json

html = requests.get(
    "https://www.bilbasen.dk/brugt/bil/tesla/model-y/long-range-awd-5d/6843759",
    headers={"User-Agent": "Mozilla/5.0"}
).text

soup = BeautifulSoup(html, "html.parser")

props = None

for script in soup.find_all("script"):
    if script.string and "var _props" in script.string:
        text = script.string
        
        start = text.find("var _props = ") + len("var _props = ")
        end = text.rfind("};") + 1  # include closing }
        
        json_text = text[start:end]
        props = json.loads(json_text)
        break



data = props["listing"]["vehicle"]["details"]  # your list

display_values = [item["displayValue"] for item in data]

#print(display_values)


print(display_values[0])
print(display_values[2])
print(display_values[11])
print(props["listing"]["vehicle"]["make"])
print(props["listing"]["vehicle"]["model"] + ": " + props["listing"]["vehicle"]["variant"])
print(props["listing"]["vehicle"]["ratings"]["average"])
print(props["listing"]["price"]["displayValue"])
