import sqlite3

con = sqlite3.connect('organizations.sqlite')
cur = con.cursor()

cur.execute('CREATE TABLE Counts(org TEXT, count INTEGER)')
fhandle = open('mbox.txt')
for line in fhandle:
    line = line.strip()
    if line.startswith('From:'):

cur.execute('SELECT COUNT(email) FROM Counts')