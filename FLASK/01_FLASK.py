from flask import Flask, render_template,redirect,url_for,request

app = Flask(__name__)

@app.route("/")
def ana_sayfa():
    return render_template("01,1_FK-H.html")



@app.route("/users/<name>")
def kullaniciadi(name):
    if name == "admin":
        return redirect(url_for("yönetici"))
        
    print(name)
    return render_template("01_FK-H.html",name=name)


@app.route("/admin")
def yönetici():
    return render_template("01,2_FK-H.html")


@app.route("/toplam/<int:sayi_1>/<int:sayi_2>")
def toplam(sayi_1,sayi_2):
    toplam = sayi_1+sayi_2
    return render_template("01_FK-H.html",sayı_1=sayi_1,sayı_2=sayi_2,toplam=toplam)







if __name__ == "__main__":
    app.run(debug=True)

