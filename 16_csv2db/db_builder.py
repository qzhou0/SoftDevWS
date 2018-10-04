# Maggie Zhao & Qian Zhou
# SoftDev1 pd7
# K16-- No Trouble
# 2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

#==========================================================

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE


#building peeps table

command = "CREATE TABLE peeps(name TEXT, age INTEGER, id INTEGER)"

#build SQL stmt, save as string
c.execute(command)    #run SQL statement
with open('peeps.csv') as csvfile:
    readerPeeps = csv.DictReader(csvfile)
    for row in readerPeeps:
		#prepares execute many
        command = "INSERT INTO peeps VALUES (?,?,?)" 
        c.executemany(command, values)



command = "CREATE TABLE courses(name TEXT, age INTEGER, id INTEGER)"

#build SQL stmt, save as string
c.execute(command)

with open('courses.csv') as csvfile:
    readerCourses = csv.DictReader(csvfile)
    for row in readerCourses:
        command = "INSERT INTO courses VALUES (?,?,?)"
        values = [(row["code"], row["mark"], row["id"])]

        c.executemany(command, values)
#==========================================================

db.commit() #save changes
db.close()  #close database
