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
    html = requests.get(
        "https://www.bilbasen.dk/brugt/bil/opel/astra/13-cdti-95-enjoy-5d/6842078",
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


    print(display_values[0]) #årgang
    print(display_values[2]) #km
    print(display_values[3]) #drivemidel
    print(display_values[11]) #hestekraft
    print(props["listing"]["vehicle"]["make"] + ": " + props["listing"]["vehicle"]["model"]) #mærke
    print(props["listing"]["price"]["displayValue"]) #pris
    
    pris = props["listing"]["price"]["displayValue"]
    pris = pris.replace("kr","")
    pris = pris.replace(".","")
    km = display_values[2]
    km = km.replace("km","")
    km = km.replace(".","")
    mærke = props["listing"]["vehicle"]["make"] + ": " + props["listing"]["vehicle"]["model"]
    return [display_values[11], pris, km, display_values[0], display_values[3], mærke]

bil_info()

#file = open("data_på_bil", "a")
#link = open("link_til_bil.txt")
#antal_links = lines_in_fil("link_til_bil.txt")

#while n < antal_links:
 #   print(n)
  #  templist = []
   # templist.append(bil_info(link.readline()))
    #file.write(templist + "\n")
    #n += 1

#file.close()