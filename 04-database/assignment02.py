import sqlite3

con = sqlite3.connect('music.sqlite')
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks(title TEXT, plays INTEGER)')
cur.close()