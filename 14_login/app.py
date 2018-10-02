"""
JaQi-Qian -- Jabir Chowdhury, Qian Zhou
SoftDev1 pd07
K14 -- Do I Know You?    this
2018-10-01
"""

from flask import Flask,render_template,request,session,url_for,redirect
import os

app = Flask(__name__)

app.secret_key = os.urandom(32)
login_credentials = {"usern" : "passw"}

@app.route("/")
def loginPage():
    if "usern" in session:
        # print("user already in session")
        return render_template("homePage.html", user = "usern")
    return render_template("login.html", error= "")

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
            return render_template("login.html", error = "Invalid username, try again!")
        else:
            return render_template("login.html", error = "Invalid password, try again!")

@app.route("/logout", methods=["GET"])
def logOut():
    session.pop("usern")
    return redirect(url_for("loginPage"))

if __name__ == "__main__":
    app.debug = True
    app.run()
