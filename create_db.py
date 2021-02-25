import sqlite3

conn = sqlite3.connect("covidtimesdata.db")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS Users")
cur.execute("DROP TABLE IF EXISTS History")
cur.execute("CREATE TABLE Users(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE)")
cur.execute('INSERT INTO Users(name) VALUES(?)', ('adam',))
cur.execute("CREATE TABLE History(userid INTEGER NOT NULL, searchterm TEXT NOT NULL, FOREIGN KEY(userid) REFERENCES Users(id))")
cur.execute('INSERT INTO History(userid, searchterm) VALUES(?,?)', (1,'united-states'))

conn.commit()
cur.close()