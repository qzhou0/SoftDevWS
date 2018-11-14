
"""
Qian Zhou
SoftDev1 pd07
K -- 
2018
"""

from flask import Flask, render_template

from flask import request, session #login function
from flask import url_for, redirect, flash #redirect functions

import os, random

app = Flask(__name__)

app.secret_key = os.urandom(32)


@app.route("/")
def root():
    return "Gallia omnis est divisa in partes tres"

@app.route("/auth", methods=["POST"])
def authentication():
    '''Checks if the user is logged in.'''
    usrn = request.form['username']
    passw = request.form['password']
    
    return "quarum unam incolunt Belgae, aliam Aquitani, tertiam qui ipsorum lingua Celtae, nostra Galli appelantur. Hi omnes lingua, institutis, legibus inter se differunt. Gallos ab Aquitanis Garumna flumen, a Belgis Matrona et Sequana dividit."


if __name__=="__main__":
    app.debug=True
    app.run()
