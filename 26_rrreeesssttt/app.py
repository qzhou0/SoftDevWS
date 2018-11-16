"""
Qian Zhou
SoftDev1 pd07
K26-- Getting More REST
2018-11-15
"""

import json
import random
from urllib import request

from flask import Flask, render_template

app = Flask(__name__)




@app.route("/")
def root():
    #WIKI_URL='https://en.wikipedia.org/api/rest_v1/page/segments/'
    #WIKI_URL='https://en.wikipedia.org/api/rest_v1/page/summary/'
    FDA_URL='https://api.fda.gov/food/enforcement.json?search='
    FDA_QURY='classification:"Class+III"&limit=100'

    SPCX_URL='https://api.spacexdata.com/v3/dragons'

    WIKI_URL='https://en.wikipedia.org/api/rest_v1/page/random/summary'
    title=''
    #title = "Sleep"
    #Obj_Num= str(random.randint(1,472586))
    req= WIKI_URL + title
    
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
    
    """
print("-----------------------------")
        
#print("public Domain")
#print (d['isPublicDomain'])
print(s)
print(d['constituents'][0]['name'])
print("------------------------------------------")
"""
        
    WikiContnt = d['extract']
    #content = d['segmentedContent']
    
    
    req=FDA_URL+FDA_QURY
    response= request.urlopen(req)
    s=response.read()
    """
    print("-----------------------------")
    print("response")
    print (s)
    print("------------------------------------------")
    """
    d=json.loads(s)
    r=random.randint(0,100)
    FDAContent = d['results'][r]['state']+','+d['results'][r]['country']+"   :   "
    FDAContent +=d['results'][r]['reason_for_recall']
    FDAContent += d['results'][r]['distribution_pattern']

    req=SPCX_URL
    response=request.urlopen(req)
    s=response.read()
    print("-----------------------------")
    print("response")
    print (s)
    
    print("------------------------------------------")
    d=json.loads(s)
    print(d)
    id=random.randint(0,1)
    n=random.randint(0,len(d[id]['flickr_images'])-1)
    
    spacexIm=d[id]['flickr_images'][n]
    
    return render_template("a.html", WikiContent=WikiContnt,
                                     FDAC = FDAContent,
                                     star=spacexIm)

if __name__=="__main__":
    app.debug=True
    app.run()
