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
def DBtable(connection):
    query = """
    CREATE TABLE IF NOT EXISTS users(
        name TEXT PRIMARY KEY,
        emil TEXT UNIQUE,
        password TEXT,
    )
    CREATE TABLE IF NOT EXISTS biler(
        id INTEGER PRIMARYKEY,
        prisPrKm INTEGER,
        modelÅr INTEGER,
        drivemidel TEXT,
        BilNavn TEXT,
        Url TEXT,
    )
    """
    try:
        with connection:
            connection.execute(query)
    except Exception as e:
        print(e)
        raise

def Update(db_name):
    sql = "DELETE FROM biler WHERE id = ?"
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    for i in sql.count(id):
        cur.execute(sql, i)
        i += 1
    conn.commit()
    conn.close()

def ADDuser(db_name, UserName, Email, Password):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("insert into users values (?, ?, ?)", (UserName, Email, Password))
    conn.commit()
    conn.close()
