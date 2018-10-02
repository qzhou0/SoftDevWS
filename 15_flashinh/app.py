"""
JaQi-Qian -- Jabir Chowdhury, Qian Zhou
SoftDev1 pd07
K15 -- Oh yes, perhaps I do
2018-10-02
"""

from flask import Flask,render_template,request,session,url_for,redirect,flash
import os

app = Flask(__name__)

app.secret_key = os.urandom(32)
login_credentials = {"usern" : "passw"}

@app.route("/")
def loginPage():
    if "usern" in session:
        # print("user already in session")
        return render_template("homepage.html", user = "usern")
    return render_template("login.html")

@app.route("/auth", methods=["POST"])
def homePage():
    username_input = request.form.get("username")
    password_input = request.form.get("password")
    #dict.get() handles key error exceptions
    if login_credentials.get(username_input) == password_input:
        # print("made it!")
        session[username_input] = password_input
        # print(session)
        #return render_template("homepage.html", user = username_input)
        return redirect(url_for('loginPage'))
    else:
        # print("Failed login")
        if username_input not in login_credentials:
            flash("Invalid username, try again!")
            return redirect(url_for('loginPage'))
            #return render_template("login.html")
        else:
            flash("Invalid password, try again!")
            return redirect(url_for('loginPage'))
            #return render_template("login.html")

@app.route("/logout", methods=["GET"])
def logOut():
    if ("usern" in session):
        session.pop("usern")
    return redirect(url_for("loginPage"))

if __name__ == "__main__":
    app.debug = True
    app.run()
