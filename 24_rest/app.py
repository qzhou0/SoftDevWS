"""
Qian Zhou
SoftDev1 pd07
K24 -- A RESTful Journey Skyward
2018-11-13
"""

from flask import Flask, render_template
import urllib
import json

app = Flask(__name__)

@app.route("/")
def root():

    s = urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY').read()
    
 
    
    d=json.loads(s)
    #print(u)
    print(s)
    #print(d)
    return render_template("a.html", pic = d['url'], expl=d['explanation'])

if __name__=="__main__":
    app.debug=True
    app.run()
