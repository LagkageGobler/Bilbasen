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
        id INTEGER PRIMARY KEY
        name TEXT
        emil TEXT UNIQUE
        password TEXT
    )
    """
    try:
        with connection:
            connection.execute(query)
    except Exception as e:
        print(e)
        raise