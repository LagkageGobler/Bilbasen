#imports
import sqlite3


#Script wide variables
db_name = "bilgovrum.db"
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
        cur.execute("create table if not exists biler(id, prisPrKm, modelÅr, drivemidel, BilNavn, Url)")
    except Exception as e:
        print(e)
        raise
    conn.commit()
    conn.close()

#slet datbase
def Update(db_name):
    pass

#add users to database
def ADDuser(db_name, UserName, Email, Password):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("insert into users values (?, ?, ?)", (UserName, Email, Password))
    conn.commit()
    conn.close()

#add biler to database
def ADDbiler():
    pass

#main
def main():
    StartDatabase(db_name)
    DBtable(db_name)
main()