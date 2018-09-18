"""Qian Zhou
SoftDev1 pd07
K08 -- Fill Yer Flask
2018-09-20"""

from flask import Flask
app=Flask(__name__) #create instance of flask

@app.route("/")
def helworld():
    return "hablo peble passo"
@app.route("/jelly")
def jel():
    return "biw for something different"
@app.route("/beans")
def b():
    return "hi"
if __name__=="__main__":
    app.debug=True
    app.run()
