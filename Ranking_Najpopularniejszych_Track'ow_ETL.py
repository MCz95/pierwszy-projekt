#!/usr/bin/python

import sqlite3
import datetime

start = datetime.datetime.now()


def sampleData():
    with open("c:/sqlite/triplets_sample_20p.txt", "r", encoding='utf-8') as contentA:
        sample = []
        for row in contentA:
            a = row.split(";")
            sample.append(a)
        return sample


def uniqueData():
    with open("c:/sqlite/unique_tracks.txt", "r", encoding='utf-8') as contentB:
        unique = []
        for row in contentB:
            b = row.split(";")
            unique.append(b)
        return unique


conn = sqlite3.connect("c:/sqlite/ETL.db")
c = conn.cursor()

triplets = sampleData()
tracks = uniqueData()

c.execute('''CREATE TABLE listeners
    (userID CHAR(4), trackID CHAR(5), date TEXT)''')
c.executemany("INSERT INTO listeners VALUES(?, ?, ?)", triplets)

c.execute('''CREATE TABLE artists
    (exID INTEGER, trackID CHAR(5), artist TEXT, title TEXT, length INTEGER)''')
c.executemany("INSERT INTO artists VALUES(?, ?, ?, ?, ?)", tracks)


def mpA():
    c.execute('SELECT artist, count(artist) FROM listeners INNER JOIN artists\n'
              'ON listeners.trackID = artists.trackID\n'
              'GROUP BY artist ORDER BY count(*) DESC')

    name = c.fetchone()[0]
    print("The most popular artist is " + name + ".\n")


def mpT():
    print("The 5 most popular tracks are: ")
    c.execute('SELECT title, count(title) FROM listeners INNER JOIN artists\n'
              'ON listeners.trackID = artists.trackID\n'
              'GROUP BY title ORDER BY count(*) DESC')
    rows = c.fetchmany(5)
    counter = 1
    while counter <= 5:
        for row in rows:
            print(str(counter) + ". Title: " + row[0])
            print("Listened " + str(row[1]) + " times.")
            counter += 1


sampleData()
uniqueData()
mpA()
mpT()
conn.commit()
conn.close()
elapsed = datetime.datetime.now() - start
print("\nThe data processing time is: ", elapsed.microseconds, " microseconds")
