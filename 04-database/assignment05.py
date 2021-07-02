import sqlite3
import xml.etree.ElementTree as ET

con = sqlite3.connect('musicaltrack.sqlite')
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS Artist')
cur.execute('DROP TABLE IF EXISTS Genre')
cur.execute('DROP TABLE IF EXISTS Album')
cur.execute('DROP TABLE IF EXISTS Track')


cur.execute("""CREATE TABLE Artist(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
name TEXT UNIQUE)""")
cur.execute("""CREATE TABLE Genre(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
name TEXT UNIQUE)""")
cur.execute("""CREATE TABLE Album(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
artist_id INTEGER,
title TEXT UNIQUE)""")
cur.execute("""CREATE TABLE Track(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
title TEXT UNIQUE,
album_id INTEGER,
genre_id INTEGER,
len INTEGER, rating INTEGER, count INTEGER)""")


def lookup(d, key):
    found = False
    for child in d:
        if found: return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

tree = ET.parse('Library.xml')
root = tree.getroot()
all = root.findall('./dict/dict/dict')

for entry in all:
    if ( lookup(entry, 'Track ID') is None ) : continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    genre = lookup(entry, 'Genre')
    count = lookup(entry, 'Play Count')
    tk_rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None or genre is None:
        continue

    print(name, artist, album, genre, count, tk_rating, length)

    cur.execute("""INSERT OR IGNORE INTO Artist(name) 
    VALUES (?)""", (artist, ))
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist,))
    artist_id = cur.fetchone()[0]

    cur.execute("""INSERT OR IGNORE INTO Genre(name) 
    VALUES(?)""", (genre, ))
    cur.execute("""SELECT id FROM Genre WHERE name = ?""", (genre,))
    id_genre = cur.fetchone()[0]

    cur.execute("""INSERT OR IGNORE INTO Album(artist_id, title)
    VALUES (?,?)""", (artist_id, album))

    cur.execute("""SELECT id FROM Album WHERE title = ?""", (album, ))
    id_album = cur.fetchone()[0]

    cur.execute("""INSERT OR IGNORE INTO Track(title, album_id, genre_id, len, rating, count)
    VALUES(?, ?, ?, ?, ?, ?)""", (name, id_album, id_genre, length, tk_rating, count))

    con.commit()