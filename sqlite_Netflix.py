import sqlite3
import csv

conn = sqlite3.connect('NetFlix_database.db')
c= conn.cursor()

#Drop table
c.execute("DROP TABLE IF EXISTS tvshows")
#creating table
c.execute("CREATE TABLE tvshows(id INTEGER PRIMARY KEY AUTOINCREMENT, tvshows text, seasons Integer, ratings Float)")
conn.commit()

#Insert In Table
c.execute("INSERT INTO tvshows(tvshows,seasons,ratings) VALUES ('The Flash',5,4.7)")
conn.commit()

#showname=input("Enter ShowName: ")
#season = int(input("Enter total seasons: "))
#rating = float(input("Enter ratings: "))
c.execute("INSERT INTO tvshows(tvshows,seasons,ratings) VALUES (?,?,?)",("YOU",2,5))
conn.commit()

#Update into Table
c.execute("UPDATE tvshows set ratings =4.9 WHERE id = 1")
conn.commit()

#DELETE from Table
c.execute("DELETE from tvshows WHERE id = 1")
conn.commit()



#GETTING CSV FILE INTO TABLE

f = open('NetFlix Records.csv')
reader = csv.reader(f)
count=0
for values in reader:
    if count == 0:
        pass
    else:
        c.execute("INSERT INTO tvshows (tvshows,seasons,ratings) VALUES (?,?,?)",(values[1],values[2],values[3]))
        #print(f'tvshows: {values[1]}, seasons: {values[2]}, ratings: {values[3]}')
    conn.commit()
    count += 1
    



#SELECTING ALL DATA FROM TABLE
get_all = c.execute("SELECT * from tvshows").fetchall()
for i in get_all:
    print(i)