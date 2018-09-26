""" RamenNoodles -- Adil Gondal, Qian Zhou
SoftDev1 pd07
K10 -- Jinja Tuning ...
2018-09-22"""

from flask import Flask, render_template
from util import occ_rateFxn
app = Flask(__name__)
            
"""@app.route("/temp")
def temp():
    return render_template("occdatatemp.html")
"""

@app.route("/occupations")
def renderOcc():
    # read data

    listOlist = occ_rateFxn.readNameRateCSV("occupations.csv")
    #display data
    #R02 removed
    return render_template("occdatatemp.html",
                           titl="Occupation!",
                           thineOcc= occ_rateFxn.randomOcc(listOlist),
                           th = listOlist[0],#table heading
                           superL=listOlist[1:])

            
            

if __name__=="__main__":
    app.debug=True
    app.run()

