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
        id INTEGER PRIMARY KEY,
        name TEXT,
        emil TEXT UNIQUE,
        password TEXT,
    )
    CREATE TABLE IF NOT EXISTS biler(
        id INTEGER PRIMARYKEY,
        km INTEGER,
        modelÅr INTEGER,
        pris INTEGER,
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