
"""
Qian Zhou
SoftDev1 pd07
K -- 
2018
"""

from flask import Flask, render_template
from flask import request, session
from flask import url_for, redirect, flash
import os, random

app = Flask(__name__)

@app.route("/")
def root():
    return "Gallia omnis est divisa in partes tres"

if __name__=="__main__":
    app.debug=True
    app.run()
