
f = open("data_på_bil.txt", "w")
f.write("")
f.close

n = 2
def fake_data():
    
    url = input("url: ")
    pris = input("pris: ")
    mærke = input("mærke: ")
    årgang = input("årgang: ")
    km = input("km: ")
    drivemidel = input("drivemidel: ")
    hestekraft = input("hestekraft: ")

    return [hestekraft, pris, km, årgang, drivemidel, mærke, url]

while n > 1:
    templist = fake_data()
    with open("data_på_bil.txt", "a") as f:
        f.write(str(templist) + "\n")