"""
Qian Zhou
SoftDev1 pd07
K13 -- Echo Echo Echo . . .
2018-09-27
"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def base():
    return render_template("input.html")

@app.route("/auth")
def authenticate():
    print(request)
    """    print(app)
    print(request)
    print(request.method)
    
    print(request.args)
    print(request.args['username'])
    print(request.headers)"""
    word = request.args['words'].rsplit(" ")
    word.reverse()
    return render_template("authresp.html",
                            username_entered = request.args['username'],
                            reply = word,
                            reqmeth=request.method)


if __name__=="__main__":
    app.debug=True
    app.run()
