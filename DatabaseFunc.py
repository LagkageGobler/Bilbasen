#imports
import sqlite3
from bilbasen_scraper import setter_data_ind_på_data_txt
#variabler
db_name = "BilGoVrum.db"
#bruges i while loop 
def lines_in_fil(filename):
    with open(filename) as file:
        lines = file.readlines()
        total_lines = len(lines)
        return total_lines
    
# setup database
def StartDatabase(db_name):
    try:
        return sqlite3.connect(db_name)
    except Exception as e:
        print(e)
        raise

# lav table
def DBtable(db_name):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    try:
        cur.execute("create table if not exists users(name, emil, password)")
        cur.execute("create table if not exists biler(prisPrKm, modelÅr, drivemidel, BilNavn, Url, hestekrafter)")
    except Exception as e:
        print(e)
        raise
    conn.commit()
    conn.close()

#slet database og indstætte de nye biler
def Update(db_name):
    #bruges i while loop som place holder
    n = 0
    #sletter databasen
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("DROP TABLE biler")
    conn.commit()
    conn.close()
    DBtable(db_name)
    #sletter data på text fil
    with open("data.txt","w") as fil:
        fil.write("")
    setter_data_ind_på_data_txt()
    #indsætter de nye biler
    Data_til_bil = open("data_på_bil.txt")
    #while loop kører igennem alle linjer i filen data_på_bil og ligger dem ind i databasen 
    while lines_in_fil("data_på_bil.txt") > n:
        tempstring = Data_til_bil.readline()
        templist = tempstring.split(",")
        print(templist)
        ADDbiler(db_name, templist[0], templist[1], templist[2], templist[3], templist[4], templist[5], templist[6])
        print(templist)
        n += 1
    Data_til_bil.close()

#add users to database
def ADDuser(db_name, UserName, Email, Password):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("insert into users values (?, ?, ?)", (UserName, Email, Password))
    conn.commit()
    conn.close()

#add biler to database
def ADDbiler(db_name, Hestekrafter, pris, km, modelår, drivemidel, bilnavn, url):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    #striper stringsne så de kan konverteres til int
    prisPrKM = int(pris.strip()) / int(km.strip())
    cur.execute("INSERT INTO biler VALUES (?, ?, ?, ?, ?, ?)",(prisPrKM, modelår, drivemidel, bilnavn, url, Hestekrafter))
    conn.commit()
    conn.close()