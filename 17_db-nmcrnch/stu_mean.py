#PwdPwd - Ivan Zhang and Qian Zhou
#SoftDev1 pd7
#K #17: Average, ... or Basic?
#2018-10-06

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O
import db_builder
#==========================================================
db_builder.main()

DB_FILE="discobandit.db"
db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops
#======================== our hw ===============================

def name_to_id(name): #Given a student's name, returns their id number, otherwise None
    cmd = 'SELECT id FROM peeps WHERE name = "{}"'.format(name)
    cur = c.execute(cmd)
    i_d = cur.fetchone()
    if i_d:
        return i_d[0]
    return None
def id_to_name(id):
    cmd = 'SELECT name FROM peeps WHERE id = "{}"'.format(id)
    cur = c.execute(cmd)
    nomen = cur.fetchone()
    if nomen:
        return nomen[0]
    return None
#print(name_to_id('alison'))

#looks up grades of student
def getGrades(name): #Returns grades of students in 2D array [[course1, grade1], ...]
    _id = name_to_id(name)
    if not _id:
        return None
    else:
        cmd = "SELECT code, mark FROM courses WHERE courses.id = {}".format(_id)
        cur = c.execute(cmd)
        grades = cur.fetchall()
        l_grades = []
        for grade in grades:
            l_grades.append([grade[0], grade[1]])
        return l_grades

#print(getGrades('alison'))
#----------------------^^ specific retrieval functions ^^----------

def stuNames():
    cmd = "SELECT name FROM peeps"
    cur = c.execute(cmd)
    return cur.fetchall()# [(name),(name)] 
#--------------------^^ general retrieval function ^^ ---------------


#display each stu's courses and respective grades
def gradeBook(): #Gives a gradebook of each student's courses and grades
    students =  stuNames()
    res = ""
    for stu in students:
        list_of_grades = getGrades(stu[0])
        res += "\nGrades for " + stu[0] + ":\n"
        for course in list_of_grades:
            res += course[0] + ": " + str(course[1]) + "\n"

    return res
print("\n---------------------Gradebook---------------------\n")
print(gradeBook())

def get_average(name):#computes average of a student
    grades = getGrades(name)
    if grades:
        total = 0.0
        for gra in grades:
            total += gra[1]

        return total/len(grades)
    return None

#display students' averages
def averageBook(): #Gives average of students
    students = stuNames()
    res = ""
    for stu in students:
        res += "\nAverage of " + stu[0] + ": " + str(get_average(stu[0]))

    return res

print("\n---------------------TABLE OF AVERAGES---------------------\n")
print(averageBook())

#display each student's name, id, and average
def createGradebook_avg(): #Creates a grade book with name, id, and average
    students = stuNames()
    res = ""
    for stu in students:   
        res += "Name: {}, ID: {}, Average = {} \n".format(stu[0], name_to_id(stu[0]), get_average(stu[0]))
    return res

print("\n---------------------STUDENT DATA---------------------\n")
print(createGradebook_avg()) 

#----------------------^^ display functions ^^-----------------------

def createAvgTable(): #Creates a table of id, avg
    cmd = "CREATE TABLE peeps_avg (id INTEGER, average REAL)"
    cur = c.execute(cmd)
    students = stuNames() 
    res = ""
    for stu in students: 
        cmd = "INSERT INTO peeps_avg VALUES({}, {})".format(name_to_id(stu[0]), get_average(stu[0]))
        cur = c.execute(cmd)
    return
createAvgTable()
db.commit()

#----------------------^^ creates table ^^ -------------------

def changeAvrg(id, new):
    cmd = "UPDATE peeps_avg SET average = "+str(new)+" WHERE id="+str(id)
    c.execute(cmd)
    return
changeAvrg(9, 199)
#-----------------------^^ cheating fxn ^^--------------------

def addRowCourses(code, mark, id):# adds a course, a mark, for a id to courses
    cmd ='INSERT INTO courses VALUES("{_code}", {_mark}, {_id})'.format(_code = code, _mark = mark, _id = id)
    c.execute(cmd)
    changeAvrg(id,get_average(id_to_name(id)))
    return

addRowCourses("pokemon", 88, 8)
#------------------^^ add course function ^^---------------


db.commit() #save changes
db.close()  #close database
            #facilitate db ops

