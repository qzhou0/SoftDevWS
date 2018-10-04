#Clyde "Thluffy" Sinclair
#SoftDev1 pd0
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

def csvdb(f):
    fn=f[:f.find(".csv")]
    cmd="CREATE TABLE " + fn
    with open(f) as csvfile:
        reader = csv.DictReader(csvfile)
        i=0
        
        for row in reader:
            k = list(row.keys())
            if i==0:
                cmd+="(" +k[0]+"TEXT, "+k[1]+"INTEGER, "+k[2]+"INTEGER)"
                c.execute(cmd)
                i+=1
            cmd = "INSERT INTO "+fn+" VALUES (?,?,?)"
            values = [(row[k[0]],
                       row[k[1]],
                       row[k[2]])]
            c.executemany(cmd, values)
#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

csvdb("peeps.csv")
csvdb("courses.csv")
#command = ""          #build SQL stmt, save as string
#c.execute(command)    #run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database


