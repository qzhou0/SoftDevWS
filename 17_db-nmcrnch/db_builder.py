import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

def main():
    DB_FILE= "discobandit.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops
    command = "CREATE TABLE peeps(name TEXT, age INTEGER, id INTEGER PRIMARY KEY)"
    c.execute(command)
    with open("peeps.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            command = 'INSERT INTO peeps VALUES (?,?,?)'
            c.execute(command,(row['name'],row['age'],row['id']))
    command = "CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)"
    c.execute(command)
    with open("courses.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            command = 'INSERT INTO courses VALUES (?,?,?) '
            c.execute(command,(row['code'],row['mark'],row['id']))
    db.commit() #save changes
    db.close()  #close database

# DB_FILE= "foo.db"
# db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
# c = db.cursor()               #facilitate db ops
# command = "CREATE TABLE {table_name}(job class TEXT, percentage INTEGER)".format(table_name = "occupations")
# c.execute(command)
# with open("occupations.csv", newline = "") as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         command = 'INSERT INTO occupations VALUES ("{job}", {percentage}) '.format(job=row['Job Class'],percentage=row['Percentage'])
#         c.execute(command)
# db.commit() #save changes
# db.close()  #close database



