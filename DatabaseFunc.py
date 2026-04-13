#imports
import sqlite3

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

#slet datbase og indstætte de nye biler
def Update(db_name):
    #sletter databasen
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("DROP TABLE biler")
    conn.commit()
    conn.close()
    DBtable(db_name)
    #indsætter de nye biler
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    for biler in 

    ADDbiler()

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
    prisPrKM = pris / km
    cur.execute("insert into biler values (?, ?, ?, ?, ?, ?)",(prisPrKM, modelår, drivemidel, bilnavn, url, Hestekrafter))
    conn.commit()
    conn.close()
