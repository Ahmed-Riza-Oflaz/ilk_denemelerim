from flask import Flask,render_template,redirect,request,url_for,flash,logging,session

from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "POST":
        return render_template("05,2_FK-H.html")
    else:
        return render_template("05,2_FK-H.html")

@app.route("/login")
def a_etiketi():
    return redirect(url_for("login"))



@app.route("/kayıt_formu", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return render_template("05_FK-H.html")
    else:
        return render_template("05,1_FK-H.html")
    

if __name__ == "__main__":
    app.run(debug=True)