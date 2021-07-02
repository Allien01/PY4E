import sqlite3

con = sqlite3.connect('organizations.sqlite')
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts(org TEXT, count INTEGER)')
fhandle = open('mbox.txt')
dic = {}
for line in fhandle:
    if  not line.startswith('From:'): continue
    line = line.strip()
    pieces = line.split()
    address = pieces[1]
    pos = address.find('@') + 1
    key = address[pos: ]
    dic[key] = dic.get(key, 0) + 1
for key, value in dic.items():
    print('Key: {} and Value: {}'.format(key, value))
    cur.execute(' INSERT INTO Counts(org, count) VALUES (?, ?)', (key, value))

con.commit()
cur.close()


#cur.execute('SELECT COUNT(email) FROM Counts')