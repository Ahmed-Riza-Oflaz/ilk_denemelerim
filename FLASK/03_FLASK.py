from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)



@app.route("/", methods=['POST', 'GET'] )
def HOME():
    if request.method == 'POST':
        name = request.form["name"]
        if name == "admin":
            return render_template("03_FK-H.html")
        return redirect(url_for("user", name=name))
    else:
        return render_template("03,1_FK-H.html")

@app.route("/user/<name>")
def user(name):
    return render_template("02,2_FK-H.html", F_name=name )


@app.route("/LOGİN", methods=['POST', 'GET'] )
def login():
    render_template("03,1_FK-H.html")





if __name__ == "__main__":
    app.run(debug=True)