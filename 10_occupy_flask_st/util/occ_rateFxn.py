""" RamenNoodles -- Adil Gondal, Qian Zhou
SoftDev1 pd07
K10 -- Jinja Tuning ...
2018-09-25"""

import csv
import random

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

def readNameRateCSV(csvF):
    # read data
    listOlist=[] #to contain subgroups for iteration purposes
    with open("data/"+csvF) as f:
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
    return listOlist
