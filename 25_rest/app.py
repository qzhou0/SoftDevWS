"""
Qian Zhou
SoftDev1 pd07
K15 -- Getting More REST
2018-11-14
"""

import json
import random
from urllib import request

from flask import Flask, render_template

app = Flask(__name__)




@app.route("/")
def root():

    """open file of available items"""
    f = open('availItems.txt')
    r = f.read()
    availItems=r.split( ',')
    
    MET_URL= 'https://collectionapi.metmuseum.org/public/collection/v1/objects/'

    accessible = False

    while not accessible:
        Obj_Num = str(random.choice(availItems))
        #Obj_Num= str(random.randint(1,472586))
        req= MET_URL + Obj_Num

        """
        print("------------------------------------------")
        print("request:")
        print(req)
        print("------------------------------------------")
        """
        
        response = request.urlopen(req)
        s = response.read()
        #s for string of request

        """
        print("-----------------------------")
        print("response")
        print (s)
        print("------------------------------------------")
        """

        d=json.loads(s)
        #d for dictionary of object
        if d['constituents']== None:
            name = "n/a"
        else:
            name = d['constituents'][0]['name']
        """
        print("-----------------------------")
        
        #print("public Domain")
        #print (d['isPublicDomain'])
        print(s)
        print(d['constituents'][0]['name'])
        print("------------------------------------------")
        """
        
        accessible= d['isPublicDomain']

    
    
    
    
    #print(d)
    return render_template("a.html", pic =d['primaryImage'],
                                     titl=d['title'],
                                   author=name)

if __name__=="__main__":
    app.debug=True
    app.run()
