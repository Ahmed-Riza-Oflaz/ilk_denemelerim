from flask import Flask,render_template,url_for,redirect,request

app= Flask(__name__)

@app.route("/")
def HOME():
        return render_template("02_FK-H.html")


@app.route("/LOGİN", methods=['POST', 'GET'] )
def LOGİN():
     return render_template("02,1_FK-H.html")


@app.route("/LOGİN/Kullanıcı")
def Kullanıcı():
     return render_template("02,2_FK-H.html")


# @app.route("/kullanıcı", methods=['POST', 'GET'])
# def LOGİN():
#     if request.method == 'POST':
#         name= request.form[name]
#         return redirect(url_for(""))
#     else:
#         return render_template("02_FK-H.html", name=name )



if __name__ == "__main__":
    app.run(debug=True)