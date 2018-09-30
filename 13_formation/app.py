"""
Qian Zhou
SoftDev1 pd07
K13 -- Echo Echo Echo . . .
2018-09-27
"""

from flask import Flask, render_template, request
from random import random
app = Flask(__name__)

@app.route("/")
def base():
    r = random()
    if r <0.5:
        method = "POST"
    else:
        method = "GET"
                 
    return render_template("input.html", meth=method)

@app.route("/auth", methods = ["POST", "GET"])
def authenticate():
    #print(request.cookies)
    """    print(app)
    print(request)
    print(request.method)
    
    print(request.args)
    print(request.args['username'])
    print(request.headers)"""
    if (request.method == "POST"):
        word = request.form['words'].rsplit(" ")
        usrnm = request.form['username']
    else:
        word = request.args['words'].rsplit(" ")
        usrnm= request.args['username']
    
    word.reverse()
    return render_template("authresp.html",
                            username_entered = usrnm,
                            reply = word,
                            reqmeth=request.method)


if __name__=="__main__":
    app.debug=True
    app.run()
