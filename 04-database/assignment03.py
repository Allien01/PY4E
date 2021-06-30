import sqlite3
con = sqlite3.connect('music.sqlite')
cur = con.cursor()

cur.execute('INSERT INTO Tracks(title, plays) VALUES (?,?)', ('Beggin', 20))

cur.execute('INSERT INTO Tracks(title, plays) VALUES (?, ?)', ('Spinning Over You', 50))

cur.execute('INSERT INTO Tracks(title, plays) VALUES (?, ?)', ('Adore You', 10))

cur.execute('INSERT INTO Tracks(title, plays) VALUES (?, ?)', ('Freedom 90', 39))

cur.execute('INSERT INTO Tracks(title, plays) VALUES (?, ?)', ('Baile de Favela', 13))

cur.execute('INSERT INTO Tracks(title, plays) VALUES (?, ?)', ('Yucky Blucky Fruitcake', 3))

cur.execute('INSERT INTO Tracks(title, plays) VALUES (?, ?)', ('Arcade', 27) )

cur.execute('INSERT INTO Tracks(title, plays) VALUES (?, ?)', ('Poison', 80))

cur.execute('INSERT INTO Tracks(title, plays) VALUES (?, ?)', ('Eu tenho medo', 10))

cur.execute('INSERT INTO Tracks(title, plays) VALUES (?, ?)', ('Cant Hold Us', 40))

con.commit()

print('\nMeu TOP 10:\n')
cur.execute('SELECT * FROM Tracks')
for row in cur:
    print(row)

cur.execute('DELETE FROM Tracks')
con.commit()
cur.close()