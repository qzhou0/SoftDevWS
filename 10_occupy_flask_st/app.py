""" RamenNoodles -- Adil Gondal, Qian Zhou
SoftDev1 pd07
K10 -- Jinja Tuning ...
2018-09-22"""
import csv
import random
from flask import Flask, render_template

app = Flask(__name__)



"""@app.route("/temp")
def temp():
    return render_template("occdatatemp.html")
"""

@app.route("/occupations")
def renderOcc():
    occupC=[]
    rateC =[]
    master=[]
    with open("data/occupations.csv") as f:
        for line in iter(f.readline, ""):
            servant=[]
            if line[0]=="\"":
                e = line[1:].find("\"")+1
                #occupC.append(line[1:e])
                #rateC.append(line[e+2:line.find("\n")])
                servant.append(line[1:e])
                servant.append(line[e+2:line.find("\n")])
            else:
                e=line.find(",")
                ##occupC.append(line[:e])
                #rateC.append(line[e+1:line.find("\n")])
                servant.append(line[:e])
                servant.append(line[e+1:line.find("\n")])
            master.append(servant)    
        f.closed
    remaining_percentage=100.0
    j = 1

    while (j<len(master) -1):#uses DK's approach from last similar hw
        if random.random()<float(master[j][1])/remaining_percentage:
            return render_template("occdatatemp.html",
                                   titl="Occupation!",
                                   thineOcc=master[j][0],
                                   th = master[0],
                                   magarita=master[1:])

        else:
            remaining_percentage -= float(master[j][1])
            j+=1
            
    return render_template("occdatatemp.html",
                           titl="Occupation!",
                           thineOcc="Alas, thou art not in our list",
                           th = master[0],
                           magarita=master[1:])       

            
            

if __name__=="__main__":
    app.debug=True
    app.run()
            
