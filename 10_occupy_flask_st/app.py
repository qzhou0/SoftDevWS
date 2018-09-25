""" RamenNoodles -- Adil Gondal, Qian Zhou
SoftDev1 pd07
K10 -- Jinja Tuning ...
2018-09-22"""
import csv
import random
from flask import Flask, render_template

app = Flask(__name__)


def randomOcc(superlist):#super is of form occ_rate
    remaining_percentage=100.0
    j = 1#counter to go through different occ_rate of listOlist
    while j < len(superlist):
        if random.random()<float(superlist[j][1])/remaining_percentage:#if chance hath befallen
            return superlist[j][0]
        else:
            remaining_percentage-=float(superlist[j][1])
            j+=1
    return "Alas, thou art not in our list"
            
"""@app.route("/temp")
def temp():
    return render_template("occdatatemp.html")
"""

@app.route("/occupations")
def renderOcc():
    # read data
    listOlist=[] #to contain subgroups for iteration purposes
    with open("data/occupations.csv") as f:
        for line in iter(f.readline, ""):
            occ_rate=[] #[0] is occupation, [1] is rate
            if line[0]=="\"":# if first element of line is a "
                sep = line[1:].find("\"")+1 #find index of next " -1
                occ_rate.append(line[1:sep])# this is job
                occ_rate.append(line[sep+2:line.find("\n")])# rest is rate, should not include new line symbol
            else:
                sep=line.find(",")# find "," so that we know the thing before it is occupation, after is rate
                occ_rate.append(line[:sep])
                occ_rate.append(line[sep+1:line.find("\n")])
            listOlist.append(occ_rate)    
        f.closed
    #display data
    #R02 removed
    return render_template("occdatatemp.html",
                           titl="Occupation!",
                           thineOcc= randomOcc(listOlist),
                           th = listOlist[0],
                           magarita=listOlist[1:])

            
            

if __name__=="__main__":
    app.debug=True
    app.run()

"""#R02
    remaining_percentage=100.0
    j = 1#counter to go through different occ_rate of listOlist
    while (j<len(listOlist) -1):#uses DK's approach from last similar hw
        if random.random()<float(listOlist[j][1])/remaining_percentage:#if chance hath befallen
            return render_template("occdatatemp.html",
                                   titl="Occupation!",
                                   thineOcc=listOlist[j][0],
                                   th = listOlist[0],#table heading should be first line of csv
                                   magarita=listOlist[1:])#content

        else:
            remaining_percentage -= float(listOlist[j][1])
            j+=1
            
    return render_template("occdatatemp.html",
                           titl="Occupation!",
                           thineOcc=,
                           th = listOlist[0],
                           magarita=listOlist[1:])    """
