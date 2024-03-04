from flask import Flask,render_template,redirect,request,url_for,flash,logging,session

from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt


class RegisterForm(Form):
    name = StringField("isim soyisim",validators=[validators.length(min=4, max= 25)] )
    username = StringField("kullanıcı adı",validators=[validators.Length(min=4, max=25)] )
    email = StringField("email",validators=[validators.Length(min=10, max=35),validators.Email(message= "geçerli email adresi giriniz...") ] )
    password = PasswordField("parola:")

    confirm = PasswordField("parola doğrula")



app = Flask(__name__)



app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "01_flask_denme"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)



@app.route("/")
def ANASAYFA():
    return render_template("01_FK-H.html")

@app.route("/04_FK-H.html", methods=["POST", "GET"] )
def deneme_sayfası():
    form = RegisterForm(request.form)

    if request.method == "POST" and form.validate():
        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(form.password.data)

        cursor = mysql.connection.cursor()

        sorgu = "Insert into users(name,username,email,password) VALUES(%s,%s,%s,%s)"

        cursor.execute(sorgu,(name,email,username,password))
        mysql.connection.commit()

        cursor.close()

        return render_template("01_FK-H.html")

    else:
        return render_template("04_FK-H.html", form=form )



if __name__ == "__main__":
    app.run(debug=True)