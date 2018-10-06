

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

#==========================================================

DB_FILE="discobandit.db"
db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#----------------------

def looknameid():
    cmd = "SELECT name, mark,peeps.id FROM peeps, courses WHERE peeps.id = courses.id"
    cur = c.execute(cmd)
    #print(cur.fetchall())
    return cur #list of name, grade, and id
grades = looknameid()

def gradeBook(grades):
    stuG={}
    for i in grades:
        #print (i)
        if i[0] in stuG:
            stuG[i[0]][0]+=i[1]#add grade
            stuG[i[0]][1]+=1#add course
        else:
            stuG[i[0]]=[i[1],1,i[2]]
    return stuG#(name:[total grade, courses taken, id])
stuG=gradeBook(grades)
#print(stuG)

def displayAvrg(gb):#returns a csv separated with each id and student average
    k = gb.keys()
    s=""
    for key in k:
        #print(key,stuG[key][2],stuG[key][0]/stuG[key][1])
        s+=key+","+str(stuG[key][2])+","+str(stuG[key][0]/stuG[key][1])+"\n"
    return s[:len(s)-2]
print(displayAvrg(stuG))

def averageTable(csvNameIDaverg):
    #creates table
    cmd = "CREATE TABLE peeps_avg (id INTEGER, average REAL)"
    c.execute(cmd)

    # insertion
    for line in csvNameIDaverg.split("\n"):
        cmd = "INSERT INTO peeps_avg VALUES ({}{})".format(
            line[line.find(",")+1:line.rfind(",")],line[line.rfind(","):])
        #print(cmd)
        c.execute(cmd)
    return
averageTable(displayAvrg(stuG))
#inserts new value
def changeAvrg(id, new):
    cmd = "UPDATE peeps_avg SET average = "+str(new)+" WHERE id="+str(id)
    c.execute(cmd)
    return
changeAvrg(9, 199)

def addRowCourses(code,mark, id):# adds a course, a mark, for a id to courses
    cmd ='INSERT INTO COURSES VALUES("'+code+'",'+str(mark)+','+str(id)+")"
    print(cmd)
    c.execute(cmd)
    cmd = "SELECT name FROM peeps WHERE id =" +str(id)
    for r in c.execute(cmd):
        if r[0] in stuG:
            stuG[r[0]][0]+=mark
            stuG[r[0]][1]+=1
        else:
            stuG["n.k."]=[mark, 1,id]
        changeAvrg(id, stuG[r[0]][0]/stuG[r[0]][1])
    
    return
print(c.execute("SELECT average FROM peeps_avg WHERE id = 8").fetchone())

addRowCourses("ceramics",88, 8)


db.commit() #save changes
db.close()  #close database
            #facilitate db ops

