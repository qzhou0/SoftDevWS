#Jabir Chowdhury, Qian Zhou
#SoftDev1 pd7
#K14 -- Do I Know You?    this
#2018-10=01

from flask import Flask,render_template,request,session, url_for, redirect

app = Flask(__name__)

app.secret_key = "not secret"
# secrets should not be put public, but this file is public

loggedIn = False
password="psswrd"
username ="srnm"
@app.route("/")
def log():
    
    if len(session)!=0 :
        return redirect(url_for('authenticate'))
    else:
        return render_template("login.html")

@app.route('/auth')
def authenticate():
    #print (url_for('log'))
    #print (url_for('authenticate'))
    
    if len(session)==0:# if not logged in
        if (len(request.args)==0):
            return redirect(url_for('log'))
        if (request.args['username'] not in session.keys()):
            session[request.args["username"]]=request.args['password']
        key = list(session.keys())[0]
        if key == username:# checks for username
            if session[key]==password:# checks for password
                return redirect(url_for('authenticate'))
            else:
                words  = "bad passowrd"
        else:
            words = "nonexistent username"
        session.pop(key)
        return render_template('welcome.html',
                               correct = False,
                               name = words)
    else:#if already logged in
        words = list(session.keys())[0]
        return  render_template('welcome.html',
                           correct = True,
                           name = words)

@app.route('/out')
def logout():
    #loggedIn = False
    if (len(session)!=0):
        session.pop(list(session.keys())[0])
    return redirect(url_for('log'))

    
if __name__ == "__main__":
    app.debug = True
    app.run()
