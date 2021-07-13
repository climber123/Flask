import sqlite3

def Execute(name, query, i = 0):
    connection = sqlite3.connect(name)
    cur = connection.cursor()
    try:
        rows = cur.execute(query).fetchall()
        connection.commit()
    except:
        cur.execute(query)

    return (rows)

def ShowInfo(name):
    names = []
    connection = sqlite3.connect(name)
    db_names = connection.execute("SELECT name FROM sqlite_master WHERE type='table'")
    all_db_names = [description[0] for description in db_names]
    for i in all_db_names:
        db = (connection.execute("PRAGMA table_info(" + (i) + ")").fetchall())
        names.append([description[1] for description in db])
    return [all_db_names,names]