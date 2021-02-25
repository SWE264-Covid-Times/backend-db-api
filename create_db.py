import sqlite3
from datetime import date

conn = sqlite3.connect("covidtimesdata.db")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS Users")
cur.execute("DROP TABLE IF EXISTS History")
cur.execute("CREATE TABLE Users(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE)")
cur.execute('INSERT INTO Users(name) VALUES(?)', ('adam',))
cur.execute("CREATE TABLE History(userid INTEGER NOT NULL, searchterm TEXT NOT NULL, fromdate DATE, todate DATE, casecount INTEGER, FOREIGN KEY(userid) REFERENCES Users(id))")
cur.execute('INSERT INTO History(userid, searchterm, fromdate, todate, casecount) VALUES(?,?,?,?,?)', (1,'united-states','2021-02-10','2021-02-16',100))

conn.commit()
cur.close()